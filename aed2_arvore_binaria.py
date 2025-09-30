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
                    no_atual.esquerda = Node(valor)
                    break
                else:
                    no_atual = no_atual.esquerda

            # se o valor for maior, vai pra direita
            elif valor > no_atual.valor:
                if no_atual.direita is None:
                    no_atual.direita = Node(valor)
                    break
                else:
                    no_atual = no_atual.direita

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


# Exemplos de uso das classes
if __name__ == "__main__":
    print("=== EXEMPLOS DE USO ===")
    
    # Exemplo 1: Lista Normal
    print("\n1. Lista Normal:")
    lista = Lista()
    
    # Inserindo valores
    for valor in [10, 5, 15, 3, 7]:
        lista.inserir(valor)
    print(f"Valores inseridos: [10, 5, 15, 3, 7]")
    
    # Buscando valores
    print(f"Buscar 7: {lista.buscar(7)}")
    print(f"Buscar 20: {lista.buscar(20)}")
    
    # Exemplo 2: Lista Otimizada
    print("\n2. Lista Otimizada:")
    lista_otimizada = Lista_otimizada()
    
    # Inserindo valores
    for valor in [10, 5, 15, 3, 7]:
        lista_otimizada.inserir(valor)
    print(f"Valores inseridos: [10, 5, 15, 3, 7]")
    
    # Primeira busca (ordena automaticamente)
    print(f"Primeira busca 7: {lista_otimizada.buscar(7)}")
    print(f"Segunda busca 20: {lista_otimizada.buscar(20)}")
    
    # Exemplo 3: Árvore Binária
    print("\n3. Árvore Binária:")
    arvore = Arvore()
    
    # Inserindo valores
    for valor in [10, 5, 15, 3, 7, 12, 18]:
        arvore.inserir(valor)
    print(f"Valores inseridos: [10, 5, 15, 3, 7, 12, 18]")
    
    # Buscando valores
    print(f"Buscar 12: {arvore.buscar(12)}")
    print(f"Buscar 25: {arvore.buscar(25)}")
    
    # Exemplo 4: Comparação de Performance
    print("\n4. Teste de Performance (1000 valores):")
    random.seed(42)
    valores_teste = [random.randint(1, 1000) for _ in range(1000)]
    
    # Lista
    lista_teste = Lista()
    inicio = time.perf_counter()
    for valor in valores_teste:
        lista_teste.inserir(valor)
    tempo_lista = time.perf_counter() - inicio
    
    # Árvore
    arvore_teste = Arvore()
    inicio = time.perf_counter()
    for valor in valores_teste:
        arvore_teste.inserir(valor)
    tempo_arvore = time.perf_counter() - inicio
    
    print(f"Construção Lista: {tempo_lista:.6f}s")
    print(f"Construção Árvore: {tempo_arvore:.6f}s")
    
    # Teste de busca
    valor_busca = valores_teste[500]
    
    inicio = time.perf_counter()
    resultado_lista = lista_teste.buscar(valor_busca)
    tempo_busca_lista = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    resultado_arvore = arvore_teste.buscar(valor_busca)
    tempo_busca_arvore = time.perf_counter() - inicio
    
    print(f"Busca Lista: {tempo_busca_lista:.6f}s (resultado: {resultado_lista})")
    print(f"Busca Árvore: {tempo_busca_arvore:.6f}s (resultado: {resultado_arvore})")