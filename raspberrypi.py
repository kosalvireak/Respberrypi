import RPi.GPIO as GPIO
import time
import socket
from gpiozero import LED
from datetime import datetime
HOST = "172.16.0.188"
PORT = 6789
ADDR = (HOST, PORT)
max_size = 1024
FORMAT = "utf-8"
led = LED(17)
led_server = LED(27)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
f = open("/home/pi/Desktop/Light sensor.txt", "a")
print("Starting the client at: ", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("""q : for close connection
on : for turn a light on
off: for turn a light off
        """)

# Reading sensor using RaspBerry Pi Zero W GPIO (1)

def fun2():
    for i in range(0, 30):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        time.sleep(1)
        if GPIO.input(4) == 1:
            dark = "\nDark  " + str(current_time)
            f.write(dark)

            # Command one actuator using RaspBerry Pi Zero W GPIO (4)
            
            led.on()
            print(dark)
        elif GPIO.input(4) == 0:
            light = "\nLight " + str(current_time)
            f.write(light)
            print(light)
            led.off()


# Receiving command from your Laptop or Desktop over TCP/IP socket communication using Python and command your actuator (3)

def fun1():
    while True:
        data = client.recv(max_size)
        if data.decode('utf-8') == 'on':
            led_server.on()
            print("light is on")
        elif data.decode('utf-8') == 'off':
            led_server.off()
            print("light is off")
            print("At ", datetime.now(),
                  "server replied with: ", data.decode('utf-8'))
        if data.decode('utf-8') == 'q':
            break


fun2()
fun1()
f.close()

# Send sensor data and datetime over TCP/IP socket communication to your Laptop or Desktop (2)

f = open("/home/pi/Desktop/Light sensor.txt", "r")
data = f.read()
client.send("Light sensor.txt".encode(FORMAT))
msg = client.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
client.send(data.encode(FORMAT))
msg = client.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
f.close()
client.close()
