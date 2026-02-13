import json
import pandas as pd
import streamlit as st
import google.generativeai as genai

# --- CONFIGURAÇÕES DA API ---
# Substitua pela sua chave gerada no Google AI Studio
GOOGLE_API_KEY = "AIzaSyB1WbRoj1JEHdC8C0rGTZHCq-6rWWNwvpA" #"SUA_API_KEY_AQUI" 
genai.configure(api_key=GOOGLE_API_KEY)

# Debug: listar todos os modelos disponíveis
# print("MODELOS DISPONÍVEIS:", [m.name for m in genai.list_models()])

# Usando o modelo gratuito e rápido que discutimos
MODELO = "models/gemini-2.5-flash" 

# --- CARREGAR DADOS ---
try:
    transacoes = pd.read_csv('/Users/margarida/Documents/DIO/dio-lab-bia-do-futuro/data/transacoes.csv')
    historico = pd.read_csv('/Users/margarida/Documents/DIO/dio-lab-bia-do-futuro/data/historico_atendimento.csv')
    
    with open('/Users/margarida/Documents/DIO/dio-lab-bia-do-futuro/data/perfil_investidor.json','r', encoding='utf-8') as f:
        perfil = json.load(f)

    with open('/Users/margarida/Documents/DIO/dio-lab-bia-do-futuro/data/produtos_financeiros.json','r', encoding='utf-8') as f:
        produtos = json.load(f)
except Exception as e:
    st.error(f"Erro ao carregar arquivos: {e}")
    st.stop()

# --- MONTAR CONTEXTO ---
contexto_dados = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R${perfil['patrimonio_total']} | RESERVA: R${perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES (Últimas 10):
{transacoes.tail(10).to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS FINANCEIROS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# --- CONFIGURAÇÃO DO MODELO (SYSTEM PROMPT) ---

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

# Inicializa o modelo com as instruções de sistema
model = genai.GenerativeModel(
    model_name=MODELO,
    system_instruction=SYSTEM_PROMPT
)

def perguntar_gemini(msg):
    try:
        # Criamos o prompt final injetando o contexto de dados
        prompt_completo = f"CONTEXTO DO CLIENTE:\n{contexto_dados}\n\nPERGUNTA DO USUÁRIO: {msg}"
        
        response = model.generate_content(prompt_completo)
        return response.text
    except Exception as e:
        return f"Erro na API Gemini: {e}"

# --- INTERFACE STREAMLIT ---
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

# Inicializar histórico de chat se não existir
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if pergunta := st.chat_input("Em que posso ajudar no seu planejamento hoje?"):
    # Adiciona pergunta ao chat
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)

    # Gera resposta
    with st.chat_message("assistant"):
        with st.spinner("AnaLis(ando) dados..."):
            resposta = perguntar_gemini(pergunta)
            st.markdown(resposta)
            st.session_state.messages.append({"role": "assistant", "content": resposta})