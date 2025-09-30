# Relatório Técnico - Comparação de Estruturas de Dados

## Análise Experimental: Lista Normal vs Lista Otimizada vs Árvore Binária

### Resumo Executivo

Este relatório apresenta uma análise comparativa de três estruturas de dados implementadas: Lista Normal (busca linear), Lista Otimizada (busca binária com ordenação) e Árvore Binária. Os testes foram realizados com conjuntos de dados de 100.000, 5.000.000 e 30.000.000 elementos, executando 5 repetições para cada cenário.

### Metodologia

Foram implementadas três estruturas de dados:
- **Lista Normal**: Inserção O(1), busca linear O(n)
- **Lista Otimizada**: Inserção O(1), ordenação merge sort O(n log n), busca binária O(log n)
- **Árvore Binária**: Inserção O(log n), busca O(log n)

Cada estrutura foi testada com três cenários de busca: valor no meio da estrutura, último valor inserido e valor inexistente.

### Resultados Experimentais

#### Tabela 1: Tempos Médios de Execução (5 repetições)

| Estrutura | 100k Construção | 100k Busca | 5M Construção | 5M Busca | 30M Construção | 30M Busca |
|-----------|----------------|-------------|---------------|----------|----------------|-----------|
| Lista Normal | 0.012535s | 0.002907s | 0.448908s | 0.113257s | 2.691840s | 0.859188s |
| Lista Otimizada | 0.014195s | 0.583902s* | 0.510926s | 31.690071s* | 3.075158s | 222.361537s* |
| Árvore Binária | 0.489208s | 0.000006s | 28.843344s | 0.000010s | 215.364682s | 0.000013s |

*Primeira busca incluindo tempo de ordenação

#### Análise por Conjunto de Dados

**Conjunto Pequeno (100.000 valores)**

Construção:
- Lista Normal: 0.012535s (mais rápida)
- Lista Otimizada: 0.014195s (13% mais lenta)
- Árvore Binária: 0.489208s (39x mais lenta)

Busca:
- Lista Normal: 0.002907s
- Lista Otimizada: 0.583902s (primeira) / 0.000008s (subsequentes)
- Árvore Binária: 0.000006s (mais rápida)

**Conjunto Médio (5.000.000 valores)**

Construção:
- Lista Normal: 0.448908s (mais rápida)
- Lista Otimizada: 0.510926s (14% mais lenta)
- Árvore Binária: 28.843344s (64x mais lenta)

Busca:
- Lista Normal: 0.113257s
- Lista Otimizada: 31.690071s (primeira) / 0.000015s (subsequentes)
- Árvore Binária: 0.000010s (mais rápida)

**Conjunto Grande (30.000.000 valores)**

Construção:
- Lista Normal: 2.691840s (mais rápida)
- Lista Otimizada: 3.075158s (14% mais lenta)
- Árvore Binária: 215.364682s (80x mais lenta)

Busca:
- Lista Normal: 0.859188s
- Lista Otimizada: 222.361537s (primeira) / 0.000018s (subsequentes)
- Árvore Binária: 0.000013s (mais rápida)

### Análise de Complexidade

**Construção:**
1. Lista Normal: Sempre mais eficiente
2. Lista Otimizada: 13-14% 
3. Árvore Binária: Significativamente mais lenta

**Busca:**
1. Árvore Binária: Performance constante O(log n)
2. Lista Otimizada: Eficiente após ordenação inicial
3. Lista Normal: Degrada linearmente O(n)

### Padrões de Escalabilidade

**Lista Normal**: Apresenta degradação linear conforme esperado pela complexidade O(n). O tempo de busca cresce proporcionalmente ao tamanho dos dados.

**Lista Otimizada**: Demonstra queda significativo entre custo inicial de ordenação e eficiência de buscas subsequentes. A ordenação merge sort O(n log n) domina o tempo da primeira busca.

**Árvore Binária**: Mantém performance logarítmica consistente, confirmando a complexidade teórica O(log n) para buscas.

### Ponto de Virada

A análise experimental identificou que a Árvore Binária se torna superior para buscas a partir de 100.000 elementos. Para volumes menores, a Lista Normal pode ser mais eficiente devido à menor sobrecarga.

### Recomendações Técnicas

**Lista Normal:**
- Indicada para conjuntos pequenos (< 100k elementos)
- Cenários com poucas operações de busca
- Quando velocidade de construção é prioritária

**Lista Otimizada:**
- Adequada quando múltiplas buscas (> 10) justificam o custo de ordenação
- Conjuntos médios (100k - 5M elementos)
- Cenários onde busca binária compensa a sobrecarga inicial

**Árvore Binária:**
- Recomendada para conjuntos grandes (> 1M elementos)
- Aplicações com buscas frequentes
- Quando performance de busca é crítica

### Conclusões

Os resultados experimentais confirmam as complexidades teóricas das estruturas implementadas. A Árvore Binária demonstrou superioridade consistente para operações de busca em grandes volumes de dados, enquanto a Lista Normal mantém vantagem na construção. A Lista Otimizada apresenta um trade-off interessante, sendo vantajosa apenas em cenários específicos com múltiplas buscas após a construção inicial.

O ponto de virada identificado (100k elementos) fornece uma diretriz prática para seleção da estrutura de dados mais adequada conforme o volume de dados e padrão de uso da aplicação.