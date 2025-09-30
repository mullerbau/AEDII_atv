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


# função simples para testar um conjunto
def testar_conjunto(arquivo):
    # lê o arquivo
    valores = []
    with open(arquivo, 'r') as f:
        for linha in f:
            valores.append(int(linha.strip()))
    
    print(f"Testando {len(valores)} valores")
    
    # cria as estruturas
    lista = Lista()
    arvore = Arvore()
    
    # teste construção
    inicio = time.perf_counter()
    for valor in valores:
        lista.inserir(valor)
    print(f"Lista construção: {time.perf_counter() - inicio:.6f}s")
    
    inicio = time.perf_counter()
    for valor in valores:
        arvore.inserir(valor)
    print(f"Árvore construção: {time.perf_counter() - inicio:.6f}s")
    
    # testes de busca
    valor_meio = valores[len(valores)//2]
    valor_ultimo = valores[-1]
    valor_inexistente = -999999
    
    # busca valor do meio
    inicio = time.perf_counter()
    lista.buscar(valor_meio)
    tempo_lista = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    arvore.buscar(valor_meio)
    tempo_arvore = time.perf_counter() - inicio
    print(f"Busca meio - Lista: {tempo_lista:.6f}s | Árvore: {tempo_arvore:.6f}s")
    
    # busca último valor
    inicio = time.perf_counter()
    lista.buscar(valor_ultimo)
    tempo_lista = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    arvore.buscar(valor_ultimo)
    tempo_arvore = time.perf_counter() - inicio
    print(f"Busca último - Lista: {tempo_lista:.6f}s | Árvore: {tempo_arvore:.6f}s")
    
    # busca valor inexistente
    inicio = time.perf_counter()
    lista.buscar(valor_inexistente)
    tempo_lista = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    arvore.buscar(valor_inexistente)
    tempo_arvore = time.perf_counter() - inicio
    print(f"Busca inexistente - Lista: {tempo_lista:.6f}s | Árvore: {tempo_arvore:.6f}s")

# exemplo de uso
if __name__ == "__main__":
    print("Teste simples com dados pequenos")
    random.seed(42)
    valores_teste = [random.randint(1, 1000) for _ in range(1000)]
    
    lista = Lista()
    arvore = Arvore()
    
    # construir
    for valor in valores_teste:
        lista.inserir(valor)
        arvore.inserir(valor)
    
    # testar busca
    valor_busca = valores_teste[500]
    
    inicio = time.perf_counter()
    resultado_lista = lista.buscar(valor_busca)
    tempo_lista = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    resultado_arvore = arvore.buscar(valor_busca)
    tempo_arvore = time.perf_counter() - inicio
    
    print(f"Busca valor {valor_busca}:")
    print(f"Lista: {resultado_lista} em {tempo_lista:.6f}s")
    print(f"Árvore: {resultado_arvore} em {tempo_arvore:.6f}s")
