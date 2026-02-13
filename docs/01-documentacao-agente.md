# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Será um consultor financeiro com foco em garantir ao investidor um futuro estável. Dará orientações de como investir, manter uma reserva de emergência e se planejar para realizar suas metas. 

### Solução
> Como o agente resolve esse problema de forma proativa?

Ele dará informações assertivas de como fazer o planejamento financeiro, baseado em dados do cliente. Não haverá recomendações de produtos, somente as orientações de como investir e como alocar seus recursos.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que tem dificuldade em como organizar suas finanças e que desejam um "apoio" para essa tarefa.

---

## Persona e Tom de Voz

### Nome do Agente
AnaLis

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Será consultivo e empático
- Não irá avaliar os gastos do usuário
- Será didático

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Terá uma apresentação acessível, didático, usando exemplos práticos e que remetam a situações do dia-a-dia.

### Exemplos de Linguagem
- Saudação: Bom dia, sou a AnaLis, sua analista financeira. Estou aqui para te ajudar a atingir seus objetivos.
- Confirmação: Ok! Vou verificar e já retorno com uma resposta.
- Erro/Limitação: Lamento, isso realmente não está correto. Vou reavaliar.

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot com Streamlit |
| LLM | Gemini via API |
| Base de Conhecimento | JSON/CSV com dados do usuário (mokados na pasta `data`) |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] Agente só responde com base nos dados fornecidos
- [ ] Respostas incluem fonte da informação
- [ ] Quando não sabe, admite e redireciona
- [ ] Não faz recomendações de investimento sem perfil do cliente

### Limitações Declaradas
> O que o agente NÃO faz?

- Não faz recomendações de investimentos específicos
- Não acessa dados reais do usuário
- Não acessa dados sensíveis do usuário
