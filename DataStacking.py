import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from scipy.signal import correlate
import matplotlib.pyplot as plt

documents_path = # insert document path

# Define a list of file paths for your CSV files
file_paths = [
    # Enter the csv files you want to compare
]

data_list = []

for file_path in file_paths:
    df = pd.read_csv(file_path)
    
    # Extract the columns from the DataFrame
    time_column = df['Time']
    sensor1_column = df['Sensor A0']
    sensor2_column = df['Sensor A1']
    sensor3_column = df['Sensor A2']

    # Convert the columns to NumPy arrays and append to the list
    data = np.column_stack((time_column.to_numpy(), sensor1_column.to_numpy(), sensor2_column.to_numpy(), sensor3_column.to_numpy()))
    data_list.append(data)

peaks_list = [] 
ref_peaks_list = []

for i in range(len(file_paths)):
    # Find peaks
    peaks, _ = find_peaks(data_list[i][:, 3], height=1.5, distance = 1.2)
    peaks_list.append(peaks)
    
    # Calculate the reference peak for each dataset
    if len(peaks) > 0:
        # If peaks were detected, find the peak with the maximum value
        peak_index = data_list[i][peaks,3]
        ref_peak_data = data_list[i][peaks[0], 0]
    else:
        # If no peaks were detected, set a default value or handle it as needed
        ref_peak_data = None  
        
    ref_peaks_list.append(ref_peak_data)

# Define a list to store the time differences for each dataset
time_differences = []

for i in range(len(file_paths)):
    # Calculate the time difference between the reference peak and the next peak
    if ref_peaks_list[i] is not None and len(peaks_list[i]) > 1:
        time_difference = data_list[i][peaks_list[i][1], 0] - ref_peaks_list[i]
    else:
        # If there's no reference peak or not enough peaks, set the time difference to None or handle it as needed
        time_difference = None

    time_differences.append(time_difference)

print(time_differences)

# peaks_list will now contain the peaks for each dataset
peaks_data1 = peaks_list[0]
peaks_data2 = peaks_list[1]
peaks_data3 = peaks_list[2]
peaks_data4 = peaks_list[3]
peaks_data5 = peaks_list[4]
peaks_data6 = peaks_list[5]
peaks_data7 = peaks_list[6]
peaks_data8 = peaks_list[7]
peaks_data9 = peaks_list[8]
peaks_data10 = peaks_list[9]

# Select reference peaks
ref_peak_data1 = ref_peaks_list[0]
ref_peak_data2 = ref_peaks_list[1]
ref_peak_data3 = ref_peaks_list[2]
ref_peak_data4 = ref_peaks_list[3]
ref_peak_data5 = ref_peaks_list[4]
ref_peak_data6 = ref_peaks_list[5]
ref_peak_data7 = ref_peaks_list[6]
ref_peak_data8 = ref_peaks_list[7]
ref_peak_data9 = ref_peaks_list[8]
ref_peak_data10 = ref_peaks_list[9]

# Calculate the initial time shift based on the reference peaks
time_shift_1_2 = ref_peak_data1 - ref_peak_data2
time_shift_1_3 = ref_peak_data1 - ref_peak_data3
time_shift_1_4 = ref_peak_data1 - ref_peak_data4
time_shift_1_5 = ref_peak_data1 - ref_peak_data5
time_shift_1_6 = ref_peak_data1 - ref_peak_data6
time_shift_1_7 = ref_peak_data1 - ref_peak_data7
time_shift_1_8 = ref_peak_data1 - ref_peak_data8
time_shift_1_9 = ref_peak_data1 - ref_peak_data9
time_shift_1_10 = ref_peak_data1 - ref_peak_data10

# Reasign Data for later timeshift
aligned_data1 = data_list[0]
aligned_data2 = data_list[1]
aligned_data3 = data_list[2]
aligned_data4 = data_list[3]
aligned_data5 = data_list[4]
aligned_data6 = data_list[5]
aligned_data7 = data_list[6]
aligned_data8 = data_list[7]
aligned_data9 = data_list[8]
aligned_data10 = data_list[9]

