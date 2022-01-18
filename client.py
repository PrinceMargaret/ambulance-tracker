import socket

s=socket.socket()
host=input("enter server host name or server ip address: ")

port=1234
s.connect((host,port))
print('connected to server')
while 1:
    in_msg=s.recv(5000)
    in_msg=in_msg.decode()
    print("Server:>>",in_msg)
    msg=Distance("current location","current location")
    msg=msg.encode()
    s.send(msg)



