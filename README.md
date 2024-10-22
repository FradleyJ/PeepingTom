
PeepingTom

PeepingTom is a simple Python-based network port scanner that allows users to scan specified ports on a target host. It checks if the selected ports are open or closed by attempting to establish TCP connections to them. This tool is useful for network troubleshooting, security assessments, or learning about network sockets and port scanning.

Features

- Scans specified ports on a target host.
- Displays whether the port is open or closed.
- Performs DNS lookup to resolve the target host's IP address.
- Optionally performs reverse DNS to get the hostname from an IP address.

How It Works

1. The script uses Python's socket library to create network connections.
2. A connection is attempted for each specified port on the target host.
3. If a connection is successful, the port is marked as open; otherwise, it is marked as closed.
4. The script attempts to resolve the IP address of the target host and can also retrieve its reverse DNS hostname (if available).

Prerequisites

- Python 3.x installed on your machine.
- Basic understanding of networking concepts such as IP addresses, ports, and DNS.

Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PeepingTom.git
   cd PeepingTom

2. Ensure you have Python installed:
   ```bash
   python --version

Usage

1. Open a terminal and navigate to the project directory:
   ```bash
   cd PeepingTom

2. Run the Python script with your target host and ports:
     ```bash
     python peepingtom.py

3. Example usage:
   ```bash
   python peepingtom.py google.com 80 22 443

4. The script will output whether the specified ports are open or closed on the target host.

Example Output:
   ```bash
  [+] Scan result of : 172.217.10.110
  Scanning Port: 80
  [+]80/tcp open  
  Scanning Port: 22
  [-]22/tcp closed
  Scanning Port: 443
  [+]443/tcp open
```

5. Customization

You can modify the script to scan a different set of ports or modify how it handles connection attempts (e.g., timeout length, protocol type, etc.).

Limitations

- This tool scans TCP ports only (not UDP).
- Reverse DNS resolution may not return the expected hostnames for all servers.
- Port scanning may be flagged as suspicious activity by some firewalls or intrusion detection systems. Use responsibly.

Contributing

Feel free to fork the repository and submit pull requests for bug fixes or new features. Contributions are welcome!
