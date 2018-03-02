#!/usr/bin/python3 -d

# Importando módulos do S.O.
import os
import socket

# Limpando a tela
os.system("clear")
#print(chr(27) + "[2J")

# Coletando quais interfaces de rede o servidor tem
#os.system("nmcli d | sed -n '2,$p' | awk '{print $1}' | grep -v ^lo > /tmp/net.txt")
network_interfaces = socket.if_nameindex()

# Formando o arquivo de conf para cada interface encontrada no arquivo "/tmp/net.txt
for iface in network_interfaces:
        if iface[1] != "lo":
                print("Encontrei interface: %s" %(iface[1]))
                netip = input("Entre com o IP para a interface %s: " % iface[1])
                netpref = input("Qual PREFIX da rede? ")
                netgw = input("Qual GATEWAY da rede? ")
                print("\nConfigurando a interface com as seguintes configuracoes: \n\nIPADDR=%s\nPREFIX=%s\nGATEWAY=%s\n" %(netip, netpref, netgw))

                interface_file = open("ifcfg-%s" % iface[1], 'w')
                interface_file.write("DEVICE=%s\n" %(iface[1]))
                interface_file.write("TYPE=Ethernet\n")
                interface_file.write("ONBOOT=yes\n")
                interface_file.write("NM_CONTROLLED=yes\n")
                interface_file.write("BOOTPROTO=yes\n")
                interface_file.write("IPADDR=%s\n" %(netip))
                interface_file.write("PREFIX=%s\n" %(netpref))
                interface_file.write("GATEWAY=%s\n" % netgw )
                interface_file.close()
