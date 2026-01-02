import socket
import sys
from datetime import datetime

def port_scanner():
    remote_server = input("Enter a remote host to scan (IP or URL): ").strip()
    try:
        # Use gethostbyname() to resolve hostnames to IP addresses
        remote_server_ip = socket.gethostbyname(remote_server)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting.")
        sys.exit()

    print("-" * 60)
    print(f"Scanning remote host: {remote_server_ip}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 60)

    t1 = datetime.now()

    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            
            # Fixed: connect_ex() not connect.ex()
            # Also fixed the parentheses
            result = sock.connect_ex((remote_server_ip, port))

            if result == 0:
                print(f"Port {port}: Open")
            
            sock.close()

    except KeyboardInterrupt:
        print("\nExiting Program!!!")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()
    total_time = t2 - t1
    print(f"Scanning Complete in: {total_time}")

if __name__ == "__main__":
    port_scanner()