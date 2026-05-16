import streamlit as st

st.title("Sistema de Chamados")

#CRIAR AS LISTAS DE CHAMADOS

if "chamados" not in st.session_state:
    st.session_state.chamados=[]

#ABRIR CHAMADOS
st.subheader("Abrir Chamado")
titulo=st.text_input("Título do Chamado")
descricao=st.text_area("Descrição de serviço")

#BOTÃO
if st.button("Abrir Chamado"):
    if titulo !=""and descricao!="":
        chamado= {
            "Título": titulo,
            "Descrição":descricao,
            "Status":"Aberto"
        }
        st.session_state.chamados.append(chamado)
        st.success("Chamado aberto com sucesso!")
        



