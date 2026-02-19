from scapy.all import IP

MY_IP = "192.168.1.9"  # your machine IP

def analyze_packet(packet):
    # make sure the packet has an IP layer
    if IP not in packet:
        return

    # now you can safely ignore your own outgoing traffic
    if packet[IP].src == MY_IP:
        return

    # rest of your alert logic
    src = packet[IP].src
    print(f"🚨 ALERT: Suspicious high traffic detected!\nSource IP: {src}\n--------------------------------------------------")
