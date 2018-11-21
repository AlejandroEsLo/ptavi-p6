#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Clase (y programa principal) para un servidor de eco en UDP simple."""

import socketserver
import sys
import os


class EchoHandler(socketserver.DatagramRequestHandler):
    """Echo server class."""

    def handle(self):
        """Manejador del servidor."""
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

            # Escribe dirección y puerto del cliente (de tupla client_address)
            print("El cliente nos manda " + line.decode('utf-8'))

            mensaje_cliente = line.decode("utf-8").split(" ")
            metodo = mensaje_cliente[0]
            Ip = self.client_address[0]

            if metodo == "INVITE":
                respuesta_serv = ("SIP/2.0 100 Trying\r\n\r\n"
                                  + "SIP/2.0 180 Ringing\r\n\r\n"
                                  + "SIP/2.0 200 OK\r\n\r\n")
                self.wfile.write(bytes(respuesta_serv, "utf-8"))

            elif metodo == "ACK":
                # aEjecutar es un string con lo que ejcutara en la shell
                aEjecutar = ("mp32rtp -i " + Ip + " -p 23032 < " + fich_audio)
                print("Vamos a ejecutar", aEjecutar)
                os.system(aEjecutar)

            elif metodo == "BYE":
                respuesta_serv = ("SIP/2.0 200 OK\r\n\r\n")
                self.wfile.write(bytes(respuesta_serv, "utf-8"))

            elif metodo != ["INVITE", "ACK", "BYE"]:
                respuesta_serv = ("SIP/2.0 405 Method Not Allowed\r\n\r\n")
                self.wfile.write(bytes(respuesta_serv, "utf-8"))

            else:
                respuesta_serv = ("SIP/2.0 400 Bad Request\r\n\r\n")
                self.wfile.write(bytes(respuesta_serv, "utf-8"))


if __name__ == "__main__":
    try:
        Ip_serv = sys.argv[1]
        puerto_serv = int(sys.argv[2])
        fich_audio = sys.argv[3]
    except IndexError:
        sys.exit("Usage: python3 server.py IP port audio_file")
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer((Ip_serv, puerto_serv), EchoHandler)
    print("Listening...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
