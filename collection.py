import serial
import csv
from datetime import datetime

# Open serial connection
def open_serial_connection():
    port = '/dev/tty.usbmodem142301'  
    baud_rate = 9600
    try:
        return serial.Serial(port, baud_rate, timeout=1)
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

def main():
    ser = open_serial_connection()
    if ser is None:
        print("Failed to open serial connection.")
        return

    file_path = '/Users/jayant/Documents/Trimester1-2024/SIT724/sensor_data.csv' 
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        print(f"File opened successfully at {file_path}")

        while True:
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f"Received line: {line}")  # Debugging output
                data = line.split(',')
                writer.writerow(data)
                file.flush()  # data is written to disk
                print("Data written to file.")  # Confirming data write

if __name__ == "__main__":
    main()
