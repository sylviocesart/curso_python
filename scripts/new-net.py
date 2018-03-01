#!/usr/bin/python3

import os

# Limpando a tela
os.system("clear")

# Coletando quais interfaces de rede do servidor
os.system("nmcli d | sed -n '2,$p' | awk '{print $1}' | grep -v ^lo > /tmp/net.txt")

# Formando o arquivo de conf para cada interface encontrada no arquivo "/tmp/net.txt

f = open('/tmp/net.txt','r')
line = f.readline()
while line:
        print("\n")
        fileNET = open('/tmp/ifcfg-%s' %(line.strip()),'w')
        netip = input("Entre com o IP para a interface %s: " %(line.strip()))
        netpref = input("Qual PREFIX da rede? ")
        netgw = input("Qual GATEWAY da rede? ")
        texto = ('DEVICE=%s' %(line.strip()) + '\n')
        texto += ('TYPE=Ethernet' + '\n')
        texto += ('ONBOOT=yes' + '\n')
        texto += ('NM_CONTROLLED=yes' + '\n')
        texto += ('BOOTPROTO=static' + '\n')
        texto += ('IPADDR=' + netip + '\n')
        texto += ('PREFIX=' + netpref + '\n')
        texto += ('GATEWAY=' + netgw + '\n')
        fileNET.write(texto)
        line = f.readline()
line = f.readline()
os.system("sleep 1")
print("\n")
print("Configuracao de interfaces finalizadas.")
f.close()
