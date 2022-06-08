import sys
import socket

def main(file):
    def summary():
        print(f'\n{file}','[ HOST ] [ OPTIONS ]\n')
        print('Options')
        print('\033[34m-p-\033[0m   ','  scan 1-65535 ports\n')
        print('\033[34mmin-max\033[0m ',' scan specified ports ( Example 1-1000, scan 1 to 1000 ports) \n')
        print('\033[34m-Np\033[0m   ','  No ping (start port scan without pinging the host)\n')
        print('\033[34m--help\033[0m  ','print this help summary\n')
        print('By default it scans 1000 ports')
        sys.exit()
    
    if len(sys.argv) > 4 or len(sys.argv) < 2:
        summary()
    
    if sys.argv[1] == '--help':
        summary()
    
    
    arguments = sys.argv
    raw_host = arguments[1]
    port_range = [1,1000]
    Np = False
    
    if len(arguments) == 3:
        if arguments[2] == '-Np':
            Np = True
        else:
            try:
                port_range = [ int(x) for x in arguments[2].replace('-p-','65535').split('-') ]
            except:
                print(f'\033[31;1mE:\033[0m invalid argument \'{arguments[2]}\'')
                sys.exit()
    
    elif len(arguments) == 4:
        try:
            port_range = [ int(x) for x in arguments[2].replace('-p-','65535').split('-') ]
            if arguments[3] == '-Np':
                Np = True
            else:
                print(f'\033[31;1mE:\033[0m invalid argument \'{arguments[3]}\'')
                sys.exit()
        except:
            try:
                port_range = [ int(x) for x in arguments[3].replace('-p-','65535').split('-') ]
            except:
                print(f'\033[31;1mE:\033[0m invalid argument \'{arguments[3]}\'')
                sys.exit()
            
            if arguments[2] == '-Np':
                Np = True
            else:
                print(f'\033[31;1mE:\033[0m invalid argument \'{arguments[2]}\'')
                sys.exit()
    
    try:
        HOST = socket.gethostbyname(raw_host)
    except socket.gaierror:
        print(f'\033[31;1mE:\033[0m Unrecognised host \'{raw_host}\'')
        sys.exit()
    
    main.HOST = HOST
    main.port_range = port_range
    main.Np = Np
    return main.HOST
