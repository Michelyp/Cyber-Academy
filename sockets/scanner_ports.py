from socket import *

# preguntamos por la ip
ip = input("Introduce IP :")
start = int(input("Introduce puerto de inicio: "))
# preguntamos por los puertos
end = int(input("Introduce puerto de fin: "))
print("Escaneado IP{}: ".format(ip))
for port in range(start, end):
    print("Probando puerto{}...".format(port))
    # crea el objeto socket
    s = socket(AF_INET, SOCK_STREAM)
    # establecer timeout
    s.settimeout(5)
    # comprobar conexión
    if (s.connect_ex((ip, port)) == 0):
        # puerto abierto
        print("Puerto", port, "abierto")
    # cierra el socket
    s.close()
    print("Escaneo finalizado!")
