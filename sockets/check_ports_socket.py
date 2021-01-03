import socket
import sys


def checkPortSocket(ip, portlist):
    try:
        for port in portlist:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #indica el tiempo de intento de conexión en segundos
            sock.settimeout(5)
            #establece una conexión con los parámetros pasados y devuelve un error
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Puerto{} : \t esta Abierto".format(port))
            else:
                print("Puerto{} : \t esta Cerrado".format(port))
            sock.close()
    except socket.error as error:
        print(str(error))
        print("Error de conexion")
        sys.exit()
checkPortSocket('localhost',[80,8080,443])