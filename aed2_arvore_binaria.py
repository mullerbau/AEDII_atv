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

class Lista_otimizada:
    def __init__(self):
        # cria uma lista vazia com o nome elementos
        self.elementos = []
        self.ordenada = False

    def inserir(self, valor):
        # insere o valor na lista
        self.elementos.append(valor)
        self.ordenada = False

    def _ordenar(self):
        # implementação manual do merge sort
        def merge_sort(lista):
            if len(lista) <= 1:
                return lista
            
            meio = len(lista) // 2
            esquerda = merge_sort(lista[:meio])
            direita = merge_sort(lista[meio:])
            
            # junta as duas metades ordenadas
            resultado = []
            i = j = 0
            
            while i < len(esquerda) and j < len(direita):
                if esquerda[i] <= direita[j]:
                    resultado.append(esquerda[i])
                    i += 1
                else:
                    resultado.append(direita[j])
                    j += 1
            
            # adicionar elementos restantes
            resultado.extend(esquerda[i:])
            resultado.extend(direita[j:])
            return resultado
        
        self.elementos = merge_sort(self.elementos)

    def buscar(self, valor):
        # se a lista não estiver ordenada, ordena antes de buscar
        if not self.ordenada:
            self._ordenar()
            self.ordenada = True

        # busca binária
        baixo = 0
        alto = len(self.elementos) - 1
        while baixo <= alto:
            meio = (baixo + alto) // 2
            if self.elementos[meio] == valor:
                return True
            elif self.elementos[meio] < valor:
                baixo = meio + 1
            else:
                alto = meio - 1
        return False



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


# função para testar lista otimizada vs lista normal
def testar_listas(arquivo):
    # lê o arquivo
    valores = []
    with open(arquivo, 'r') as f:
        for linha in f:
            valores.append(int(linha.strip()))
    
    print(f"Testando {len(valores)} valores")
    
    # cria as estruturas
    lista_normal = Lista()
    lista_otimizada = Lista_otimizada()
    
    # teste construção
    inicio = time.perf_counter()
    for valor in valores:
        lista_normal.inserir(valor)
    print(f"Lista normal construção: {time.perf_counter() - inicio:.6f}s")
    
    inicio = time.perf_counter()
    for valor in valores:
        lista_otimizada.inserir(valor)
    print(f"Lista otimizada construção: {time.perf_counter() - inicio:.6f}s")
    
    # testes de busca
    valor_meio = valores[len(valores)//2]
    valor_ultimo = valores[-1]
    valor_inexistente = -999999
    
    # busca valor do meio
    inicio = time.perf_counter()
    lista_normal.buscar(valor_meio)
    tempo_normal = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    lista_otimizada.buscar(valor_meio)
    tempo_otimizada = time.perf_counter() - inicio
    print(f"Busca meio - Normal: {tempo_normal:.6f}s | Otimizada: {tempo_otimizada:.6f}s")
    
    # busca último valor
    inicio = time.perf_counter()
    lista_normal.buscar(valor_ultimo)
    tempo_normal = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    lista_otimizada.buscar(valor_ultimo)
    tempo_otimizada = time.perf_counter() - inicio
    print(f"Busca último - Normal: {tempo_normal:.6f}s | Otimizada: {tempo_otimizada:.6f}s")
    
    # busca valor inexistente
    inicio = time.perf_counter()
    lista_normal.buscar(valor_inexistente)
    tempo_normal = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    lista_otimizada.buscar(valor_inexistente)
    tempo_otimizada = time.perf_counter() - inicio
    print(f"Busca inexistente - Normal: {tempo_normal:.6f}s | Otimizada: {tempo_otimizada:.6f}s")

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
    

