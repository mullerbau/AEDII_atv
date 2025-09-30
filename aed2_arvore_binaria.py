import random
import time


class Lista:
    def __init__(self):
        # cria uma lista vazia com o nome elementos
        self.elementos = []
    
    def inserir(self, valor):
        # insere o valor ao final da lista
        self.elementos.append(valor)
    
    def buscar(self, valor):
        # vai passando por cada elemento até achar o valor, ou acabar a lista
        for elemento in self.elementos:
            if elemento == valor:
                return True  # retorna True se achou
        return False  # retorna False se não achou


class Node:
    def __init__(self, valor):
        # atribui o valor ao nó
        self.valor = valor
        # inicia os ponteiros para os filhos como None
        self.esquerda = None  # insere valores menores 
        self.direita = None   # insere valores maiores 


class Arvore:
    def __init__(self):
        # começa uma árvore vazia, sem raiz
        self.raiz = None

    def inserir(self, valor):
        # se ainda não tem raiz, cria a raiz
        if self.raiz is None:
            self.raiz = Node(valor)
            return

        # começa a inserção pela raiz
        no_atual = self.raiz

        while True:
            # se o valor for menor, vai pra esquerda
            if valor < no_atual.valor:
                if no_atual.esquerda is None:
                    no_atual.esquerda = Node(valor)  # achou o valor
                    break
                else:
                    no_atual = no_atual.esquerda  # continua descendo

            # se o valor for maior, vai pra direita
            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = Node(valor)  # ahcou o valor
                    break
                else:
                    no_atual = no_atual.direita  # continua descendo

            # se o valor já existe, não insere novamente
            else:
                break

    def buscar(self, valor):
        # começa a busca pela raiz
        no_atual = self.raiz

        # verifica se a árvore está vazia
        if no_atual is None:
            return False

        # procura o valor descendo pela árvore
        while no_atual is not None:
            # se achou o valor, retorna True
            if valor == no_atual.valor:
                return True
            # verifica se é menor, se for, vai pra esquerda
            elif valor < no_atual.valor:
                no_atual = no_atual.esquerda
            # verifica se é maior, se for, vai pra direita
            else:
                no_atual = no_atual.direita
        
        # retorna False se não achou
        return False


def testar_conjunto(arquivo, nome):
    # lê o arquivo
    valores = []
    try:
        with open(arquivo, 'r') as f:
            for linha in f:
                valores.append(int(linha.strip()))
    except:
        print(f"Erro ao ler {arquivo}")
        return
    
    print(f"\n=== {nome} ({len(valores)} entradas) ===")
    
    # cria as estruturas
    lista = Lista()
    arvore = Arvore()
    
    # construção
    inicio = time.perf_counter()
    for valor in valores:
        lista.inserir(valor)
    tempo_lista = time.perf_counter() - inicio
    print(f"Lista construção: {tempo_lista:.6f}s")
    
    inicio = time.perf_counter()
    for valor in valores:
        arvore.inserir(valor)
    tempo_arvore = time.perf_counter() - inicio
    print(f"Árvore construção: {tempo_arvore:.6f}s")
    
    # TESTE 1: Caso aleatório
    valor_aleatorio = valores[len(valores)//2]
    inicio = time.perf_counter()
    lista.buscar(valor_aleatorio)
    tempo_lista_aleatorio = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    arvore.buscar(valor_aleatorio)
    tempo_arvore_aleatorio = time.perf_counter() - inicio
    print(f"Busca aleatória - Lista: {tempo_lista_aleatorio:.6f}s | Árvore: {tempo_arvore_aleatorio:.6f}s")
    
    # TESTE 2: Pior caso (último valor)
    ultimo_valor = valores[-1]
    inicio = time.perf_counter()
    lista.buscar(ultimo_valor)
    tempo_lista_ultimo = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    arvore.buscar(ultimo_valor)
    tempo_arvore_ultimo = time.perf_counter() - inicio
    print(f"Busca último - Lista: {tempo_lista_ultimo:.6f}s | Árvore: {tempo_arvore_ultimo:.6f}s")
    
    # TESTE 3: Valor inexistente
    valor_inexistente = -999999
    inicio = time.perf_counter()
    lista.buscar(valor_inexistente)
    tempo_lista_inexistente = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    arvore.buscar(valor_inexistente)
    tempo_arvore_inexistente = time.perf_counter() - inicio
    print(f"Busca inexistente - Lista: {tempo_lista_inexistente:.6f}s | Árvore: {tempo_arvore_inexistente:.6f}s")

if __name__ == "__main__":
    testar_conjunto("conjuntos/conjunto_pequeno.txt", "CONJUNTO PEQUENO")
    testar_conjunto("conjuntos/conjunto_medio.txt", "CONJUNTO MEDIO")
    testar_conjunto("conjuntos/conjunto_grande.txt", "CONJUNTO GRANDE")
