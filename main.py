#Python Network Port Scanner Project
from socket import * # imports all functions,classes,constants from 'socket' module- a socket is an endpoint defined by IP addr., Port #,
# TCP/UDP to send/receive data- 10.0.0.1:80 IP:Port - Your browser creates a socket to HTTP/S(80/443) using servers IP Google(172.217.164.110:443)
def conScan(tgtHost, tgtPort): #defining function conScan with 2 arguments (target host, target port)
    try:
        connskt = socket(AF_INET, SOCK_STREAM) # connskt creates a new TCP socket - AF_INET specifies IPv4/SOCK_STREAM indicates it's TCP connection
        connskt.connect((tgtHost, tgtPort))# Tries to connect to target host at selected port, takes tuple of (host, port) as argument.
        print('[+]%d/tcp open'% tgtPort)# Prints# target port is open if connection is successful
    except:
        print('[-]%d/tcp closed'% tgtPort)# If connection is not succesful tells you target port is closed. 

def portScan(tgtHost, tgtPorts):# creating a function using target host and target ports as argumetns
    try:
        tgtIP = gethostbyname(tgtHost)# resolves host name 'target host' to its corresponding IP address
    except:# if not possible
        print('[-] Cannot resolve %s'% tgtHost)# will print 'cannont resolve' with a string of the target host domain name 
        return# stops further execution of the function
    try:
        tgtName = gethostbyaddr(tgtIP)# tries to get the host name by IP address
        print('\n[+] Scan result of : %s'% tgtName[0])# if succussful it prints host name
    except:
       print('\n[+] Scan result of : %s'% tgtIP)#if reverse lookup fails it prints the IP address
    setdefaulttimeout(1)# a default timeout of 1 second for socket operations
    for tgtPort in tgtPorts:# starts a loop that iterates through the list of ports provided
        print("Scanning Port: %d " % tgtPort)
        conScan(tgtHost, int(tgtPort))  #calls conScan function for ea. port- passing target host & target port
                       

if __name__== '__main__':# checksif script is being run directly(as opposed to being imported as a module)
    portScan('discord.com', [80,22,23,44,21,110,143,25,53,3306,123,111,2049,135,137,138,445])#calls portScan function passing "google.com" as tgthost and [80,22] as list of ports to scan. 