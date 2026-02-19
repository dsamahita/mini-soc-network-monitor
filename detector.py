
from scapy.layers.inet import IP

ip_count = {}
alerted_ips = set()

THRESHOLD = 20

def analyze_packet(packet):
    if packet.haslayer(IP):
        src = packet[IP].src

        if src not in ip_count:
            ip_count[src] = 0

        ip_count[src] += 1

        if ip_count[src] > THRESHOLD and src not in alerted_ips:
            print("🚨 ALERT: Suspicious high traffic detected!")
            print("Source IP:", src)
            print("-" * 50)
            alerted_ips.add(src)
            MY_IP = "192.168.1.9"


