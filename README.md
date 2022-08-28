# Respberrypi
## Boardnumber 9
```
username: pi
password: 011018
ip: 172.16.1.173

```


## Boardnumber 20
```
username: pi
password: 011018
ip: 172.16.1.175

```

### We can send sensor output directly to server

```
while True:
    data = GPIO.input(4)
    client.send(data.encode(FORMAT))

```