# Internet of Things (IoT) Based Interoperability and Standardization in Healthcare

This project focuses on optimizing communication protocols for IoT devices in healthcare settings, specifically for improving gait analysis. The system integrates various IoT devices, data collection methodologies, and communication protocols (MQTT, AMQP, DDS) to enhance data handling efficiency. This document details the scope and requirements, development process, technology stack, code structure, and evaluation of the system, along with considerations for future enhancements.

## Scope and Requirements

### IoT Device Setup
- **Sensor Integration:** Arduino Uno with Ultrasonic, DHT22, and Accelerometer sensors for gait analysis.
- **Real-Time Data Collection:** Continuous data collection and transmission using different communication protocols.

### Protocol Implementation
- **MQTT Protocol:** Real-time data transfer using MQTT.
- **AMQP Protocol:** Message-oriented communication via AMQP.
- **DDS Protocol:** Data distribution using DDS for real-time services.

### Data Analysis and Visualization
- **Data Storage:** Structured storage of collected sensor data for analysis.
- **Visualization:** Python with Pandas and Matplotlib for data visualization.

## Development

### Technology Stack
- **Arduino:** Hardware for sensor data collection.
- **Python:** Core programming language for data handling and protocol implementation.
- **MQTT/AMQP/DDS:** Libraries for implementing communication protocols.
- **MATLAB:** Advanced data visualization and analysis.

### System Architecture
The system integrates IoT devices with communication protocols to monitor and analyze gait patterns. Sensor data is collected in real-time, transmitted using the selected protocol, and stored for analysis. The architecture allows modular testing of different protocols to determine the most efficient method for real-time data transfer.

![System Architecture Diagram] <img width="848" alt="Screenshot 2024-08-23 at 7 28 19 PM" src="https://github.com/user-attachments/assets/de1bfd5d-895a-45cc-b8d9-fcaf97b18ef0">


### Workflow

**Sensor Data Collection and Transmission:**
- Setup sensors on Arduino and initiate real-time data collection.
- Transmit data using MQTT, AMQP, and DDS protocols.
- Store transmitted data for further analysis.

**Protocol Testing:**
- Run Python scripts to evaluate each protocol's performance.
- Measure key metrics like latency, reliability, and scalability.

**Data Visualization and Analysis:**
- Use Python and MATLAB to visualize collected data.
- Analyze results to compare the efficiency of different protocols.

![Data Visualization Example]<img width="825" alt="Screenshot 2024-08-23 at 7 29 07 PM" src="https://github.com/user-attachments/assets/febf9060-a0ab-4c43-8e0c-f563526ef30c">


## Code Structure

- **/arduino_code/**: Arduino sketches for sensor data collection.
- **/scripts/**: Python scripts for protocol implementation and testing.
  - `mqtt_publisher.py`
  - `amqp_publisher.py`
  - `dds_publisher.py`
- **/data/**: Collected sensor data in CSV format.
- **/visualization/**: Scripts and notebooks for data analysis and visualization.

## Evaluation

### Performance and Functionality
- The system effectively monitored and analyzed gait in real-time.
- Protocol testing showed the strengths and weaknesses of MQTT, AMQP, and DDS in healthcare data handling.
- The system’s modular approach supports easy adaptation for different healthcare applications.

### Testing and Scientific Evidence
- Extensive testing in simulated environments validated the communication protocols.
- Data analysis confirmed the system's reliability and accuracy for real-time gait analysis.

### Future Iterations and Reflection
- Future work will refine data transmission protocols for better real-time performance.
- Additional sensors and data points will be integrated for more comprehensive gait analysis.
- The system architecture will be iteratively improved based on user feedback and testing outcomes.


