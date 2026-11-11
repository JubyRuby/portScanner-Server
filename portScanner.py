import socket;
import threading;
from queue import Queue;

target= "127.0.0.1"

def portScan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #uses tcp instead of udp
        #target connection
        sock.connect((target, port))
        return True
    except:
        return False

queue = Queue()
open_Ports=[]

def fillQ(portList):
    for port in portList:
        queue.put(port)



def workerMethod():
    while not queue.empty():
        port = queue.get()
        if portScan(port):
            print("Port {} is open".format(port))
            open_Ports.append(port)


port_list = range(1,8889)
fillQ(port_list)

thread_list= []
for t in range(1000):
    thread = threading.Thread(target=workerMethod)     
    thread_list.append(thread)  


for thread in thread_list:
    thread.start()
    
for thread in thread_list:
    thread.join()

print("Open ports are ", open_Ports)
