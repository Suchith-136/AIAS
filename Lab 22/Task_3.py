import socket

def scan_ports(target, port_range=(1, 1024), timeout=0.5):
    """
    Scans the specified ports on the given target to check if they are open.

    Args:
        target (str): The IP address or hostname of the target to scan.
        port_range (tuple): A tuple (start_port, end_port) to specify which ports to scan.
        timeout (float): Timeout in seconds for each port scan.

    Returns:
        list: List of open ports.
    """
    open_ports = []
    print(f"Scanning {target} from port {port_range[0]} to {port_range[1]}...")
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: OPEN")
                open_ports.append(port)
        except Exception as e:
            print(f"Error scanning port {port}: {e}")
        finally:
            sock.close()
    print("Scan complete.")
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP address or hostname: ").strip()
    port_input = input("Enter port range to scan (e.g. 1-1024) [default 1-1024]: ").strip()
    if port_input:
        try:
            start_port, end_port = map(int, port_input.split('-'))
        except Exception:
            print("Invalid port range. Using default (1-1024).")
            start_port, end_port = 1, 1024
    else:
        start_port, end_port = 1, 1024
    timeout_input = input("Enter timeout in seconds per port [default 0.5]: ").strip()
    try:
        timeout = float(timeout_input) if timeout_input else 0.5
    except ValueError:
        timeout = 0.5

    scan_ports(target, (start_port, end_port), timeout=timeout)

