
import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

print("[STARTING] Server is starting.")
# Staring a TCP socket. #
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the IP and PORT to the server. #
server.bind(ADDR)

# Server is listening, i.e., server is now waiting for the client to connected. #
server.listen()
print("[LISTENING] Server is listening.")

while True:
    # Server has accepted the connection from the client. #
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    # Receiving the filename from the client. #
    filename = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the filename.")
    file = open(filename, "a")
    conn.send("Filename received.".encode(FORMAT))

    # Receiving the file data from the client. #
    data = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    conn.send("File data received".encode(FORMAT))

    # Closing the file. #
    file.close()

    # Closing the connection from the client. #
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")



# insert data base

import mysql.connector


dataBase = mysql.connector.connect(

host="localhost",

user="root",

passwd="",

database="kosalvireak"
)


cursorObject = dataBase.cursor()
f = open(r"Light sensor.txt")
for x in f:
    res = x.split()
    sql = "INSERT INTO tbl_STUDENT (NAME, EMAIL) VALUES (%s, %s)"
    val = (str(res[0]), str(res[1]))
    #or we can simple type below code in phpMyAdmin >> SQL >> past in query box >> Go 
    #INSERT INTO `tbl_student`(`NAME`, `EMAIL`) VALUES ('student3','student3@gmail.com')
    cursorObject.execute(sql, val)
    dataBase.commit()
