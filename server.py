#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
                
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            
            if not line:
                break
           
           # Escribe dirección y puerto del cliente (de tupla client_address)
            print("El cliente nos manda " + line.decode('utf-8'))
                    
            mensaje_cliente = line.decode("utf-8").split(" ")
            Ip = self.client_address[0]
            metodo = mensaje_cliente[0]
            direccion = mensaje_cliente[1]

            if metodo == "INVITE":
                respuesta_serv = ("SIP/2.0 100 Trying\r\n\r\n" \
                                    + "SIP/2.0 180 Ringing\r\n\r\n" \
                                    + "SIP/2.0 200 OK\r\n\r\n")
            
                self.wfile.write(bytes(respuesta_serv, "utf-8"))
            
            elif metodo == "ACK":
               print("LLEGA ACK")
            
            #    print("Metodo = " + metodo + " IP = " + Ip + " Direccion = " \
            #    + direccion)
                
            # Si no hay más líneas salimos del bucle infinito
            

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 5555), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
