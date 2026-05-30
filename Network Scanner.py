#!/usr/bin/env python3

import scapy.all as scapy #shorten the module name
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #Send the ARP request packets, capture answered and unanswered requests. TIme out after 1sec
    
    clients_list = []
    for element in answered_list:
        client_dictionary = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        clients_list.append(client_dictionary)
    return clients_list

def print_result(results_list):
    print("IP\t\t\tMAC Address\n-------------------------------------------")
    for client in results_list:
        print(client["IP"] + "\t\t" + client["MAC"])

options = get_arguments()
scan_result = scan("192.168.1.231/24")
print_result(scan_result)