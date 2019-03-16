import threading
import socket


host = ''
port = 9000
tello_IP = '192.168.10.1'
tello_command_port = 8889
tello_state_port = 8890
tello_stream_port = 11111

locaddr = (host,port)
tello_command_address = (tello_IP, tello_command_port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Create a UDP socket


sock.bind(locaddr)