# Aligns data to the first data signal
aligned_data2[:,0] = aligned_data2[:, 0] + time_shift_1_2
aligned_data3[:,0] = aligned_data3[:, 0] + time_shift_1_3
aligned_data4[:,0] = aligned_data4[:, 0] + time_shift_1_4
aligned_data5[:,0] = aligned_data5[:, 0] + time_shift_1_5
aligned_data6[:,0] = aligned_data6[:, 0] + time_shift_1_6
aligned_data7[:,0] = aligned_data7[:, 0] + time_shift_1_7
aligned_data8[:,0] = aligned_data8[:, 0] + time_shift_1_8
aligned_data9[:,0] = aligned_data9[:, 0] + time_shift_1_9
aligned_data10[:,0] = aligned_data10[:, 0] + time_shift_1_10

# Peak values lined up for A0 which was on the back of the pole
A0_aligned_peak_voltage1 = aligned_data1[peaks_list[0][0], 1]
A0_aligned_peak_voltage2 = aligned_data2[peaks_list[1][0], 1]
A0_aligned_peak_voltage3 = aligned_data3[peaks_list[2][0], 1]
A0_aligned_peak_voltage4 = aligned_data4[peaks_list[3][0], 1]
A0_aligned_peak_voltage5 = aligned_data5[peaks_list[4][0], 1]
A0_aligned_peak_voltage6 = aligned_data6[peaks_list[5][0], 1]
A0_aligned_peak_voltage7 = aligned_data7[peaks_list[6][0], 1]
A0_aligned_peak_voltage8 = aligned_data8[peaks_list[7][0], 1]
A0_aligned_peak_voltage9 = aligned_data9[peaks_list[8][0], 1]
A0_aligned_peak_voltage10 = aligned_data10[peaks_list[9][0], 1]

A0_aligned_peak_voltages = [A0_aligned_peak_voltage1, A0_aligned_peak_voltage2, A0_aligned_peak_voltage3, A0_aligned_peak_voltage4, A0_aligned_peak_voltage5
                            , A0_aligned_peak_voltage6, A0_aligned_peak_voltage7, A0_aligned_peak_voltage8, A0_aligned_peak_voltage9, A0_aligned_peak_voltage10]

# Peak values lined up for A1 which was on the side of the pole
A1_aligned_peak_voltage1 = aligned_data1[peaks_list[0][0], 2]
A1_aligned_peak_voltage2 = aligned_data2[peaks_list[1][0], 2]
A1_aligned_peak_voltage3 = aligned_data3[peaks_list[2][0], 2]
A1_aligned_peak_voltage4 = aligned_data4[peaks_list[3][0], 2]
A1_aligned_peak_voltage5 = aligned_data5[peaks_list[4][0], 2]
A1_aligned_peak_voltage6 = aligned_data6[peaks_list[5][0], 2]
A1_aligned_peak_voltage7 = aligned_data7[peaks_list[6][0], 2]
A1_aligned_peak_voltage8 = aligned_data8[peaks_list[7][0], 2]
A1_aligned_peak_voltage9 = aligned_data9[peaks_list[8][0], 2]
A1_aligned_peak_voltage10 = aligned_data10[peaks_list[9][0], 2]

A1_aligned_peak_voltages = [A1_aligned_peak_voltage1, A1_aligned_peak_voltage2, A1_aligned_peak_voltage3, A1_aligned_peak_voltage4, A1_aligned_peak_voltage5
                            , A1_aligned_peak_voltage6, A1_aligned_peak_voltage7, A1_aligned_peak_voltage8, A1_aligned_peak_voltage9, A1_aligned_peak_voltage10]

