# Network Monitor Tool

## Overview

The Network Monitor Tool is a Python-based utility designed to monitor devices on your WiFi network and capture network traffic. It provides basic functionality for discovering connected devices and capturing/analyzing network traffic. The tool also includes a GUI using Tkinter, a web interface using Flask, database storage using SQLite, and advanced traffic analysis features.

## Features

- Discover all devices connected to your network.
- Capture and analyze network traffic.
- Display relevant information about network packets.
- GUI using Tkinter.
- Web interface using Flask.
- Database storage using SQLite.
- Advanced traffic analysis.

## Prerequisites

- Python 3.x
- Pip (Python package installer)

## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine using the following command:

```sh
git clone https://github.com/yourusername/network-monitor-tool.git
cd network-monitor-tool
```
### Step 2: Install Dependencies

Install the required Python libraries using pip:

```sh


`pip install -r requirements.txt`
```
Usage
-----

### GUI

1.  Open a terminal and navigate to the directory where you cloned the repository.

2.  Run the GUI:

sh


`python gui.py`

### Web Interface

1.  Open a terminal and navigate to the directory where you cloned the repository.

2.  Run the web interface:

sh


`python web_interface.py`

1.  Open a web browser and go to `http://127.0.0.1:5000`.

### Command Line

1.  Open a terminal and navigate to the directory where you cloned the repository.

2.  Run the network monitoring tool:

sh


`python network_monitor.py`

1.  The tool will start by discovering devices on your network and then begin capturing network traffic.

Customization
-------------

### Subnet Adjustment

-   Modify the subnet in the `scapy.arping("192.168.1.0/24")` line according to your network configuration.

### Packet Processing

-   Customize the `process_packet` method to extract and display the specific information you need from the captured packets.

Contributing
------------

Feel free to submit issues and pull requests. Contributions are welcome!

License
-------

This project is licensed under the MIT License.

About Me
------------
- I'm Brian Ndegwa, a passionate IT professional with over 5 years of experience.
- I specialize in cybersecurity.
- My expertise spans system development, network administration, and penetration testing.
- I'm proficient in C, Python, Java, Django, and React.
- I developed RONA, a nationally recognized virtual assistant to combat misinformation during the pandemic.
- I value collaboration, teamwork, and continuous learning.
