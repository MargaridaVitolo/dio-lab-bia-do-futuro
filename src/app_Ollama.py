import json
import pandas as pd
import requests
import streamlit as st


# Configurações
OLLAMA_URL = 'http://localhost:11434/api/generate'
MODELO = 'qwen3:4b'

# Carregar dados
# csv
transacoes = pd.read_csv('/Users/margarida/Documents/DIO/dio-lab-bia-do-futuro/data/transacoes.csv')
historico = pd.read_csv('/Users/margarida/Documents/DIO/dio-lab-bia-do-futuro/data/historico_atendimento.csv')
# json
with open('/Users/margarida/Documents/DIO/dio-lab-bia-do-futuro/data/perfil_investidor.json','r', encoding='utf-8') as f:
  perfil = json.load(f)

with open('/Users/margarida/Documents/DIO/dio-lab-bia-do-futuro/data/produtos_financeiros.json','r', encoding='utf-8') as f:
  produtos = json.load(f)

# Montar contexto

contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R${perfil['patrimonio_total']} | RESERVA: R${perfil['reserva_emergencia_atual']}

TRANSAÇOES RECENTES:
{transacoes.tail(10).to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# System prompt para o modelo

SYSTEM_PROMPT = """
Você é AnaLis, uma analista financeira inteligente especializada em garantir ao investidor um futuro estável. Dará orientações de como investir, manter uma reserva de emergência e se planejar para realizar suas metas.
Seu objetivo é fornecer informações assertivas de como fazer o planejamento financeiro, baseado em dados do cliente. Não haverá recomendações de produtos, somente as orientações de como investir e como alocar seus recursos. Sua cominicação será empática e usará exemplos do dia-a-dia.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Avalie a situação do cliente com base nos dados
5. Oriente de forma estratégica como realizar os objetivos
6. Nunca recomende investimentos específicos - apenas explique como funcionam
7. Faça comparativo entre os investimentos disponíveis
8. Utilize as regras de juros compostos para simular um investimento, utilize os dados do perfil do cliente e a taxa média de juros anuais de mercado, solicite o tempo de permanencia do investimento da aplicação ou o montante final desejado
9. Use uma linguagem acessível e concisa. Sempre confirme com o usuário se ele entendeu.
10. Nunca responda sobre assuntos fora de finanças (ex: previsão do tempo, receitas).
11. Nunca invente nomes de bancos ou taxas que não estão no arquivo JSON.
12. Responda sempre em português de forma clara e empática.
"""

# Chamar o Ollama

def perguntar(msg):
    try:
        prompt = f"""
        {SYSTEM_PROMPT}

        CONTEXTO DO CLIENTE:
        {contexto}

        Pergunta: {msg}
        """

        r = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            }
        )


        r.raise_for_status()
        data = r.json()

        return data.get("response", f"Resposta inesperada: {data}")

    except Exception as e:
        return f"Erro na requisição: {e}"


# Interface


st.set_page_config(page_title="AnaLis - Analis(ta) Virtual", page_icon="👩🏼‍💻")
st.markdown("""
<div style="
    font-size: 2.5em; 
    font-weight: bold; 
    line-height: 1.1; 
    margin-bottom: 1rem;
    white-space: nowrap;
">
    👩🏼‍💻 AnaLis - Analis(ta) Financeira Estratégica
</div>
""", unsafe_allow_html=True)
    
if pergunta := st.chat_input("Em que posso ajudar no seu planejamento hoje?"):
    st.chat_message("user").write(pergunta)
    with st.spinner("AnaLis(ando) dados..."):
       st.chat_message("assistant").write(perguntar(pergunta))