# Peak values lined up for A1 which was closest to the hammer
A2_aligned_peak_voltage1 = aligned_data1[peaks_list[0][0], 3]
A2_aligned_peak_voltage2 = aligned_data2[peaks_list[1][0], 3]
A2_aligned_peak_voltage3 = aligned_data3[peaks_list[2][0], 3]
A2_aligned_peak_voltage4 = aligned_data4[peaks_list[3][0], 3]
A2_aligned_peak_voltage5 = aligned_data5[peaks_list[4][0], 3]
A2_aligned_peak_voltage6 = aligned_data6[peaks_list[5][0], 3]
A2_aligned_peak_voltage7 = aligned_data7[peaks_list[6][0], 3]
A2_aligned_peak_voltage8 = aligned_data8[peaks_list[7][0], 3]
A2_aligned_peak_voltage9 = aligned_data9[peaks_list[8][0], 3]
A2_aligned_peak_voltage10 = aligned_data10[peaks_list[9][0], 3]

A2_aligned_peak_voltages = [A2_aligned_peak_voltage1, A2_aligned_peak_voltage2, A2_aligned_peak_voltage3, A2_aligned_peak_voltage4, A2_aligned_peak_voltage5
                            , A2_aligned_peak_voltage6, A2_aligned_peak_voltage7, A2_aligned_peak_voltage8, A2_aligned_peak_voltage9, A2_aligned_peak_voltage10]


A0_PeakDiff = []
A1_PeakDiff = []
A2_PeakDiff = []

# Calculate the time difference between A0 peaks
for i in range(len(A0_aligned_peak_voltages)):
    A0_PeakDiff.append((A0_aligned_peak_voltages[0] - A0_aligned_peak_voltages[i]))

print(A0_PeakDiff)

# Calculate the time difference between A1 peaks
for i in range(len(A1_aligned_peak_voltages)):
    A1_PeakDiff.append((A1_aligned_peak_voltages[0] - A1_aligned_peak_voltages[i]))

print(A1_PeakDiff)

# Calculate the time difference between A2 peaks
for i in range(len(A2_aligned_peak_voltages)):
    A2_PeakDiff.append((A2_aligned_peak_voltages[0] - A2_aligned_peak_voltages[i]))

print(A2_PeakDiff)

Val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
# plt.figure(figsize=(10, 6))
plt.figure(1)
plt.plot(aligned_data1[:, 0], aligned_data1[:, 1], label='A0 Data 1')
plt.plot(aligned_data2[:, 0], aligned_data2[:, 1], label='A0 Data 2 (Aligned)')
plt.plot(aligned_data3[:, 0], aligned_data3[:, 1], label='A0 Data 3 (Aligned)')
plt.plot(aligned_data4[:, 0], aligned_data4[:, 1], label='A0 Data 4 (Aligned)')
plt.plot(aligned_data5[:, 0], aligned_data5[:, 1], label='A0 Data 5 (Aligned)')
plt.plot(aligned_data6[:, 0], aligned_data6[:, 1], label='A0 Data 6 (Aligned)')
plt.plot(aligned_data7[:, 0], aligned_data7[:, 1], label='A0 Data 7 (Aligned)')
plt.plot(aligned_data8[:, 0], aligned_data8[:, 1], label='A0 Data 8 (Aligned)')
plt.plot(aligned_data9[:, 0], aligned_data9[:, 1], label='A0 Data 9 (Aligned)')
plt.plot(aligned_data10[:, 0], aligned_data10[:, 1], label='A0 Data 10 (Aligned)')
plt.xlim(2400,2800)
plt.legend()
plt.grid(True)
plt.savefig(f"")# Enter where you want the figure to be saved

