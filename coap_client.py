import asyncio
import serial
import json
import time
from aiocoap import *

# Configure serial port (replace with your correct port)
serial_port = '/dev/cu.usbmodem141201'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)

async def main():
    protocol = await Context.create_client_context()

    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            sensor_data = {
                'timestamp': time.time(),
                'data': line
            }
            payload = json.dumps(sensor_data).encode('utf-8')
            request = Message(code=POST, payload=payload, uri='coap://localhost/sensor/data')
            response = await protocol.request(request).response
            print(f"Sent data: {sensor_data}, Response: {response.payload.decode('utf-8')}")
            await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
