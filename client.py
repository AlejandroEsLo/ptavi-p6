#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys
# Cliente UDP simple.

# Dirección IP del servidor.
try:
    METODO = sys.argv[1]    
    DIRECCION = sys.argv[2]
    LOGIN = DIRECCION.split("@")[0]
    IP_Y_PORT = DIRECCION.split("@")[1]
    IP_RECEPTOR = IP_Y_PORT.split(":")[0] # 127.0.0.1
    PORT = int(sys.argv[2].split(":")[-1])
    
except IndexError:
    sys.exit("Usage: python3 client.py method receiver@IP:SIPport")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((IP_RECEPTOR, PORT))
#Prueba para ver que enviamos
    
    print("Metodo = " + METODO + " LOGIN = " + LOGIN + " IP = " + IP_RECEPTOR \
    + " PUERTO = " + str(PORT) )

    # Contenido que vamos a enviar
    mensaje = (METODO.upper() + " sip:" + LOGIN + "@" + IP_RECEPTOR \
                + " SIP/2.0\r\n")
    
    print("Enviando: " + mensaje)
    my_socket.send(bytes(mensaje, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
