# Este script tem o intuito de selecionar as interfaces de rede existentes
#!/usr/bin/python3

import os
os.system("nmcli d | sed -n '2,$p' | awk '{print $1}' | grep -v ^lo > net.txt")

"""
f = open('net.txt','r')
for line in f.readlines():
    print(line)
f.close()

f = open('net.txt','r')
line = f.readline()
while line:
    netip = input("Entre com o IP para a interface %s" %(line))
    netpref = input("Qual PREFIX da rede? ")
    netgw = input("Qual GATEWAY da rede? ")
    print("Configurando a interface com as seguintes configuracoes: IPADDR=%s PREFIX=%s GATEWAY=%s" %(netip, netpref, netgw))
    line = f.readline()
f.close()

filepath = 'nomes'  
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1

filepath = 'net.txt'  
with open(filepath) as fp:
    line = fp.readline()
    while line:
        netip = input("Entre com o IP para a interface %s: " %(line.strip()))
        netpref = input("Qual PREFIX da rede? ")
        netgw = input("Qual GATEWAY da rede? ")
        print("Configurando a interface com as seguintes configuracoes: \n\nIPADDR=%s\nPREFIX=%s\nGATEWAY=%s\n" %(netip, netpref, netgw))
        line = fp.readline()
"""

f = open('net.txt','r')
    fp = open('net2.txt', 'w')
line = f.readline()
while line:
    netip = input("Entre com o IP para a interface %s" %(line))
    netpref = input("Qual PREFIX da rede? ")
    netgw = input("Qual GATEWAY da rede? ")
    print("Configurando a interface com as seguintes configuracoes: IPADDR=%s PREFIX=%s GATEWAY=%s" %(netip, netpref, netgw))
    line = f.readline()
f.close()