# Relatório de Testes - Lista vs Árvore Binária

## Resultados Detalhados - 5 Testes por Conjunto

### CONJUNTO PEQUENO (100.000 valores)

**Construção:**
- Teste 1: Lista 0.009484s | Árvore 0.459869s
- Teste 2: Lista 0.015037s | Árvore 0.449922s
- Teste 3: Lista 0.016885s | Árvore 0.457819s
- Teste 4: Lista 0.012202s | Árvore 0.534816s
- Teste 5: Lista 0.009069s | Árvore 0.543616s
- **MÉDIA: Lista 0.012535s | Árvore 0.489208s**

**Busca Meio:**
- Teste 1: Lista 0.003143s | Árvore 0.000010s
- Teste 2: Lista 0.001815s | Árvore 0.000012s
- Teste 3: Lista 0.002443s | Árvore 0.000009s
- Teste 4: Lista 0.001031s | Árvore 0.000005s
- Teste 5: Lista 0.003528s | Árvore 0.000009s
- **MÉDIA: Lista 0.002392s | Árvore 0.000009s**

**Busca Último:**
- Teste 1: Lista 0.001802s | Árvore 0.000007s
- Teste 2: Lista 0.004825s | Árvore 0.000009s
- Teste 3: Lista 0.001801s | Árvore 0.000006s
- Teste 4: Lista 0.001829s | Árvore 0.000004s
- Teste 5: Lista 0.001793s | Árvore 0.000006s
- **MÉDIA: Lista 0.002410s | Árvore 0.000006s**

**Busca Inexistente:**
- Teste 1: Lista 0.001799s | Árvore 0.000003s
- Teste 2: Lista 0.004937s | Árvore 0.000004s
- Teste 3: Lista 0.004263s | Árvore 0.000005s
- Teste 4: Lista 0.004007s | Árvore 0.000005s
- Teste 5: Lista 0.004585s | Árvore 0.000005s
- **MÉDIA: Lista 0.003918s | Árvore 0.000004s**

---

### CONJUNTO MÉDIO (5.000.000 valores)

**Construção:**
- Teste 1: Lista 0.516418s | Árvore 36.132817s
- Teste 2: Lista 0.401282s | Árvore 26.474329s
- Teste 3: Lista 0.470279s | Árvore 26.993535s
- Teste 4: Lista 0.432565s | Árvore 26.352264s
- Teste 5: Lista 0.423994s | Árvore 28.263777s
- **MÉDIA: Lista 0.448908s | Árvore 28.843344s**

**Busca Meio:**
- Teste 1: Lista 0.079802s | Árvore 0.000012s
- Teste 2: Lista 0.076193s | Árvore 0.000013s
- Teste 3: Lista 0.098716s | Árvore 0.000013s
- Teste 4: Lista 0.083889s | Árvore 0.000013s
- Teste 5: Lista 0.108142s | Árvore 0.000013s
- **MÉDIA: Lista 0.089348s | Árvore 0.000013s**

**Busca Último:**
- Teste 1: Lista 0.150333s | Árvore 0.000011s
- Teste 2: Lista 0.127436s | Árvore 0.000013s
- Teste 3: Lista 0.114067s | Árvore 0.000011s
- Teste 4: Lista 0.129446s | Árvore 0.000012s
- Teste 5: Lista 0.136609s | Árvore 0.000013s
- **MÉDIA: Lista 0.131578s | Árvore 0.000012s**

**Busca Inexistente:**
- Teste 1: Lista 0.127860s | Árvore 0.000004s
- Teste 2: Lista 0.118287s | Árvore 0.000004s
- Teste 3: Lista 0.100982s | Árvore 0.000004s
- Teste 4: Lista 0.119524s | Árvore 0.000004s
- Teste 5: Lista 0.127575s | Árvore 0.000004s
- **MÉDIA: Lista 0.118846s | Árvore 0.000004s**

---

### CONJUNTO GRANDE (30.000.000 valores)

**Construção:**
- Teste 1: Lista 2.744320s | Árvore 216.418752s
- Teste 2: Lista 2.930968s | Árvore 222.972578s
- Teste 3: Lista 2.532077s | Árvore 210.031358s
- Teste 4: Lista 2.551620s | Árvore 214.738371s
- Teste 5: Lista 2.700217s | Árvore 212.662351s
- **MÉDIA: Lista 2.691840s | Árvore 215.364682s**

**Busca Meio:**
- Teste 1: Lista 0.453885s | Árvore 0.000016s
- Teste 2: Lista 0.543914s | Árvore 0.000017s
- Teste 3: Lista 0.538019s | Árvore 0.000017s
- Teste 4: Lista 0.611062s | Árvore 0.000016s
- Teste 5: Lista 0.539169s | Árvore 0.000026s
- **MÉDIA: Lista 0.537210s | Árvore 0.000018s**

**Busca Último:**
- Teste 1: Lista 0.978647s | Árvore 0.000014s
- Teste 2: Lista 1.013838s | Árvore 0.000015s
- Teste 3: Lista 1.224775s | Árvore 0.000020s
- Teste 4: Lista 1.193136s | Árvore 0.000014s
- Teste 5: Lista 1.121688s | Árvore 0.000014s
- **MÉDIA: Lista 1.106417s | Árvore 0.000015s**

**Busca Inexistente:**
- Teste 1: Lista 0.781356s | Árvore 0.000005s
- Teste 2: Lista 0.876371s | Árvore 0.000005s
- Teste 3: Lista 1.028684s | Árvore 0.000005s
- Teste 4: Lista 1.053928s | Árvore 0.000005s
- Teste 5: Lista 0.929351s | Árvore 0.000006s
- **MÉDIA: Lista 0.933938s | Árvore 0.000005s**

---

## 🎯 MÉDIAS FINAIS

### Eficiência Média de Busca:
- **100k**: Lista 0.002907s | Árvore 0.000006s (Árvore 484x mais rápida)
- **5M**: Lista 0.113257s | Árvore 0.000010s (Árvore 11.326x mais rápida)
- **30M**: Lista 0.859188s | Árvore 0.000013s (Árvore 66.092x mais rápida)

### Padrão Confirmado:
- **Lista**: Cresce linearmente (0.003s → 0.113s → 0.859s)
- **Árvore**: Mantém constante (~0.00001s)
- **Ponto de virada**: Entre 1k-100k entradas