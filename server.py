import socket
s=socket.socket()       #initialization of socket 

host , port=socket.gethostname() , 1234   

print("server will start on host : "+host)

s.bind((host,port))   #bind the server with host and port
print('Server is bound successfully')

s.listen(1000)        #1000 define that 1000 device can be connect by this server
conn,address=s.accept()   

print(address," client has connected")
while 1:
    conn,address=s.accept()
    msg=Distance("my current location","my current location")
    msg=msg.encode()
    conn.send(msg) 
    in_msg=s.recv(5000) 
    in_msg=in_msg.decode()
    print("Server:>>",in_msg)

