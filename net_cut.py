#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy
from scapy.layers import http


def process_packet(packet):
    print(packet)


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
