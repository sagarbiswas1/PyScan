#!/usr/bin/env python3

import os
import sys
import time
import socket
import threading
from queue import Queue
import parts.__ping as ping
import parts.__print as prnt
import parts.__argvmanager as manage

print(f'''
\033[34;1m   ____       \033[0;1m ____
\033[34;1m  |  _ \\ _   _\033[0;1m/ ___|  ___ __ _ _ __
\033[34;1m  | |_) | | | \033[0;1m\\___ \\ / __/ _` | '_ \\
\033[34;1m  |  __/| |_| |\033[0;1m___) | (_| (_| | | | |
\033[34;1m  |_|    \\__, |\033[0;1m____/ \\___\\__,_|_| |_|
\033[34;1m         |___/

''')

this_file = os.path.basename(__file__)

if manage.main(this_file):
    HOST = manage.main.HOST
    port_range = manage.main.port_range
    Np = manage.main.Np

def main(HOST,port_range):
    print('\033[32m[+]\033[0m Starting scan..')
    start_time = time.time()
    queue = Queue()
    OPENED = []
    
    print('\n\033[35mPORT   STATUS  SERVICE\033[0m')
    
    def scan(target,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        con = s.connect_ex((target,port))
        
        if not con:
            try:
                serviceName = socket.getservbyport(port)
            except OSError:
                serviceName = 'unknown'
            
            prnt.main(port,serviceName)
            s.close()
            return True
        
        else:
            s.close()
            return False
    
    def GetQueue():
        try:
            for ports in range(port_range[0],port_range[1] + 1):
                queue.put(ports)
        except IndexError:
            for ports in range(port_range[0] + 1):
                queue.put(ports)
    
    def buildQueue():
        while not queue.empty():
            p = queue.get()
            if (scan(HOST,p)):
                OPENED.append(p)
    
    GetQueue()
    thread_list = []
    
    for t in range(15):# WARNING : extending the thread can cause the program to get stuck, range 10-15 recommend.
        thread = threading.Thread(target=buildQueue)
        thread_list.append(thread)
    
    for thread in thread_list:
        try:
            thread.start()
        except Exception as e:
            pass
    
    for thread in thread_list:
        thread.join()
    
    now_time = time.time()
    time_in_int = int(now_time - start_time)
    seconds = time.strftime('%M:%S', time.gmtime(time_in_int))
    
    if not OPENED:
        print('All scanned ports are closed.')
    
    print(f'\nScan finished in {seconds} sec')


if __name__ == '__main__':
    try:
        ping.main(HOST,Np)
        main(HOST,port_range)
    
    except KeyboardInterrupt:
        
        print('\n\033[31mScan terminated!\033[0m')
        os._exit(1)
