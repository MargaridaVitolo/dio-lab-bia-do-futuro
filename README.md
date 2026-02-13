# 🤖 AnaLis: Analis(ta) Financeira Inteligente

## Contexto

AnaLis é uma assistente virtual de nova geração desenvolvida para o setor financeiro. Diferente de chatbots tradicionais, a AnaLis atua como uma consultora proativa, utilizando IA Generativa para transformar dados transacionais em insights acionáveis e planejamento financeiro personalizado.

---

## 🎯 Objetivo do Projeto

Este repositório contém a solução desenvolvida para o desafio BIA do Futuro (DIO), focando na criação de um agente que antecipa necessidades do cliente e garante segurança nas recomendações (anti-alucinação).

---

## 🧠 A Solução: AnaLis

 * A AnaLis foi projetada para resolver o problema da falta de clareza financeira dos usuários, atuando em:

* Análise de Gastos: Identificação automática de padrões e alertas de consumo.

* Consultoria de Investimentos: Sugestões baseadas no perfil individual e produtos disponíveis.

* Planejamento de Metas: Cocriação de estratégias para alcance de objetivos financeiros.

---

## 🏗️ Estrutura da Documentação

O desenvolvimento do projeto foi documentado em etapas detalhadas:

- [Documentação do Agente:](./docs/01-documentacao-agente.md) Definição da Persona, Tom de Voz (Educativo e Seguro) e Arquitetura do fluxo de dados.

- [Base de Conhecimento:](./docs/02-base-conhecimento.md) Estruturação dos dados (Transações, Perfil e Histórico) que alimentam a inteligência da AnaLis.

- [Design de Prompts:](./docs/03-prompts-e-configuracoes.md) Detalhamento do System Prompt e técnicas de Few-Shot Prompting para evitar alucinações.

- [Métricas e Avaliações:](./docs/04-metricas.md) Como foram realizadas as métricas e avaliações do projeto.

- [Pitch de Apresentação:](./docs/05-pitch.md) Proposta de valor e impacto da solução no mercado financeiro.

## 🛠️ Tecnologias Utilizadas

IA Generativa: Modelagem de linguagem para respostas consultivas.

Prompt Engineering: Estruturação de contextos e travas de segurança.

Markdown: Para documentação técnica e estruturada.

---

Este projeto foi desenvolvido como parte do laboratório "BIA do Futuro" na plataforma DIO.

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   ├── app_Ollama.py                 # (Qwen3:4b)
│   └── app_Gemini.py                 # (models/gemini-2.5-flash)

```

---
