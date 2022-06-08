def main(port,serviceName):
    if port < 10:
        print(port,'      \033[32mopen\033[0m',f'      {serviceName}')
    elif port < 100:
        print(port,'    \033[32mopen\033[0m',f'   {serviceName}')
    elif port < 1000:
       print(port,'   \033[32mopen\033[0m',f'   {serviceName}')
    elif port < 10000:
        print(port,'  \033[32mopen\033[0m',f'   {serviceName}')
    else:
        print(port,' \033[32mopen\033[0m',f'   {serviceName}')