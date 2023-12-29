import streamlit as st 
import pickle

# ------ DICIONÁRIOS ------

# Os modelos fazem uso de números, logo, um dicionário para a conversão é necessário antes de prever os resultados.
TRADUCAO_CAMPOS = {
    "Sim": 1,
    "Não": 0,
    "Urbana": 0,
    "Rural": 1,
    "Nunca Fumou": 0, 
    "Já Fumou no Passado": 1, 
    "Atualmente Fumante": 2,
    "Sem Dor": 0, 
    "Dor Mínima, quase imperceptível": 1, 
    "Dor Leve, perceptível": 2,
    "Dor Moderada, desconfortável": 3, 
    "Dor Intensa, insumportável": 4
}

# A resposta do modelo também deve ser convertida.
TRADUCAO_RESULTADOS = {
    0: "Verde",
    1: "Amarelo",
    2: "Laranja",
    3: "Vermelho"
}



# ------ FUNÇÕES ------

# Gera erro com a versão mais nova do Scikit (1.3.2). Mudando para a 1.2.2
def triagem_incompleta(nome, idade, hipertensao, historico, residencia, fumante, dor, angina, imc, pressao):
    modelo = pickle.load(open("modelos/modelo_limitado.sav", "rb"))
    resultado = modelo.predict([[idade, TRADUCAO_CAMPOS[dor], pressao, TRADUCAO_CAMPOS[angina], imc, 
                                 TRADUCAO_CAMPOS[hipertensao], TRADUCAO_CAMPOS[historico], TRADUCAO_CAMPOS[residencia], 
                                 TRADUCAO_CAMPOS[fumante]]])
    st.session_state["pacientes"].append({"Nome": nome, "Triagem": TRADUCAO_RESULTADOS[resultado[0]], "Value": resultado[0]})

def triagem_completa(nome, idade, hipertensao, historico, residencia, fumante, dor, angina, imc, pressao, glucose, colesterol, insulina, frequencia_max, grossura):
    modelo = pickle.load(open("modelos/modelo_completo.sav", "rb"))
    resultado = modelo.predict([[idade, TRADUCAO_CAMPOS[dor], pressao, colesterol, frequencia_max, 
                                 TRADUCAO_CAMPOS[angina], glucose, grossura, insulina, imc, TRADUCAO_CAMPOS[hipertensao], 
                                 TRADUCAO_CAMPOS[historico], TRADUCAO_CAMPOS[residencia], TRADUCAO_CAMPOS[fumante]]])
    st.session_state["pacientes"].append({"Nome": nome, "Triagem": TRADUCAO_RESULTADOS[resultado[0]], "Value": resultado[0]})



# ------ MODELOS ------
aba_modelo_incompleto, aba_modelo_completo = st.tabs(["Modelo Incompleto", "Modelo Completo"])

with aba_modelo_incompleto:
    st.header("Modelo Incompleto")
    st.write("Para casos aonde não existe tempo para a coleta de dados por exames.")

    coluna_incompleto_01, coluna_incompleto_02 = st.columns(2)

    with coluna_incompleto_01:
        st.subheader("Dados Pessoais")
        nome = st.text_input("Nome do Paciente")
        idade = st.number_input("Idade do Paciente", 0, 120)
        hipertensao = st.radio("Paciente Hipertenso?", ["Sim", "Não"])
        historico = st.radio("Já teve Doença Cardiáca", ["Sim", "Não"])
        residencia = st.radio("Mora em Zona", ["Urbana", "Rural"])
        fumante = st.radio("Fumante?", ["Nunca Fumou", "Já Fumou no Passado", "Atualmente Fumante"])
    
    with coluna_incompleto_02:
        st.subheader("Análise Preliminar")
        dor = st.radio("Sente Dor no Peito?", ["Sem Dor", "Dor Mínima, quase imperceptível", "Dor Leve, perceptível", 
                                               "Dor Moderada, desconfortável", "Dor Intensa, insumportável"])
        angina = st.radio("Sintomas de Angina?", ["Sim", "Não"])
        imc = st.number_input("IMC", 0.0, 50.0)
        pressao = st.number_input("Pressão Sanguínea", 0.0, 300.0)
    
    if st.button("Enviar para Triagem"):
        triagem_incompleta(nome, idade, hipertensao, historico, residencia, fumante,
                           dor, angina, imc, pressao)
        



with aba_modelo_completo:
    st.header("Modelo Completo")
    st.write("Para casos aonde se possui o tempo necessário para análise. Maior acurácia.")

    coluna_completo_01, coluna_completo_02, coluna_completo_03 = st.columns(3)

    # Infelizmente, o Streamlit não permite inputs iguais sem uma "key" específica.
    # Nesse caso, adotei completo_ + descrição do dado coletado como key.
    with coluna_completo_01:
        st.subheader("Dados Pessoais")
        nome = st.text_input("Nome do Paciente", key="completo_nome")
        idade = st.number_input("Idade do Paciente", 0, 120, key="completo_idade")
        hipertensao = st.radio("Paciente Hipertenso?", ["Sim", "Não"], key="completo_hipertensao")
        historico = st.radio("Já teve Doença Cardiáca", ["Sim", "Não"], key="completo_historico")
        residencia = st.radio("Mora em Zona", ["Urbana", "Rural"], key="completo_residencia")
        fumante = st.radio("Fumante?", ["Nunca Fumou", "Já Fumou no Passado", "Atualmente Fumante"], key="completo_fumante")
    
    # Aqui não é necessário a key, já que são inputs novos.
    with coluna_completo_02:
        st.subheader("Detalhes de Exame")
        glucose = st.number_input("Glucose Plasmática (mmol/L)", 0.0, 300.0)
        colesterol = st.number_input("Nível de Colesterol Total (mg/dL)", 0.0, 500.0)
        insulina = st.number_input("Insulina (µU/mL)", 0.0, 300.0)
        frequencia_max = st.number_input("Frequência Cardiáca Máxima (bpm)", 0, 300)
        grossura = st.number_input("Grossura da Pele (mm)", 0.0, 200.0)
    
    with coluna_completo_03:
        st.subheader("Análise Preliminar")
        dor = st.radio("Sente Dor no Peito?", ["Sem Dor", "Dor Mínima, quase imperceptível", "Dor Leve, perceptível", 
                                               "Dor Moderada, desconfortável", "Dor Intensa, insumportável"], key="completo_dor")
        angina = st.radio("Sintomas de Angina?", ["Sim", "Não"], key="completo_angina")
        imc = st.number_input("IMC", 0.0, 50.0, key="completo_imc")
        pressao = st.number_input("Pressão Sanguínea", 0.0, 300.0, key="completo_pressao")
    
    if st.button("Enviar para Triagem", key="completo_triagem"):
        triagem_completa(nome, idade, hipertensao, historico, residencia, fumante,
                         dor, angina, imc, pressao, glucose, colesterol, insulina,
                         frequencia_max, grossura)
