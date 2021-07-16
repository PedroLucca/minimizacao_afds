import numpy as np
from afd import AFD

print("--- MINIMIZAÇÃO DE AFD's ---\n\n")
num = int(input("Digite o numero de estados do automato: "))
estado_inicial = str(input("Qual o estado inicial: "))
estados_finais = str(input("Quais os estados finais (Separe com uma vírgula se houver mais de um): ")).split(',')
afd_inicial = open("automato.txt", 'r')
automato = []
for line in afd_inicial:
    automato.append(line.rstrip('\n'))

afd = AFD(estado_inicial, estados_finais, automato, num)
afd.minimizar()
print("\n")
print("Finalizado...")
print("\n")
print("Estado inicial: ", afd.estado_inicial)
print("Estados finais: ", afd.estados_finais)
print("Resultado no arquivo minimizado.txt!")
        