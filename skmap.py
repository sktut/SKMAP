import socket

def scan_ports(ip, start_port, end_port):
    open_ports = []
    closed_ports = []
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)
        sock.close()
    
    return open_ports, closed_ports

def print_logo():
    logo = """
           __________    
         /__________/          ||  //
        //                     || //
       //                      ||//
       \\                       ||\\
        \\  --------            || \\
          __________           ||  \\ 
          --------             ||   \\ 
                 / /     M A P P I N G 
     /--------- / /
    /____________

    """
    print(logo)

def main():
    print_logo()
    
    ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port number: "))
    end_port = int(input("Enter the end port number: "))

    open_ports, closed_ports = scan_ports(ip, start_port, end_port)

    print("Open ports:")
    for port in open_ports:
        print(port)

    print("\nClosed ports:")
    for port in closed_ports:
        print(port)

if __name__ == "__main__":
    main()
