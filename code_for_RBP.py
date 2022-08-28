# https://www.uugear.com/portfolio/using-light-sensor-module-with-raspberry-pi/


# read from sensor
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)
for i in range(0,5):
    print (GPIO.input(4))

# write to a file

# start client and send file to the server

import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    # Staring a TCP socket. #
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to the server. #
    client.connect(ADDR)

    # Opening and reading the file data. #
    file = open("text.txt", "r")
    data = file.read()

    # Sending the filename to the server. #
    client.send("from client.txt".encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    # Sending the file data to the server. #
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    # Closing the file. #
    file.close()

    # Closing the connection from the server. #
    client.close()


if __name__ == "__main__":
    main()
