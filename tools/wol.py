import socket

def send_wol(mac_address, broadcast="255.255.255.255"):
    """Sending the magic packet to turn on the PC"""

    mac_address = mac_address.replace(":", "").replace("-", "")
    if len(mac_address) != 12:
        raise ValueError("MAC address wrong")
    
    data = bytes.fromhex("FF" * 6 + mac_address * 16)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    sock.sendto(data, (broadcast, 9))
    print(f"Magic packet sent to {mac_address}")
