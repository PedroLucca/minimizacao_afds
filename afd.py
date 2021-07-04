import numpy as np
from node import Node
from tab import TAB

class AFD:
    def __init__(self, estado_inicial, estados_finais, automato, num):
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.automato = automato
        self.alfabeto = []
        self.n = num
        self.nodes = []
        self.estados = []
        self.tabela = []
    
    def inicializar(self):
        for node in self.automato:
            node = node.split(',')
            self.nodes.append(Node(node[0], node[1], node[2]))
            if node[0] not in self.estados:
                self.estados.append(node[0])
            if node[1] not in self.estados:
                self.estados.append(node[1])
            if node[2] not in self.alfabeto:
                self.alfabeto.append(node[2])


    def construcao_da_tabela(self):
        passou = []
        for i in range(0, self.n-1):
            for k in range(1, self.n):
                if self.estados[i] != self.estados[k] and self.estados[k] not in passou:
                    self.tabela.append(TAB(self.estados[i], self.estados[k], False))
            passou.append(self.estados[i])

    def marcacao_dos_pares(self):
        for tab in self.tabela:
            if tab.est_1 in self.estados_finais and tab.est_2 not in self.estados_finais:
                tab.marcado = True
            elif tab.est_2 in self.estados_finais and tab.est_1 not in self.estados_finais:
                tab.marcado = True
    
    #Verifica se o elemento não-marcado da tabela deve ser marcado(retorna False se deve ser marcado)
    def verifica(self, est_1, est_2, valor):
        resultados = []
        for node in self.nodes:
            if node.estado == est_1 and node.valor == valor:
                resultados.append(node.next_estado)
            elif node.estado == est_2 and node.valor == valor:
                resultados.append(node.next_estado)

        if len(resultados) == 1:
            return True
        else:
            for tab in self.tabela:
                if (tab.est_1 == resultados[0] or tab.est_2 == resultados[0]) and (tab.est_1 == resultados[1] or tab.est_2 == resultados[1]):
                    if tab.marcado == False:
                        return True
        return False

    def analise_pares_nao_marcados(self):
        for tab in self.tabela:
            if not tab.marcado:
                if not (self.verifica(tab.est_1, tab.est_2, self.alfabeto[0])) or not (self.verifica(tab.est_1, tab.est_2, self.alfabeto[1])):
                    tab.marcado = True

    def unificacao_pares_nao_marcados(self):
        pass

    def exclusao_pares_inuteis(self):
        pass


    def minimizar(self):
        self.inicializar()
        #passo 1
        self.construcao_da_tabela()
        #passo 2
        self.marcacao_dos_pares()
        #passo 3
        self.analise_pares_nao_marcados()
        #passo 4
        self.unificacao_pares_nao_marcados()
        #passo 5
        self.exclusao_pares_inuteis()
        

        #Exibir resultado final!
        
