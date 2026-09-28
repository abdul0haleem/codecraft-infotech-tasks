# Network Packet Analyzer using Python and Scapy

A Python-based **Network Packet Analyzer** developed using **Scapy** on Kali Linux. The project captures live network traffic and progressively analyzes packets by identifying protocols, IP addresses, port numbers, payload information, packet numbers, and timestamps.

## Table of Contents

- [📖 Project Overview](#-project-overview)
- [🎯 Project Objective](#-project-objective)
- [🛠️ Tools and Technologies](#️-tools-and-technologies)
- [⚙️ Project Implementation](#️-project-implementation)
  - [Step 1 — Create the Project Directory](#step-1--create-the-project-directory)
  - [Step 2 — Check Python Installation](#step-2--check-python-installation)
  - [Step 3 — Install and Verify Scapy](#step-3--install-and-verify-scapy)
  - [Step 4 — Create the Python Packet Analyzer File](#step-4--create-the-python-packet-analyzer-file)
  - [Step 5 — Write the Basic Packet Capture Program](#step-5--write-the-basic-packet-capture-program)
  - [Step 6 — Run and Test the Packet Analyzer](#step-6--run-and-test-the-packet-analyzer)
  - [Step 7 — Improve Packet Analysis](#step-7--improve-packet-analysis)
  - [Step 8 — Test TCP and UDP Packet Analysis](#step-8--test-tcp-and-udp-packet-analysis)
  - [Step 9 — Add Payload Data Analysis](#step-9--add-payload-data-analysis)
  - [Step 10 — Test Payload Data Analysis](#step-10--test-payload-data-analysis)
  - [Step 11 — Add Packet Numbering and Timestamp](#step-11--add-packet-numbering-and-timestamp)
  - [Step 12 — Test Packet Numbering and Timestamp](#step-12--test-packet-numbering-and-timestamp)
  - [Step 13 — Save Packet Information to a Log File](#step-13--save-packet-information-to-a-log-file)
  - [Step 14 — Test Packet Logging](#step-14--test-packet-logging)
  - [Step 15 — Display Human-Readable Protocol Names](#step-15--display-human-readable-protocol-names)
  - [Step 16 — Test Protocol Identification](#step-16--test-protocol-identification)
  - [Step 17 — Add an Interactive Menu](#step-17--add-an-interactive-menu)
- [✅ Conclusion](#-conclusion)

## 📖 Project Overview

The **Network Packet Analyzer** is a Python-based network traffic analysis tool developed using **Scapy** on **Kali Linux**. The project captures live network packets and extracts useful information such as source and destination IP addresses, protocol names, TCP/UDP port numbers, payload information, packet numbers, and timestamps.

The analyzer also includes **packet logging** functionality, allowing captured information to be saved to `packet_log.txt` for later analysis. An interactive command-line menu provides options to start packet capture or exit the application.

The project was developed and tested in a controlled virtualized lab environment using **Kali Linux running in VirtualBox**.

## 🎯 Project Objective

The main objectives of this project are to:

* Develop a basic network packet analyzer using Python and Scapy.
* Capture and analyze live network traffic.
* Identify source and destination IP addresses.
* Identify common protocols such as **TCP, UDP, and ICMP**.
* Display TCP and UDP source and destination ports.
* Analyze basic packet payload information.
* Record packet numbers and timestamps.
* Save captured packet information to a log file.
* Provide an interactive command-line interface for controlling packet capture.
* Gain practical experience with network traffic analysis and cybersecurity monitoring concepts.

## 🛠️ Tools and Technologies

| Category             | Tools / Technologies              |
| -------------------- | --------------------------------- |
| Operating System     | Kali Linux                        |
| Virtualization       | Oracle VirtualBox                 |
| Programming Language | Python 3                          |
| Packet Analysis      | Scapy                             |
| Network Protocols    | TCP, UDP, ICMP, DNS               |
| Network Testing      | `ping`, `curl`, `nslookup`        |
| Text Editor          | Nano                              |
| Logging              | Python File I/O, `packet_log.txt` |
| Version Control      | Git / GitHub                      |

## ⚙️ Project Implementation

## Step 1 — Create the Project Directory

#### Objective

Create a dedicated project directory for the **Network Packet Analyzer** and navigate into it. This directory will contain the Python program and other project files.

#### 1. Open Kali Linux

Start the **Kali Linux** virtual machine in VirtualBox and log in to the system.

![Kali Linux running in VirtualBox](images/01-kali-linux-virtualbox.png)

*Screenshot 1: Kali Linux running in VirtualBox.*

#### 2. Create the Project Directory

Open the Kali Linux terminal and create the project directory:

```bash
mkdir -p ~/Mini_Projects/Network_Packet_Analyzer
```

#### 3. Navigate into the Project Directory

Navigate into the newly created project directory:

```bash
cd ~/Mini_Projects/Network_Packet_Analyzer
```

![Project directory creation and navigation](images/02-project-directory-creation-navigation.png)


*Screenshot 2: Terminal showing the project directory creation and navigation.*

#### 4. Verify the Current Directory

Run the following command to verify the current working directory:

```bash
pwd
```

The terminal should display:

```text
/home/kali/Mini_Projects/Network_Packet_Analyzer
```

![Current project directory](images/03-project-directory-pwd.png)

*Screenshot 3: Terminal showing the current project directory using the `pwd` command.*

---

## Step 2 — Check Python Installation

#### Objective

Verify that Python 3 is installed and working correctly on Kali Linux before developing the **Network Packet Analyzer**. Python will be used to create the packet capture and analysis program.

#### 1. Check the Python 3 Version

From inside the project directory, run:

```bash
python3 --version
```

The terminal should display the installed Python 3 version. For example:

```text
Python 3.13.7
```

The exact version may be different depending on the Kali Linux installation.

![Python 3 version](images/04-python-version.png)

*Screenshot 4: Terminal showing the installed Python 3 version.*

#### 2. Verify the Python Executable

Run the following command to verify the location of the Python 3 executable:

```bash
which python3
```

The terminal should display a path similar to:

```text
/usr/bin/python3
```

![Python executable location](images/05-python-executable-location.png)

*Screenshot 5: Terminal showing the location of the Python 3 executable.*

## Step 3 — Install and Verify Scapy

#### Objective

Install the **Scapy** Python library, which will be used to capture and analyze network packets. Scapy provides functions for working with network protocols and extracting information such as IP addresses, protocols, ports, and packet data.

#### 1. Check if Scapy Is Already Installed

From inside the project directory, run:

```bash
python3 -c "import scapy; print('Scapy is installed')"
```

If Scapy is already installed, the terminal should display:

```text
Scapy is installed
```

![Scapy already installed](images/06-scapy-already-installed.png)

*Screenshot 6: Terminal showing that Scapy is already installed.*

#### 2. Install Scapy if It Is Not Installed

If the previous command shows an error such as `ModuleNotFoundError`, install Scapy using:

```bash
sudo apt update
```

Then:

```bash
sudo apt install python3-scapy -y
```

Enter your Kali Linux password when prompted.

#### 3. Verify the Scapy Installation

After installation, run:

```bash
python3 -c "from scapy.all import sniff; print('Scapy is ready for packet capture')"
```

The terminal should display:

```text
Scapy is ready for packet capture
```

![Scapy installation verification](images/07-scapy-installation-verification.png)

*Screenshot 7: Terminal showing successful Scapy installation and verification.*

---

## Step 4 — Create the Python Packet Analyzer File

#### Objective

Create the main Python file for the **Network Packet Analyzer**. This file will contain the code used to capture network packets and display basic packet information.

#### 1. Create the Python File

Make sure you are inside the project directory:

```bash
cd ~/Mini_Projects/Network_Packet_Analyzer
```

Create the Python file:

```bash
touch packet_analyzer.py
```

#### 2. Verify the File

Run:

```bash
ls -l
```

The terminal should display the newly created file:

```text
packet_analyzer.py
```

![Packet analyzer file](images/08-packet-analyzer-file-created.png)

*Screenshot 8: Terminal showing the `packet_analyzer.py` file inside the project directory.*

#### 3. Open the Python File

Open the file using the Nano text editor:

```bash
nano packet_analyzer.py
```

The file will initially be empty.

![Packet analyzer Nano editor](images/09-packet-analyzer-nano-editor.png)

*Screenshot 9: Nano editor showing the newly created `packet_analyzer.py` file.*

---

## Step 5 — Write the Basic Packet Capture Program

#### Objective

Add the basic Python code required to capture network packets using **Scapy**. The program will display the source IP address, destination IP address, and protocol information for each captured packet.

#### 1. Open the Python File

Run:

```bash
nano packet_analyzer.py
```

#### 2. Add the Following Code

Enter the following code:

```python
from scapy.all import sniff, IP


def analyze_packet(packet):

    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n--- Packet Captured ---")
        print(f"Source IP      : {source_ip}")
        print(f"Destination IP : {destination_ip}")
        print(f"Protocol       : {protocol}")


print("Starting Network Packet Analyzer...")
print("Capturing packets. Press Ctrl+C to stop.")

sniff(prn=analyze_packet, store=False)
```

#### 3. Save the Python File

In Nano:

1. Press **Ctrl + O** to save the file.
2. Press **Enter** to confirm the filename.
3. Press **Ctrl + X** to exit Nano.

![Basic packet capture code](images/10-basic-packet-capture-code.png)

*Screenshot 10: Nano editor showing the completed basic packet capture code.*

#### What This Code Does

The program imports Scapy's `sniff()` function to capture packets.

The `analyze_packet()` function checks whether a captured packet contains an **IP layer**. If it does, the program extracts:

* **Source IP address**
* **Destination IP address**
* **IP protocol number**

The `sniff()` function continuously captures packets and sends each packet to `analyze_packet()` for analysis.

> **Important:** Only capture traffic on networks/interfaces you own or have explicit permission to monitor. For this project, use your own Kali VM/network traffic.

---

## Step 6 — Run and Test the Packet Analyzer

#### Objective

Run the **Network Packet Analyzer** and verify that it can successfully capture and display network packets. The program will show the source IP address, destination IP address, and protocol number for captured IP packets.

#### 1. Run the Packet Analyzer

From the project directory, run:

```bash
sudo python3 packet_analyzer.py
```

You should see:

```text
Starting Network Packet Analyzer...
Capturing packets. Press Ctrl+C to stop.
```

![Packet analyzer running](images/11-packet-analyzer-running-basic.png)

*Screenshot 11: Terminal showing the Network Packet Analyzer starting successfully and waiting for network packets.*

#### 2. Generate Some Network Traffic

While the analyzer is running, open another terminal and run:

```bash
ping -c 4 8.8.8.8
```

This generates ICMP network traffic that the packet analyzer can capture.

![Ping command](images/12-ping-command.png)

*Screenshot 12: Terminal showing the `ping` command.*

You should see packet information similar to:

```text
--- Packet Captured ---

Source IP      : 192.168.43.18
Destination IP : 8.8.8.8
Protocol       : 1
```

The actual IP addresses will depend on your network configuration.

![Captured packets](images/13-basic-packets-captured.png)

*Screenshot 13: Packet Analyzer terminal showing captured packets with source IP, destination IP, and protocol information.*

#### 3. Stop the Packet Analyzer

Return to the terminal running the analyzer and press:

```text
Ctrl + C
```

The packet capture will stop and return to the terminal prompt.

![Packet analyzer stopped](images/14-packet-analyzer-stopped.png)

*Screenshot 14: Terminal showing the packet analyzer stopped using Ctrl+C.*

## Step 7 — Improve Packet Analysis

#### Objective

Modify the packet analyzer to display more useful network information, including the **source IP address, destination IP address, protocol, source port, and destination port**.

#### 1. Open the Python File

Run:

```bash
nano packet_analyzer.py
```

#### 2. Replace the Existing Code

Replace the previous code with:

```python
from scapy.all import sniff, IP, TCP, UDP


def analyze_packet(packet):

    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n--- Packet Captured ---")
        print(f"Source IP      : {source_ip}")
        print(f"Destination IP : {destination_ip}")
        print(f"Protocol       : {protocol}")

        if TCP in packet:
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")


print("Starting Network Packet Analyzer...")
print("Capturing packets. Press Ctrl+C to stop.")

sniff(prn=analyze_packet, store=False)
```

#### 3. Save the File

In Nano:

1. Press **Ctrl + O**
2. Press **Enter**
3. Press **Ctrl + X**

![TCP and UDP packet analysis code](images/15-tcp-udp-analysis-code.png)

*Screenshot 15: Nano editor showing the updated packet analyzer code with TCP and UDP packet analysis.*

#### What Was Added

The program now identifies:

* **TCP packets** and displays their source and destination ports.
* **UDP packets** and displays their source and destination ports.
* **IP information** for captured packets.

This makes the analyzer more useful for basic network traffic investigation.

---

## Step 8 — Test TCP and UDP Packet Analysis

#### Objective

Test the updated **Network Packet Analyzer** by generating **TCP and UDP network traffic** and verify that the program displays the corresponding source and destination ports.

#### 1. Start the Packet Analyzer

Open the project directory:

```bash
cd ~/Mini_Projects/Network_Packet_Analyzer
```

Run the analyzer:

```bash
sudo python3 packet_analyzer.py
```

The terminal should display:

```text
Starting Network Packet Analyzer...
Capturing packets. Press Ctrl+C to stop.
```

![Packet analyzer running](images/16-packet-analyzer-running-tcp-udp.png)

*Screenshot 16: Terminal showing the Network Packet Analyzer running and waiting for packets.*

#### 2. Generate TCP Traffic

Open a **second terminal** and run:

```bash
curl https://example.com
```

This generates TCP traffic to the web server.

![Curl command](images/17-curl-command.png)

*Screenshot 17: Terminal showing the `curl` command.*

Return to the packet analyzer terminal. You should see information similar to:

```text
--- Packet Captured ---

Source IP      : 192.168.x.x
Destination IP : xxx.xxx.xxx.xxx
Protocol       : 6
Source Port    : 54321
Destination Port: 443
```

![Captured TCP packet](images/18-captured-tcp-packet.png)

*Screenshot 18: Packet analyzer displaying a captured TCP packet with source and destination ports.*

#### 3. Generate UDP Traffic

In the second terminal, run:

```bash
nslookup example.com
```

This normally generates DNS traffic using UDP.

![Nslookup command](images/19-nslookup-command.png)

*Screenshot 19: Terminal showing the `nslookup` command.*

The analyzer may display something similar to:

```text
--- Packet Captured ---

Source IP      : 192.168.x.x
Destination IP : xxx.xxx.xxx.xxx
Protocol       : 17
Source Port    : 54321
Destination Port: 53
```

![Captured UDP DNS packet](images/20-captured-udp-dns-packet.png)

*Screenshot 20: Packet analyzer displaying a captured UDP/DNS packet with source and destination ports.*

#### 4. Stop the Analyzer

Return to the packet analyzer terminal and press:

```text
Ctrl + C
```

#### Protocol Numbers

For reference:

| Protocol | IP Protocol Number |
| -------- | -----------------: |
| ICMP     |                  1 |
| TCP      |                  6 |
| UDP      |                 17 |

The exact IP addresses and source ports will vary depending on your network connection and generated traffic.

---

## Step 9 — Add Payload Data Analysis

#### Objective

Enhance the **Network Packet Analyzer** to display basic **payload data** from captured packets. This allows the analyzer to provide additional information about the contents carried by network packets.

> **Note:** Payload data can contain sensitive information. Only inspect traffic on systems and networks where you have authorization.

#### 1. Open the Python File

Run:

```bash
nano ~/Mini_Projects/Network_Packet_Analyzer/packet_analyzer.py
```

#### 2. Replace the Existing Code

Replace the existing code with:

```python
from scapy.all import sniff, IP, TCP, UDP, Raw


def analyze_packet(packet):

    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n--- Packet Captured ---")
        print(f"Source IP       : {source_ip}")
        print(f"Destination IP  : {destination_ip}")
        print(f"Protocol        : {protocol}")

        if TCP in packet:
            print(f"Source Port     : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print(f"Source Port     : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        if Raw in packet:
            payload = bytes(packet[Raw].load)
            print(f"Payload Length  : {len(payload)} bytes")
            print(f"Payload Data    : {payload[:100]!r}")

        else:
            print("Payload Data    : No payload")


print("Starting Network Packet Analyzer...")
print("Capturing packets. Press Ctrl+C to stop.")

sniff(prn=analyze_packet, store=False)
```

#### 3. Save the File

In Nano:

1. Press **Ctrl + O**
2. Press **Enter**
3. Press **Ctrl + X**

*Screenshot 21: Nano editor showing the updated packet analyzer code with payload analysis.*

#### What Was Added

The program now checks whether a captured packet contains a **Raw** layer.

If payload data is present, it displays:

* **Payload length**
* The first **100 bytes** of the payload

If no payload is present, it displays:

```text
Payload Data    : No payload
```

Limiting the output to the first 100 bytes keeps the terminal readable and prevents large packet contents from flooding the screen.

---

## Step 10 — Test Payload Data Analysis

#### Objective

Run the updated **Network Packet Analyzer** and verify that it can identify whether captured packets contain payload data and display the payload length and a limited portion of the payload.

#### 1. Start the Packet Analyzer

Open the project directory:

```bash
cd ~/Mini_Projects/Network_Packet_Analyzer
```

Run the program:

```bash
sudo python3 packet_analyzer.py
```

You should see:

```text
Starting Network Packet Analyzer...
Capturing packets. Press Ctrl+C to stop.
```

![Packet analyzer running with payload analysis](images/22-packet-analyzer-running-payload.png)

*Screenshot 22: Terminal showing the Network Packet Analyzer running with payload analysis enabled.*

#### 2. Generate Network Traffic

Open a second terminal and run:

```bash
curl https://example.com
```

This generates network traffic that the analyzer can inspect.

Return to the analyzer terminal.

You may see output similar to:

```text
Payload Data    : No payload
```

The actual IP addresses, ports, payload length, and payload contents will vary.

![No Raw payload detected](images/23-no-raw-payload-detected.png)

*Screenshot 23: Terminal showing packet analysis where no Raw payload is detected.*

#### 3. Test a Packet Without Payload

Generate another type of traffic, such as:

```bash
ping -c 4 8.8.8.8
```

The analyzer should capture ICMP packets. Depending on the packet structure, you may see:

```text
--- Packet Captured ---

Source IP       : 192.168.x.x
Destination IP  : xxx.xxx.xxx.xxx
Protocol        : 6
Source Port     : 54321
Destination Port: 443
Payload Length  : 100 bytes
Payload Data    : b'...'
```

![Captured packet with payload](images/24-payload-length-data.png)

*Screenshot 24: Terminal showing a captured packet with payload length and payload data.*

#### 4. Stop the Analyzer

Press:

```text
Ctrl + C
```

#### Result

At this stage, the analyzer can display:

* **Source IP address**
* **Destination IP address**
* **Protocol number**
* **Source port**
* **Destination port**
* **Payload length**
* **Limited payload data**

Next, packet numbering and timestamp information can be added to make the analyzer output more useful for security monitoring.

---

## Step 11 — Add Packet Numbering and Timestamp

#### Objective

Improve the **Network Packet Analyzer** by assigning a **packet number** and recording the **timestamp** for each captured packet. This makes the output easier to read and useful for basic network traffic analysis.

#### 1. Open the Python File

Run:

```bash
nano ~/Mini_Projects/Network_Packet_Analyzer/packet_analyzer.py
```

#### 2. Replace the Existing Code

Replace the existing code with:

```python
from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime


packet_count = 0


def analyze_packet(packet):

    global packet_count
    packet_count += 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n--- Packet Captured ---")
        print(f"Packet Number   : {packet_count}")
        print(f"Timestamp       : {timestamp}")
        print(f"Source IP       : {source_ip}")
        print(f"Destination IP  : {destination_ip}")
        print(f"Protocol        : {protocol}")

        if TCP in packet:
            print(f"Source Port     : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print(f"Source Port     : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        if Raw in packet:
            payload = bytes(packet[Raw].load)
            print(f"Payload Length  : {len(payload)} bytes")
            print(f"Payload Data    : {payload[:100]!r}")

        else:
            print("Payload Data    : No payload")


print("Starting Network Packet Analyzer...")
print("Capturing packets. Press Ctrl+C to stop.")

sniff(prn=analyze_packet, store=False)
```

#### 3. Save the File

In Nano:

1. Press **Ctrl + O**
2. Press **Enter**
3. Press **Ctrl + X**

![Packet numbering and timestamp code](images/25-packet-number-timestamp-code.png)

*Screenshot 25: Nano editor showing the updated packet analyzer code with packet numbering and timestamp functionality.*

#### What Was Added

The program now records:

* **Packet Number** — identifies each captured packet sequentially.
* **Timestamp** — records when the packet was processed.
* **Source IP**
* **Destination IP**
* **Protocol**
* **Source and destination ports**
* **Payload information**

For example:

```text
--- Packet Captured ---

Packet Number   : 1
Timestamp       : 2026-09-26 10:45:21
Source IP       : 192.168.1.10
Destination IP  : 8.8.8.8
Protocol        : 1
Payload Length  : 32 bytes
```

The packet number starts at **1** each time the program is started and increases for every IP packet processed.

---

## Step 12 — Test Packet Numbering and Timestamp

#### Objective

Run the updated **Network Packet Analyzer** and verify that each captured packet displays a **packet number** and **timestamp** along with the previously implemented network information.

#### 1. Start the Packet Analyzer

Open the project directory:

```bash
cd ~/Mini_Projects/Network_Packet_Analyzer
```

Run:

```bash
sudo python3 packet_analyzer.py
```

The terminal should display:

```text
Starting Network Packet Analyzer...
Capturing packets. Press Ctrl+C to stop.
```

![Packet analyzer running](images/26-packet-analyzer-running-final.png)

*Screenshot 26: Terminal showing the Network Packet Analyzer running.*

#### 2. Generate Network Traffic

Open a second terminal and run:

```bash
ping -c 4 8.8.8.8
```

The analyzer should capture the ICMP packets.

You should see output similar to:

```text
--- Packet Captured ---

Packet Number   : 1
Timestamp       : 2026-09-26 10:50:21
Source IP       : 192.168.x.x
Destination IP  : 8.8.8.8
Protocol        : 1
Payload Length  : 32 bytes
Payload Data    : b'...'
```

Additional packets should have increasing packet numbers:

```text
Packet Number   : 2
Packet Number   : 3
Packet Number   : 4
```

![Captured packets with numbering and timestamps](images/27-final-packets-number-timestamp.png)

*Screenshot 27: Terminal showing captured packets with packet numbers and timestamps.*

#### 3. Generate Additional Traffic

In the second terminal, run:

```bash
curl https://example.com
```

This allows the analyzer to capture additional TCP traffic.

![Additional TCP traffic](images/28-additional-tcp-traffic.png)

*Screenshot 28: Terminal showing additional captured TCP traffic with packet numbers, timestamps, IP addresses, and port information.*

#### 4. Stop the Analyzer

Return to the analyzer terminal and press:

```text
Ctrl + C
```

#### Expected Result

The analyzer should now provide a structured view of captured packets containing:

* **Packet Number**
* **Timestamp**
* **Source IP**
* **Destination IP**
* **Protocol**
* **Source Port**
* **Destination Port**
* **Payload Length**
* **Payload Data**

### Step 13 — Save Packet Information to a Log File

#### Objective

Modify the **Network Packet Analyzer** so that captured packet information is not only displayed in the terminal but also **saved to a log file**. This allows the captured information to be reviewed later for analysis and troubleshooting.

#### 1. Open the Python File

Run the following command:

```bash
nano ~/Mini_Projects/Network_Packet_Analyzer/packet_analyzer.py
```

#### 2. Replace the Existing Code

Replace the previous code with the updated version that includes packet logging functionality.

```python
from scapy.all import sniff, IP, TCP, UDP, Raw
from datetime import datetime

packet_count = 0
log_file = "packet_log.txt"

def write_to_log(message):
    with open(log_file, "a") as file:
        file.write(message + "\n")

def analyze_packet(packet):
    global packet_count
    packet_count += 1
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        packet_info = []

        packet_info.append("\n--- Packet Captured ---")
        packet_info.append(f"Packet Number   : {packet_count}")
        packet_info.append(f"Timestamp       : {timestamp}")
        packet_info.append(f"Source IP       : {source_ip}")
        packet_info.append(f"Destination IP  : {destination_ip}")
        packet_info.append(f"Protocol        : {protocol}")

        if TCP in packet:
            packet_info.append(f"Source Port     : {packet[TCP].sport}")
            packet_info.append(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            packet_info.append(f"Source Port     : {packet[UDP].sport}")
            packet_info.append(f"Destination Port: {packet[UDP].dport}")

        if Raw in packet:
            payload = bytes(packet[Raw].load)
            packet_info.append(f"Payload Length  : {len(payload)} bytes")
            packet_info.append(f"Payload Data    : {payload[:100]!r}")

        else:
            packet_info.append("Payload Data    : No payload")

        output = "\n".join(packet_info)

        print(output)
        write_to_log(output)

print("Starting Network Packet Analyzer...")
print("Capturing packets. Press Ctrl+C to stop.")
print(f"Packet information will be saved to: {log_file}")

sniff(prn=analyze_packet, store=False)
```

#### 3. Save the File

In Nano:

1. Press **Ctrl + O** to save the file.
2. Press **Enter** to confirm the filename.
3. Press **Ctrl + X** to exit Nano.

![Packet logging code](images/29-packet-logging-code.png)

*Screenshot 29: Nano editor showing the updated packet analyzer code with packet logging functionality.*

#### What Was Added

The program now creates a log file named `packet_log.txt` and stores captured packet information in it. Every captured IP packet is displayed in the terminal and simultaneously appended to the log file, including the packet number, timestamp, IP addresses, protocol, port information, and payload details. The log file is automatically created inside the project directory, and any new packet information is appended instead of overwriting existing entries.

---

### Step 14 — Test Packet Logging

#### Objective

Run the updated **Network Packet Analyzer**, generate network traffic, and verify that captured packet information is saved successfully to the `packet_log.txt` file.

#### 1. Start the Packet Analyzer

Navigate to the project directory:

```bash
cd ~/Mini_Projects/Network_Packet_Analyzer
```

Run the analyzer:

```bash
sudo python3 packet_analyzer.py
```

The terminal should display:

```text
Starting Network Packet Analyzer...
Capturing packets. Press Ctrl+C to stop.
Packet information will be saved to: packet_log.txt
```

#### 2. Generate Network Traffic

Open a second terminal and generate ICMP traffic:

```bash
ping -c 4 8.8.8.8
```

The analyzer captures the packets and displays their information in the terminal.

#### 3. Stop the Analyzer

Return to the analyzer terminal and press:

```text
Ctrl + C
```

#### 4. Verify the Log File

Check that the log file has been created:

```bash
ls -l packet_log.txt
```

![Packet log file created](images/30-packet-log-file-created.png)

*Screenshot 30: Terminal showing the `packet_log.txt` file created in the project directory.*

#### 5. View the Saved Packet Information

Display the contents of the log file:

```bash
cat packet_log.txt
```

Example output:

```text
--- Packet Captured ---

Packet Number   : 1
Timestamp       : 2026-09-28 20:05:21
Source IP       : 192.168.x.x
Destination IP  : 8.8.8.8
Protocol        : 1
Payload Length  : 32 bytes
Payload Data    : b'...'
```

![Packet log output](images/31-packet-log-file-output.png)

*Screenshot 31: Terminal displaying the saved packet information from `packet_log.txt`.*

#### 6. Verify the Project Files

List the files in the project directory:

```bash
ls -la
```

The project directory should now contain at least:

* `packet_analyzer.py`
* `packet_log.txt`

![Completed project files](images/32-completed-project-files.png)

*Screenshot 32: Terminal showing the completed project files, including the Python program and packet log.*

#### Result

The **Network Packet Analyzer** now captures network packets, displays packet information in real time, records packet numbers and timestamps, analyzes TCP/UDP ports and payload data, and automatically saves the captured information to `packet_log.txt` for later review.

### Step 15 — Display Human-Readable Protocol Names

#### Objective

Improve the **Network Packet Analyzer** by displaying **protocol names** such as **TCP, UDP, and ICMP** instead of only their numerical protocol values. This makes the captured packet information easier to understand.

#### 1. Open the Python File

Run:

```bash
nano ~/Mini_Projects/Network_Packet_Analyzer/packet_analyzer.py
```

#### 2. Replace the Existing Code

Replace the existing code with the updated version that identifies protocols by name.

```python
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

packet_count = 0
log_file = "packet_log.txt"

def write_to_log(message):
    with open(log_file, "a") as file:
        file.write(message + "\n")

def get_protocol_name(packet):
    if TCP in packet:
        return "TCP"
    elif UDP in packet:
        return "UDP"
    elif ICMP in packet:
        return "ICMP"
    else:
        return "Other"

def analyze_packet(packet):
    global packet_count

    if IP in packet:
        packet_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol_name = get_protocol_name(packet)

        packet_info = []

        packet_info.append("\n--- Packet Captured ---")
        packet_info.append(f"Packet Number   : {packet_count}")
        packet_info.append(f"Timestamp       : {timestamp}")
        packet_info.append(f"Source IP       : {source_ip}")
        packet_info.append(f"Destination IP  : {destination_ip}")
        packet_info.append(f"Protocol        : {protocol_name}")

        if TCP in packet:
            packet_info.append(f"Source Port     : {packet[TCP].sport}")
            packet_info.append(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            packet_info.append(f"Source Port     : {packet[UDP].sport}")
            packet_info.append(f"Destination Port: {packet[UDP].dport}")

        if Raw in packet:
            payload = bytes(packet[Raw].load)
            packet_info.append(f"Payload Length  : {len(payload)} bytes")
            packet_info.append(f"Payload Data    : {payload[:100]!r}")

        else:
            packet_info.append("Payload Data    : No payload")

        output = "\n".join(packet_info)

        print(output)
        write_to_log(output)

print("Starting Network Packet Analyzer...")
print("Capturing packets. Press Ctrl+C to stop.")
print(f"Packet information will be saved to: {log_file}")

sniff(prn=analyze_packet, store=False)
```

#### 3. Save the File

In Nano:

1. Press **Ctrl + O** to save the file.
2. Press **Enter** to confirm the filename.
3. Press **Ctrl + X** to exit Nano.

![Human-readable protocol identification code](images/33-human-readable-protocol-code.png)

*Screenshot 33: Nano editor showing the updated packet analyzer code with human-readable protocol identification.*

#### What Was Added

A new `get_protocol_name()` function identifies common protocols and returns their names instead of numerical protocol values.

* **TCP** → TCP
* **UDP** → UDP
* **ICMP** → ICMP
* **Other** → Other

The analyzer now displays protocol names such as **ICMP**, **TCP**, and **UDP**, and the same information is also saved to `packet_log.txt`.

---

### Step 16 — Test Protocol Identification

#### Objective

Run the updated **Network Packet Analyzer** and verify that it correctly identifies common network protocols as **TCP, UDP, and ICMP** instead of displaying only numerical protocol values.

#### 1. Start the Packet Analyzer

Navigate to the project directory:

```bash
cd ~/Mini_Projects/Network_Packet_Analyzer
```

Run the analyzer:

```bash
sudo python3 packet_analyzer.py
```

The terminal should display:

```text
Starting Network Packet Analyzer...
Capturing packets. Press Ctrl+C to stop.
Packet information will be saved to: packet_log.txt
```

![Protocol identification enabled](images/34-packet-analyzer-running-protocol-identification.png)

*Screenshot 34: Terminal showing the Network Packet Analyzer running with protocol identification enabled.*

#### 2. Test ICMP Traffic

Open a second terminal and generate ICMP traffic:

```bash
ping -c 4 8.8.8.8
```

The analyzer should identify the packets as:

```text
--- Packet Captured ---

Packet Number   : 1
Timestamp       : 2026-09-28 20:15:21
Source IP       : 192.168.x.x
Destination IP  : 8.8.8.8
Protocol        : ICMP
```

The exact IP address and timestamp will depend on your network configuration.

![Captured ICMP packets](images/35-captured-icmp-protocol.png)

*Screenshot 35: Terminal showing captured ICMP packets identified by the analyzer.*

#### 3. Test TCP Traffic

In the second terminal, run:

```bash
curl https://example.com
```

The analyzer should identify TCP packets as:

```text
Protocol        : TCP
Source Port     : XXXXX
Destination Port: 443
```

![Captured TCP traffic](images/36-captured-tcp-protocol.png)

*Screenshot 36: Terminal showing captured TCP traffic with the protocol identified as TCP.*

#### 4. Test UDP Traffic

Generate DNS traffic by running:

```bash
nslookup example.com
```

The analyzer should identify UDP packets as:

```text
Protocol        : UDP
Source Port     : XXXXX
Destination Port: 53
```

![Captured UDP DNS traffic](images/37-captured-udp-dns-protocol.png)

*Screenshot 37: Terminal showing captured UDP/DNS traffic with the protocol identified as UDP.*

#### 5. Stop the Analyzer

Return to the analyzer terminal and press:

```text
Ctrl + C
```

#### 6. Verify the Log File

Display the saved packet log:

```bash
cat packet_log.txt
```

The log should now contain protocol names such as:

```text
Protocol        : ICMP
Protocol        : TCP
Protocol        : UDP
```

![Packet log with protocol names](images/38-packet-log-human-readable-protocols.png)

*Screenshot 38: Terminal displaying the saved packet log with human-readable protocol names.*

#### Result

The **Network Packet Analyzer** now provides more readable packet information by identifying common protocols directly as **ICMP, TCP, and UDP** instead of numerical protocol values.

---

### Step 17 — Add an Interactive Menu

#### Objective

Add a simple **command-line interactive menu** to the **Network Packet Analyzer**. The menu allows the user to start packet capture or exit the program instead of automatically starting the packet sniffer when the script is executed.

#### 1. Open the Python File

Run:

```bash
nano ~/Mini_Projects/Network_Packet_Analyzer/packet_analyzer.py
```

#### 2. Replace the Existing Code

Replace the existing code with the final version that includes an interactive menu.

```python
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

packet_count = 0
log_file = "packet_log.txt"

def write_to_log(message):
    with open(log_file, "a") as file:
        file.write(message + "\n")

def get_protocol_name(packet):
    if TCP in packet:
        return "TCP"
    elif UDP in packet:
        return "UDP"
    elif ICMP in packet:
        return "ICMP"
    else:
        return "Other"

def analyze_packet(packet):
    global packet_count

    if IP in packet:
        packet_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol_name = get_protocol_name(packet)

        packet_info = []

        packet_info.append("\n--- Packet Captured ---")
        packet_info.append(f"Packet Number   : {packet_count}")
        packet_info.append(f"Timestamp       : {timestamp}")
        packet_info.append(f"Source IP       : {source_ip}")
        packet_info.append(f"Destination IP  : {destination_ip}")
        packet_info.append(f"Protocol        : {protocol_name}")

        if TCP in packet:
            packet_info.append(f"Source Port     : {packet[TCP].sport}")
            packet_info.append(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            packet_info.append(f"Source Port     : {packet[UDP].sport}")
            packet_info.append(f"Destination Port: {packet[UDP].dport}")

        if Raw in packet:
            payload = bytes(packet[Raw].load)
            packet_info.append(f"Payload Length  : {len(payload)} bytes")
            packet_info.append(f"Payload Data    : {payload[:100]!r}")

        else:
            packet_info.append("Payload Data    : No payload")

        output = "\n".join(packet_info)

        print(output)
        write_to_log(output)

def start_capture():
    print("\nStarting Network Packet Analyzer...")
    print("Capturing packets. Press Ctrl+C to stop.\n")

    try:
        sniff(prn=analyze_packet, store=False)
    except KeyboardInterrupt:
        print("\nPacket capture stopped.")

def main():
    while True:
        print("\n===== Network Packet Analyzer =====")
        print("1. Start Packet Capture")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_capture()

        elif choice == "2":
            print("Exiting Network Packet Analyzer...")
            break

        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
```

#### 3. Save the File

In Nano:

1. Press **Ctrl + O** to save the file.
2. Press **Enter** to confirm the filename.
3. Press **Ctrl + X** to exit Nano.

![Interactive menu code](images/39-interactive-menu-code.png)

*Screenshot 39: Nano editor showing the completed Network Packet Analyzer code with the interactive menu.*

#### What Was Added

The `main()` function provides a simple interactive command-line interface:

```text
===== Network Packet Analyzer =====

1. Start Packet Capture
2. Exit
```

* Selecting **1** starts packet capture.
* Selecting **2** exits the program.
* If an invalid option is entered, the program prompts the user to select a valid menu option.
* Pressing **Ctrl + C** during packet capture safely stops the capture and returns control to the program.

#### Interactive Menu Preview

![Interactive menu](images/40-network-packet-analyzer-interactive-menu.png)

*Screenshot 40: Terminal showing the interactive menu of the completed Network Packet Analyzer.*

## ✅ Conclusion

The **Network Packet Analyzer** project demonstrates the development of a practical network traffic analysis tool using **Python and Scapy** on Kali Linux. The analyzer can capture live network packets, identify source and destination IP addresses, recognize TCP, UDP, and ICMP protocols, display TCP/UDP port information, analyze basic payload data, and record packet numbers and timestamps.

The project was further enhanced with **packet logging**, allowing captured information to be stored in `packet_log.txt` for later review. A **human-readable protocol identification** feature was added to make the captured data easier to understand, followed by an **interactive command-line menu** that allows users to start packet capture or exit the application.

Overall, this project provided hands-on experience with **Python programming, Scapy, packet capture, network protocols, traffic analysis, logging, and basic cybersecurity monitoring concepts**. It also demonstrates how network traffic can be programmatically captured and analyzed in a controlled lab environment.


