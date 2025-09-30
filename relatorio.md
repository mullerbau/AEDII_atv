# Relatório de Testes - Lista vs Árvore Binária

## Bateria de Testes Completa

### Conjunto Pequeno (100.000 entradas)
**Construção:**
- Lista: 0.019386s
- Árvore: 0.348383s (18x mais lenta)

**Buscas:**
- Busca aleatória: Lista 0.001021s | Árvore 0.000006s (170x mais rápida)
- Busca último: Lista 0.001811s | Árvore 0.000006s (302x mais rápida)
- Busca inexistente: Lista 0.004588s | Árvore 0.000005s (918x mais rápida)

**Média das Buscas:**
- Lista: 0.002473s | Árvore: 0.000006s
- **Árvore é 463x mais rápida em média**

### Conjunto Médio (5.000.000 entradas)
**Construção:**
- Lista: 0.405190s
- Árvore: 27.112751s (67x mais lenta)

**Buscas:**
- Busca aleatória: Lista 0.079162s | Árvore 0.000011s (7.196x mais rápida)
- Busca último: Lista 0.144424s | Árvore 0.000012s (12.035x mais rápida)
- Busca inexistente: Lista 0.163961s | Árvore 0.000006s (27.327x mais rápida)

**Média das Buscas:**
- Lista: 0.129182s | Árvore: 0.000010s
- **Árvore é 12.918x mais rápida em média**

### Conjunto Grande (30.000.000 entradas)
**Construção:**
- Lista: 2.475556s
- Árvore: 211.136889s (85x mais lenta)

**Buscas:**
- Busca aleatória: Lista 0.664673s | Árvore 0.000015s (44.311x mais rápida)
- Busca último: Lista 1.123663s | Árvore 0.000015s (74.911x mais rápida)
- Busca inexistente: Lista 0.854621s | Árvore 0.000005s (170.924x mais rápida)

**Média das Buscas:**
- Lista: 0.880986s | Árvore: 0.000012s
- **Árvore é 73.415x mais rápida em média**

---

## 🎯 DADOS DESTACADOS

### Eficiência Média de Busca:
- **100k entradas**: Árvore **463x mais rápida**
- **5M entradas**: Árvore **12.918x mais rápida**
- **30M entradas**: Árvore **73.415x mais rápida**

### Tempo Médio de Busca:
- **Lista 100k**: 0.002473s → **Lista 5M**: 0.129182s → **Lista 30M**: 0.880986s
- **Árvore 100k**: 0.000006s → **Árvore 5M**: 0.000010s → **Árvore 30M**: 0.000012s

### 📈 **ESCALA DRAMÁTICA:**
- **Lista**: Cresce 356x (0.002s → 0.88s)
- **Árvore**: Cresce apenas 2x (0.000006s → 0.000012s)

---

## Análise dos Resultados

### Padrões Identificados:
1. **Lista**: Tempo de busca cresce com posição do elemento
2. **Árvore**: Tempo constante (~0.00001s) independente da posição
3. **Pior caso Lista**: Busca inexistente (percorre toda a lista)
4. **Árvore sempre eficiente**: Mesmo no pior caso mantém performance

### Ponto de Virada:
- **Construção**: Lista sempre mais rápida
- **Busca**: Árvore já é superior com 100k entradas
- **Diferença aumenta**: Com mais dados, vantagem da árvore cresce exponencialmente