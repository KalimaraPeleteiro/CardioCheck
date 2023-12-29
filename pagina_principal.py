import streamlit as st


def atualiza_lista():
    pacientes_ordenados = sorted(st.session_state["pacientes"], 
                                 key = lambda dicionario: dicionario["Value"], 
                                 reverse=True)
    for paciente in pacientes_ordenados:
        secao_pacientes.write(f"Paciente {paciente['Nome']} | Triagem: {paciente['Triagem']}")



# ------ CONFIGURAÇÕES DA PÁGINA ------
st.set_page_config(layout="wide")

if 'pacientes' not in st.session_state:
    st.session_state["pacientes"] = []



# ------ CABEÇALHO ------
st.title("Triagem de Pacientes")

st.markdown("Modelo criado fazendo uso de uma [base de dados](https://www.kaggle.com/datasets/hossamahmedaly/patient-priority-classification) do Kaggle.")
st.write("Para começar, faça uso de um dos modelos disponíveis para começar a preencher a lista de pacientes. A triagem é feita sobre o contexto de uma consulta ou emergência cardíaca, e os pacientes são ordenados de acordo com a severidade do caso.")
st.write("Uma descrição de cada caso (retirada do próprio conjunto de dados) está disponível em outra página.")
st.write("")

st.subheader("Lista de Pacientes")
secao_pacientes = st.container()
if st.session_state["pacientes"] == []:
    secao_pacientes.info("A lista de pacientes começa vazia. Faça uso de um modelo para preenchê-la!")
else:
    secao_pacientes.empty()
    atualiza_lista()
