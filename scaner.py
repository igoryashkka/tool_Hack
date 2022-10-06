#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--target" , dest="target", help="Target ip /ip range")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)	
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast , timeout = 1,verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
    	client_dict = {"ip" : element[1].psrc,"MAC":element[1].hwsrc}
    	clients_list.append(client_dict)
    	#print(element[1].psrc + "\t\t" + element[1].hwsrc)
    return clients_list
 
 
def print_result(result_list):
    print("____________________________________________")	   
    print("IP\t\t\tMAC Adreess")
    print("____________________________________________")
    for client in result_list:
    	print(client["ip"] + "\t\t" + client["MAC"] )
    	

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)

 