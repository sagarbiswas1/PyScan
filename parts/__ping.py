import os
import sys
import platform
import subprocess


def main(HOST,Np):
    if Np == False:
        print('\n\033[32m[+]\033[0m Pinging the host..')
        # Option for the number of packets as a function of
        param = '-n' if platform.system().lower()=='windows' else '-c'
        # Building the command. Example: "ping -c 1 google.com"
        command = (f"ping {param} 1 {HOST}")
        # required subprocess here
        run = subprocess.getoutput(command).replace("\n","")
        host_down = run.find("100% packet loss")
        no_network = run.find("Network is unreachable")
        
        if no_network != -1:
            print('\n\033[31mNetworkUnreachable: \033[0mCheck your internet connection')
            sys.exit()
        
        elif host_down != -1:
            print(f'\n{HOST}','seems down or blocking our requests.')
            sys.exit()
    else:
        pass