plt.figure(2)
plt.plot(aligned_data1[:, 0], aligned_data1[:, 2], label='A1 Data 1')
plt.plot(aligned_data2[:, 0], aligned_data2[:, 2], label='A1 Data 2 (Aligned)')
plt.plot(aligned_data3[:, 0], aligned_data3[:, 2], label='A1 Data 3 (Aligned)')
plt.plot(aligned_data4[:, 0], aligned_data4[:, 2], label='A1 Data 4 (Aligned)')
plt.plot(aligned_data5[:, 0], aligned_data5[:, 2], label='A1 Data 5 (Aligned)')
plt.plot(aligned_data6[:, 0], aligned_data6[:, 2], label='A1 Data 6 (Aligned)')
plt.plot(aligned_data7[:, 0], aligned_data7[:, 2], label='A1 Data 7 (Aligned)')
plt.plot(aligned_data8[:, 0], aligned_data8[:, 2], label='A1 Data 8 (Aligned)')
plt.plot(aligned_data9[:, 0], aligned_data9[:, 2], label='A1 Data 9 (Aligned)')
plt.plot(aligned_data10[:, 0], aligned_data10[:, 2], label='A1 Data 10 (Aligned)')
plt.xlim(2400,3000)
plt.legend()
plt.grid(True)
plt.savefig(f"")# Enter where you want the figure to be saved

plt.figure(3)
plt.plot(aligned_data1[:, 0], aligned_data1[:, 3], label='A2 Data 1')
plt.plot(aligned_data2[:, 0], aligned_data2[:, 3], label='A2 Data 2 (Aligned)')
plt.plot(aligned_data3[:, 0], aligned_data3[:, 3], label='A2 Data 3 (Aligned)')
plt.plot(aligned_data4[:, 0], aligned_data4[:, 3], label='A2 Data 4 (Aligned)')
plt.plot(aligned_data5[:, 0], aligned_data5[:, 3], label='A2 Data 5 (Aligned)')
plt.plot(aligned_data6[:, 0], aligned_data6[:, 3], label='A2 Data 6 (Aligned)')
plt.plot(aligned_data7[:, 0], aligned_data7[:, 3], label='A2 Data 7 (Aligned)')
plt.plot(aligned_data8[:, 0], aligned_data8[:, 3], label='A2 Data 8 (Aligned)')
plt.plot(aligned_data9[:, 0], aligned_data9[:, 3], label='A2 Data 9 (Aligned)')
plt.plot(aligned_data10[:, 0], aligned_data10[:, 3], label='A2 Data 10 (Aligned)')
plt.xlim(2400,3000)
plt.legend()
plt.grid(True)
plt.savefig(f"")# Enter where you want the figure to be saved

plt.figure(4)
plt.scatter(Val, A0_PeakDiff, color='b', marker='o')
plt.axhline(0, color='r', linestyle='--')  # Add a horizontal line at y=0
plt.grid(True)

plt.figure(5)
plt.scatter(Val, A1_PeakDiff, color='b', marker='o')
plt.axhline(0, color='r', linestyle='--')  # Add a horizontal line at y=0
plt.grid(True)

plt.figure(6)
plt.scatter(Val, A2_PeakDiff, color='b', marker='o')
plt.axhline(0, color='r', linestyle='--')  # Add a horizontal line at y=0
plt.grid(True)

plt.figure(7)
# Create a box plot
plt.boxplot(A0_aligned_peak_voltages)
plt.xlabel("Dataset")
plt.ylabel("Peak Values")
plt.title("Back Sensor Variation of Peak Values")
# plt.grid(True)
plt.savefig(f"")# Enter where you want the figure to be saved

plt.figure(8)
# Create a box plot
plt.boxplot(A1_aligned_peak_voltages)
plt.xlabel("Dataset")
plt.ylabel("Peak Values")
plt.title("Side Sensor Variation of Peak Values")
# plt.grid(True)
plt.savefig(f"")# Enter where you want the figure to be saved

plt.figure(9)
# Create a box plot
plt.boxplot(A2_aligned_peak_voltages)
plt.xlabel("Dataset")
plt.ylabel("Peak Values")
plt.title("Close to Hammer Sensor Variation of Peak Values")
# plt.grid(True)
plt.savefig(f"")# Enter where you want the figure to be saved

plt.show()


