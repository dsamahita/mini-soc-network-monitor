
from scapy.all import sniff
from detector import analyze_packet


def run_sniffer():
    print("Starting Mini SOC Network Monitor...")
    print("Press CTRL+C to stop\n")
    sniff(prn=analyze_packet, store=False)

