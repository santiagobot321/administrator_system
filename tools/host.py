import socket

def send_shutdown(ip, port=9876):
    """Connect to the agent and send shutdown command"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    s.sendall(b"shutdown now")
    s.close()
    print(f"Shutdown command sent to {ip}:{port}")

if __name__ == "__main__":
    vm_ip = "192.168.1.93"  # <-- cámbialo por la IP de tu VM
    send_shutdown(vm_ip)
