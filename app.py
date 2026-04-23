import streamlit as st
import pandas as pd
from io import BytesIO

# Configura o título da aba do navegador
st.set_page_config(page_title="Gerenciador de Planilhas", page_icon="📊", layout="centered")

st.title("📊 Gerenciador de Planilhas Web")

# Cria duas abas na página
tab1, tab2 = st.tabs(["📝 Criar Planilha", "🔍 Visualizar Planilha"])

# --- ABA 1: CRIAR PLANILHA ---
with tab1:
    st.header("Nova Planilha")
    
    nome_arquivo = st.text_input("Nome do arquivo (sem .xlsx):", "minha_planilha")
    titulos_str = st.text_input("Digite os nomes das colunas (separados por vírgula):", "Nome, Idade, Cidade")
    
    if titulos_str:
        # Separa os nomes pela vírgula e tira os espaços em branco
        colunas = [c.strip() for c in titulos_str.split(",")]
        
        # Cria um DataFrame vazio com as colunas que o usuário escolheu
        df_base = pd.DataFrame(columns=colunas)
        
        st.write("Adicione seus dados na tabela abaixo (clique na linha vazia para adicionar mais):")
        
        # Cria uma tabela interativa na web onde o usuário pode digitar os dados
        df_editado = st.data_editor(df_base, num_rows="dynamic", use_container_width=True)
        
        # Lógica para converter a tabela da tela em um arquivo Excel na memória
        if not df_editado.empty:
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df_editado.to_excel(writer, index=False, sheet_name="Dados")
            excel_data = output.getvalue()
            
            # Botão de Download
            st.download_button(
                label="📥 Baixar Arquivo Excel",
                data=excel_data,
                file_name=f"{nome_arquivo}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

# --- ABA 2: VISUALIZAR PLANILHA ---
with tab2:
    st.header("Ler Planilha Existente")
    
    # Botão para fazer upload de um arquivo do computador
    arquivo_up = st.file_uploader("Envie um arquivo .xlsx para visualizar", type=["xlsx"])
    
    if arquivo_up is not None:
        try:
            # O Pandas lê o arquivo que foi feito upload
            df_lido = pd.read_excel(arquivo_up)
            st.success("Arquivo carregado com sucesso!")
            
            # Mostra os dados na tela
            st.dataframe(df_lido, use_container_width=True)
        except Exception as e:
            st.error(f"Erro ao ler o arquivo: {e}")
