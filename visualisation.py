import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = '/Users/jayant/Documents/Trimester1-2024/SIT724/sensor_data.csv'
data = pd.read_csv(file_path)
data['Timestamp'] = pd.to_datetime(data['Timestamp'], unit='ms')
data.set_index('Timestamp', inplace=True)

plt.figure(figsize=(14, 7))
plt.subplot(2, 2, 1)
plt.plot(data.index, data['AccelerationX'], label='X Axis', color='r')
plt.plot(data.index, data['AccelerationY'], label='Y Axis', color='g')
plt.plot(data.index, data['AccelerationZ'], label='Z Axis', color='b')
plt.title('Acceleration Data Over Time')
plt.xlabel('Time')
plt.ylabel('Acceleration (g)')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 2)
plt.hist(data['AccelerationX'], bins=30, color='skyblue', alpha=0.7)
plt.title('Distribution of Acceleration in X Axis')
plt.xlabel('Acceleration (g)')
plt.ylabel('Frequency')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.scatter(data['Temperature'], data['AccelerationX'], alpha=0.7, color='purple')
plt.title('Temperature vs. Acceleration X')
plt.xlabel('Temperature (°C)')
plt.ylabel('Acceleration X (g)')
plt.grid(True)

plt.tight_layout()
plt.show(block=False)

sns.pairplot(data[['AccelerationX', 'AccelerationY', 'AccelerationZ', 'Temperature', 'Humidity']], diag_kind='kde')
plt.suptitle('Pair Plot of Sensor Data', y=1.02)
plt.show()
