from socket import gethostname, gethostbyname


def check_connection():
    """  if ip address equal to 127.0.0.1 that mean there is no internet connection. """
    return gethostbyname(gethostname()) != "127.0.0.1"
