# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 19:34:23 2018

@author: Dhruv
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 13:58:44 2018

@author: Dhruv
"""

# Import socket module 
import socket          
#import sys      
  
# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
Server_port=0  
p=True  
# Define the port on which you want to connect 
while p:
        port = 5000                
        
        # connect to the server on local computer 
        s.connect(('127.0.0.1', port)) 
        
        # receive data from the server 
        
        d=True 
        x=((input('Enter the request you want: ')))
        
        while d:
            #x=((input('Enter the request you want: ')))
            
            #x=input('What is your name: ')
            # Sending the message to the server 
            print(x)
            print('---- - - -- - - - -')
            s.sendall(str(x).encode('utf-8'))
            # recieving response from the server 
            data=s.recv(1024).decode()
            print('recieve from the server: '+data)
            if data[:3]=='Yes' :   
                    #x=input('reply: ')
                    Server_port=int(data[-4:])
                    
                    d=False
                    p=False 
                    s.close()
                    
            else:
                        x=input('Enter the another request: ')
                        # receive data from the server 
                        #print('receiving data from server...')
                        #print(s.recv(1024))
                        
                        # close the connection 
                        
                        
                        
print(Server_port)
        
Ck_cnnect=input("Enter 'y' to connect to the Main Service provide:")
                        
if Ck_cnnect=='y':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          
   
    port=Server_port
    s.connect(('127.0.0.1',port))
    message=('Can you provide service: '+str(x)+' on you port '+str(port))
    s.sendall(str(message).encode('utf-8'))
    data=s.recv(1024).decode()
    print('recieve from the server: '+data)
    s.close()

                            
                            
                            



                    
                    
                    
                    
       