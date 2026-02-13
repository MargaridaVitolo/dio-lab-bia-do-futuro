# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** R$ 570,00, valor baseado no `transacoes.csv`
- **Resposta obtida:** '''Olá João! Seguindo os dados recentes, você gastou com alimentação no total de R$570,00. Isso inclui: R$450,00 no supermercado (2025-10-03)R$120,00 em restaurantes (2025-10-10)
    Você entendeu? 😊'''
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resposta obtida:** Para construir uma reserva de emergência, é essencial manter o dinheiro  em produtos com alta liquidez e baixo risco, como os Tesuros Selic ou CDBs Liquidez Diária.

    Tesuros Selic: Oferecem juros seguros, equivalentes à taxa de Selic (taxa de juros do governo), e permitem acesso imediato sem penalidades. São ideais para iniciantes que buscam segurança e liquidez rápida.
    CDBs Liquidez Diária: Propõem juros diários, mas exigem um mínimo de R$100 para investimento. São úteis para quem deseja ganhar rendimento rápido sem comprometer a acessibilidade do dinheiro.
    Evite produtos com prazos longos (como LCI/LCA), pois podem não ser acessíveis imediatamente em caso de necessidade. Dado seu perfil moderado, ambos os produtos mencionados são adequados para garantir segurança e liquidez, sem comprometer a finalidade da reserva de emergência.

    Lembre-se: a reserva de emergência deve ser mantida em conta de liquidez, não em investimentos com risco ou prazos longos.
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resposta obtida:** Lamento, mas não posso fornecer previsões do tempo. Meu foco é ajudar com assuntos de finanças. Quer saber como construir sua reserva de emergência ou outras dicas financeiras? 😊
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto ITUB4?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resposta obtida:** Desculpe, João. O produto ITUB4 não está listado nos produtos    financeiros disponíveis para você (como CDBs, Tesouro Selic, LCI/LCA, etc.). O ITUB4 é um   código de ticker para ações da Itaú Unibanco no mercado brasileiro, mas não é um produto de    investimento que oferecemos aqui — nossa lista está focada em opções seguras e adequadas para resgate rápido, como a sua reserva de emergência.

    Para ajudar você a construir sua reserva com segurança, posso explicar como os produtos que estão disponíveis rendem (por exemplo, Tesouro Selic ou CDB Liquidez Diária). Deseja saber mais sobre algum desses? 😊
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, as conclusões foram:

**O que funcionou bem:**
- Os retornos dos testes sairam conforme o esperado. Não houveram alucinações e o comportamento da analista AnaLis foi adequado.
- Foi necessário ajustar o prompt para que as respostas fossem sempre em português.

**O que pode melhorar:**
- Ao fazer uma pergunta simples, o agente estava trazendo muito mais informações do que foi solicitado. Esse ajuste foi feito alterando o prompt.

