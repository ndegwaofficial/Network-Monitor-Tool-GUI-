"""
Network Monitor Tool

Author: Brian Ndegwa

Overview:
The Network Monitor Tool is a Python-based utility designed to monitor devices on your WiFi network and capture network traffic. It provides basic functionality for discovering connected devices and capturing/analyzing network traffic.

Features:
- Discover all devices connected to your network.
- Capture and analyze network traffic.
- Display relevant information about network packets.

License: MIT License
"""

import scapy.all as scapy
import psutil
import sqlite3
import threading

class NetworkMonitor:
    def __init__(self):
        self.devices = []
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect('network_data.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS packets
                     (time TEXT, src TEXT, dst TEXT, protocol TEXT, length INT)''')
        conn.commit()
        conn.close()

    def store_packet(self, packet):
        conn = sqlite3.connect('network_data.db')
        c = conn.cursor()
        c.execute("INSERT INTO packets VALUES (?, ?, ?, ?, ?)", 
                  (packet.time, packet.src, packet.dst, packet.proto, len(packet)))
        conn.commit()
        conn.close()

    def get_interfaces(self):
        interfaces = psutil.net_if_addrs()
        return [i for i in interfaces if i != 'lo']

    def discover_devices(self):
        interfaces = self.get_interfaces()
        for interface in interfaces:
            print(f"Scanning on interface: {interface}")
            scapy.arping("192.168.1.0/24")  # Adjust the subnet as necessary

    def capture_traffic(self, interface):
        scapy.sniff(iface=interface, prn=self.process_packet, store=False)

    def process_packet(self, packet):
        if packet.haslayer(scapy.IP):
            ip_layer = packet.getlayer(scapy.IP)
            print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")
        
        if packet.haslayer(scapy.TCP):
            tcp_layer = packet.getlayer(scapy.TCP)
            print(f"TCP Packet: {tcp_layer.sport} -> {tcp_layer.dport}")
        
        if packet.haslayer(scapy.UDP):
            udp_layer = packet.getlayer(scapy.UDP)
            print(f"UDP Packet: {udp_layer.sport} -> {udp_layer.dport}")
        
        # Store packet in database
        self.store_packet(packet)

    def start_monitoring(self):
        interfaces = self.get_interfaces()
        for interface in interfaces:
            thread = threading.Thread(target=self.capture_traffic, args=(interface,))
            thread.start()

if __name__ == "__main__":
    monitor = NetworkMonitor()
    monitor.discover_devices()
    monitor.start_monitoring()
