# 🚨 Mini SOC Network Monitor (Python IDS)

## 📌 Project Overview
This is a lightweight Intrusion Detection System (IDS) built using Python and Scapy.  
It monitors live network traffic and detects incoming external connections in real-time.

---

## 🔍 Features
- Real-time packet sniffing
- Incoming connection detection
- Alert generation
- Modular architecture (Sniffer, Detector, Logger)
- Tested using Nmap

---

## 🛠 Technologies Used
- Python
- Scapy
- Nmap
- TCP/IP Networking

---

## 🧠 How It Works
Packet Sniffer captures network packets →  
Detector analyzes source & destination IP →  
If external incoming connection detected →  
Alert is triggered →  
Logger stores suspicious activity.

---

## ▶ How To Run

Install dependencies:

pip install -r requirements.txt

Run the program:

python main.py

---

## 🧪 Testing
Simulated incoming connections using:

& "C:\Program Files (x86)\Nmap\nmap.exe" -p 1-200 192.168.1.9

---

## 📸 Sample Output

🚨 ALERT: Incoming connection detected!

---

## 🎯 Learning Outcomes
- Understanding packet structure
- TCP/IP protocol basics
- Intrusion detection fundamentals
- Practical cybersecurity implementation
