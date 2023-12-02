import serial
import csv
import time
import pandas as pd
import matplotlib.pyplot as plt
import re
import pandas as pd
import numpy as np
from scipy.signal import find_peaks


name = #Enter the name for the pole under test

# Constants
V_cc = 5  # Input voltage
bit_val = 1024 # number of bits

# Enter poles diameter in meters
# Pole_Diameter = 0.961 #meters 0.973
Pole_Diameter = float(input("Enter the diameter of the pole in meters: "))

# Enter the transvers stress wave speed of the wood. On average it's about 1000-1500 m/s so I'm using the minimum to determine time dialation of a good pole
# T_waves = 1000
# Asks the user to select the T_wave speed
print("Select the T_wave speed of the pole:")
print("1. Douglas-fir: 900 m/s")
print("2. Any other type: 1000 m/s") # Safe estimate
choice = input("Enter the number of your choice: ")

# Sets T_waves based on the user's selection
if choice == "1":
    T_waves = 900
elif choice == "2":
    T_waves = 1000
else:
    print("Invalid choice. Using the default value of 1000 m/s.")
    T_waves = 1000


time_pole = Pole_Diameter/T_waves # Time in seconds
print(f"{time_pole:.2e} s")

# Make sure to load code from Arduino software so that each port is up to date with the proper baud rate. When the baud rate changes you need to update this on the arduino software. 
# ser = serial.Serial('/dev/cu.usbmodem14101', 115200) # Left USB port
ser = serial.Serial('/dev/cu.usbmodem14201', 115200) # Right USB port

documents_path = "" # enter documents path
csv_filename = f"{documents_path}/data_{name}.csv"

# Resets Arduino
ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)

# Define the analog pins that you want to read
analog_pins = ['A0', 'A1', 'A2']

def read_and_log_data(ser, filename):
    start_time = time.time()
    end_time = start_time + 5

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ["Time"] + [f"Sensor {pin}" for pin in analog_pins]
        writer.writerow(header)

        while time.time() < end_time:
            try:
                data = ser.readline().decode().strip()

                if data:
                    current_time = time.time()
                    sensor_values = [int(val) * (V_cc / bit_val) for val in re.split(r'[,\s]+', data)]
                    timestamp = int((current_time - start_time) * 1e6)  # Converts to microseconds
                    writer.writerow([timestamp] + sensor_values)

            except serial.SerialException as e:
                print(f"Serial Exception: {e}")

read_and_log_data(ser, csv_filename)

# Read the data and plot
data = pd.read_csv(csv_filename)

# Use if you want to plot all three analog sensors 
# for pin in analog_pins:
#     plt.plot(data['Time'], data[f"Sensor {pin}"], label=f"{pin}", linewidth=1)

plt.plot(data['Time'], data[f"Sensor {analog_pins[1]}"], label=f"{analog_pins[1]}", linewidth=1)
plt.plot(data['Time'], data[f"Sensor {analog_pins[2]}"], label=f"{analog_pins[2]}", linewidth=1)
plt.xlabel('Time [us]')
plt.ylabel('Voltage [V]')
plt.title('Vibration Sensor Data')
plt.grid(True)
plt.legend()
plt.savefig(f"") # Enter location of file where you want images to be saved
# plt.show()

# Close the serial connection
ser.close()

# This second part of the code calculated the time difference between peaks
file_path = f"{documents_path}/data_{name}.csv"
data = pd.read_csv(file_path)

time_values = data['Time']  # Time values of CSV file
signal_columns = ['Sensor A0', 'Sensor A1', 'Sensor A2']  # Sensor values of CSV

# Create a dictionary to store the highest peak times for each signal
highest_peak_info = {}

for signal_column in signal_columns:
    signal_values = data[signal_column]

    # Find all peaks in the signal
    peaks, _ = find_peaks(signal_values, height=0.5)

    # Finds the highest peak that goes from zero to zero, so it completes one peak and neglects spikes that may occur within that peak
    max_peak_index = 0
    max_peak_value = signal_values[peaks[0]]
    for i in range(1, len(peaks)):
        start_index = peaks[i - 1]
        end_index = peaks[i]

        # Check if the peak goes from zero to zero
        if signal_values[start_index] < 0 and signal_values[end_index] < 0:
            # Check if this peak is higher than the current maximum
            if signal_values[end_index] > max_peak_value:
                max_peak_index = i
                max_peak_value = signal_values[end_index]

    # Store the highest peak's time and value for the current signal
    highest_peak_time = time_values[peaks[max_peak_index]]
    highest_peak_info[signal_column] = {'Time': highest_peak_time, 'Value': max_peak_value}

    

# Calculate time differences between the highest peaks of different signals
time_diff_A0_A1 = abs(highest_peak_info['Sensor A1']['Time'] - highest_peak_info['Sensor A0']['Time'])
time_diff_A1_A2 = abs(highest_peak_info['Sensor A2']['Time'] - highest_peak_info['Sensor A1']['Time'])
time_diff_A0_A2 = abs(highest_peak_info['Sensor A2']['Time'] - highest_peak_info['Sensor A0']['Time'])

# Print the highest peak information for each signal
for signal_column, info in highest_peak_info.items():
    print(f"{signal_column} - Highest Peak: Time = {info['Time']} us, Value = {info['Value']} V")

# Print the time differences
print(f"Time difference between Sensor A0 and Sensor A1: {time_diff_A0_A1} us")
print(f"Time difference between Sensor A1 and Sensor A2: {time_diff_A1_A2} us")
print(f"Time difference between Sensor A0 and Sensor A2: {time_diff_A0_A2} us")

# This is a variable that will need to be tested and messed with 
if time_diff_A0_A2 <= 0.98*time_pole:
    print("This pole needs to be investigated further before climbing.")
else:
    print("This poles is safe.")

plt.show()