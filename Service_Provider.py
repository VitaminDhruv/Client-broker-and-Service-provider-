# first of all import the socket library 
import socket   
#import sys              

# next create a socket object 
s = socket.socket()          
print("Socket successfully created")
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 5045      
  
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('127.0.0.1', port))         
print("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print("socket is listening")            
   # Establish connection with client. 


client, addr = s.accept()  

# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
#   # Establish connection with client. 
#   client, addr = s.accept()      
   print('Got connection from', addr)
  
   # send a thank you message to the client. 
   data=client.recv(1024).decode()
#   data=data[::-1]
   if not data:
        break 
   
    
   print('from connected user: '+str(data))
   data=('Yes I can provide you service!')
   print(data)
   
   # sending data to client 
   client.sendall(data.encode('utf-8'))
   break 
#   print(data)
#   output='Thank you for connecting'
#   client.sendall(output.encode('utf-8')) 
#   client.sendall(data)
#   
  
   # Close the connection with the client 
client.close() 