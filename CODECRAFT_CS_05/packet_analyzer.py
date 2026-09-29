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
