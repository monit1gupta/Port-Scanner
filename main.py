import socket

# Get the host IP/URL from the scanner
# Option 1: User input
# host = input("Please enter the host details: ")

# Option 2: Use own IP address
# host = socket.gethostbyname(socket.gethostname())  # Getting IP address of the host
host = '10.0.2.15'  # Getting IP address of the host


# Function to check if a port is open
def is_port_open(host, port):
    """
    This function checks if a specific port is open on a given host.

    Args:
        host: The IP address or hostname of the target machine.
        port: The port number to check.

    Returns:
        True if the port is open, False otherwise.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a new TCP socket
    try:
        s.bind((host, port))  # Attempt to bind the socket to the host and port
    except:
        # Port is closed
        # print("could not connect")
        return True
    else:
        # Port is open
        # print("connected to port " + port)
        return False
    finally:
        s.close()  # Close the socket


# Iterate over all important ports
# Port range can be adjusted to include specific services
for port in range(1, 65000):
    if is_port_open(host, port):
        print(str(port) + " is open!")
