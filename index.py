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

st.subheader("Lista de Chamados")
if len(st.session_state.chamados) ==0:
    st.warning("Nenhum chamado aberto!")
else:
    for i,chamado in enumerate (st.session_state.chamados):
        st.write(f"{chamado['Título']}")
        st.write(f"Descrição: {chamado['Descrição']}")
        st.write(f"Status: {chamado['Status']}")

#ALTERAR STATUS
        novo_status = st.selectbox(
            "Alterar Status",
            ["Aberto","Em andamento","Finalizado"],
            key=f"status{i}"
        )
        #BOTÃO PARA ALTERAR
        if st.button("Atualizar Status", key=f"btn{i}"):
            st.session_state.chamados[i]["Status"]=novo_status
            st.success("Status Atualizado!")
            st.rerun()
        st.divider()
        
