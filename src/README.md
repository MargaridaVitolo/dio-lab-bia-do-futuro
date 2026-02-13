# 👩🏼‍💻 AnaLis - Analis(ta) Financeira Estratégica

Este projeto contém o código do seu agente financeiro inteligente, a **AnaLis**. Ela foi desenvolvida para fornecer orientações assertivas sobre planejamento financeiro, reserva de emergência e alocação de recursos, utilizando dados reais do cliente para simulações e análises estratégicas.

---

## 🏗️ Estrutura Sugerida

O projeto está organizado para suportar diferentes motores de IA (Local e Nuvem) e manter a separação de dados:

* **app_Ollama.py**: Aplicação principal utilizando o modelo local `qwen3:4b` via API Ollama.
* **app_Gemini.py**: Aplicação utilizando o modelo `gemini-1.5-flash` da Google Generative AI.
* **data/**: Pasta contendo as bases de dados em CSV e JSON (transações, histórico, perfil e produtos).
* **requirements.txt**: Arquivo com as dependências necessárias para execução.

---

## 🛠️ Requisitos e Dependências

Para rodar a aplicação, você precisará das seguintes bibliotecas:

* `streamlit`: Para a interface de chat.
* `pandas`: Para manipulação dos dados financeiros.
* `requests`: Para comunicação com a API do Ollama.
* `google-generativeai`: Para integração com o modelo Gemini.
* `python-dotenv`: Para gerenciamento de variáveis de ambiente.

---

## 🚀 Como Rodar

### 1. Preparação do Ambiente

``` Instale as dependências necessárias:

Bash
pip install -r requirements.txt 
```

### 2. Escolha o seu Motor de IA

* **Opção A:** Usando Ollama (Local)

        Certifique-se de que o Ollama está rodando em http://localhost:11434 e que o modelo qwen3:4b está instalado.

        Bash:  streamlit run app_Ollama.py

* **Opção B:** Usando Gemini (Nuvem)

        Certifique-se de inserir sua GOOGLE_API_KEY no arquivo app_Gemini.py.

        Bash:   streamlit run app_Gemini.py


## 📊 Dados Utilizados


* A AnaLis baseia suas decisões em quatro fontes de dados principais localizadas na pasta data/:

* Transações: Histórico de movimentações financeiras.

* Histórico de Atendimento: Contexto de conversas passadas.

* Perfil do Investidor: Dados demográficos, patrimônio e objetivos.

* Produtos Financeiros: Catálogo de opções disponíveis para análise.

## ⚖️ Regras de Negócio (System Prompt)


* A AnaLis segue diretrizes rigorosas para garantir a segurança do usuário:

* Não recomenda produtos específicos: Apenas explica como funcionam e faz comparativos.

* Baseada em Dados: Nunca inventa informações financeiras ou nomes de bancos.

* Cálculos Estratégicos: Utiliza juros compostos para simular cenários reais.

* Linguagem Empática: Comunicação acessível e focada no dia-a-dia do investidor.
