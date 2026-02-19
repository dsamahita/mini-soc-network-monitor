from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]

        print("Source IP:", ip_layer.src)
        print("Destination IP:", ip_layer.dst)

        # 🚨 Alert if someone connects to YOU
        if ip_layer.dst == "192.168.1.9":
            print("🚨 ALERT: Incoming connection detected!")

        print("-" * 50)

print("Starting packet monitor...")
print("Press CTRL+C to stop\n")

sniff(prn=packet_callback, store=False)
