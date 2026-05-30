# Network Scanner

A lightweight Python-based network scanner that uses ARP requests to discover active devices on a local network. Built with Scapy, the tool identifies hosts within a target subnet and displays their IP and MAC addresses in a clean, readable format.

## Features:
- Discovers active devices on a local subnet
- Enumerates IP and MAC address information
- Uses ARP broadcast requests for host discovery
- Command-line interface for specifying target ranges
- Lightweight and easy to extend

## Technologies Used:
- Python 3
- Scapy
- ARP Protocol
- Networking Fundamentals

## Example Usage:
python3 network_scanner.py -t 192.168.1.0/24

Sample Output:
IP                  MAC Address
-------------------------------------------
192.168.1.1         00:11:22:33:44:55
192.168.1.25        AA:BB:CC:DD:EE:FF

## Skills Demonstrated:
- Network programming
- Packet crafting and analysis
- Python development
- Command-line application design
- Data collection and formatting
- Troubleshooting and debugging
- Learning Objectives
  
--------------------------------------------------------------------------------------------------------------------------------------------
This project was developed to strengthen my understanding of network discovery techniques, ARP communication, packet manipulation, and Python-based automation
