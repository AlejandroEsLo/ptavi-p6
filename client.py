#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Programa cliente que abre un socket a un servidor."""

import socket
import sys


# Cliente UDP simple.
try:
    METODO = sys.argv[1]
    DIRECCION = sys.argv[2]
    LOGIN = DIRECCION.split("@")[0]
    IP_Y_PORT = DIRECCION.split("@")[1]
    IP_RECEPTOR = IP_Y_PORT.split(":")[0]  # 127.0.0.1
    PORT = int(sys.argv[2].split(":")[-1])

except IndexError:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((IP_RECEPTOR, PORT))

    # Contenido que vamos a enviar
    mensaje = (METODO.upper() + " sip:" + LOGIN + "@" + IP_RECEPTOR
               + " SIP/2.0\r\n")

    print("\r\nEnviando: " + mensaje)
    my_socket.send(bytes(mensaje, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

    respuesta_serv = data.decode('utf-8')
    # End para quitar espacio print
    print('Recibido:')
    print(data.decode('utf-8'))

    if respuesta_serv == ("SIP/2.0 100 Trying\r\n\r\n"
                          + "SIP/2.0 180 Ringing\r\n\r\n"
                          + "SIP/2.0 200 OK\r\n\r\n"):
        METODO = "ACK"
        mensaje = (METODO.upper() + " sip:" + LOGIN + "@" + IP_RECEPTOR
                   + " SIP/2.0\r\n")

        print("Enviando: " + mensaje)
        my_socket.send(bytes(mensaje, 'utf-8') + b'\r\n')
        data = my_socket.recv(1024)

    print("Terminando socket...")
my_socket.close()
print("Fin.")
