import socket

def scan_ips(start_ip, end_ip):
    for i in range(start_ip, end_ip + 1):
        ip = f"10.4.118.{i}"  # Modify the IP format based on your network
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        try:
            sock.connect((ip, 80))  # Attempt to connect to the IP address on port 80
            print(f"IP {ip} is reachable")
        except socket.error:
            pass  # If connection attempt fails, do nothing (IP is not reachable)

        sock.close()

if __name__ == "__main__":
    start_ip = 1  # Modify the start and end IPs based on your network range
    end_ip = 10
    scan_ips(start_ip, end_ip)