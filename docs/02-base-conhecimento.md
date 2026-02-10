# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anterior ou seja para conhecer melhor o cliente |
| `perfil_investidor.json` | JSON | Personalizar explicações sobre dúvidas do usuário |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para apresentar para o usuário |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações para esclarecer dúvdas |

<!--
> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.
-->
---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Foram incluídos os investimentos em Tesouro Direto.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.
 
Podemos injetar os arquivos diretamente no prompt (CTRL+C / CRTL+V) ou carregar os arquivos via código, como no exemplo abaixo:

```python

import pandas as pd
import json

# CSVs
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSON
with open('data/perfil_investidor.json','r', encoding-útf-8') as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json','r', encoding-útf-8') as f:
  produtos = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados serão usados dinâmicamente, para garantir a flexibilidade do nosso agente.

---

## Exemplo de Contexto Montado

O exemplo abaixo se baseia nos dados originais da base de conhecimento, entretanto os mesmos está otimizado, deixando apenas as informações mais relevantes, minimizando o consumo de tokens. Entretanto vale lembrar que é mais importante ter todas as informações relevantes disponíveis em seu contexto.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Objetivo: Construir reserva de emergência
- Reserva atual: R$ 10.000 (meta: 15.000)

Resumo de Gastos:
- Moradia: R$ 1.380
- Alimentação: R$ 570
- Transporte: R$ 295
- Saúde: R$ 188
- Lazer: R$ 55,90
- Total de Saídas: R$ 2.488,90

Produtos disponíveis para orientação
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Imobiliario - FII (risco médio)
- Fundo de Ações (risco alto)

```
