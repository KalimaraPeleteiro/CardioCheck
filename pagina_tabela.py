import streamlit as st 
import pandas as pd

data = {
    "Etiquetas": ["Verde", "Amarelo", "Laranja", "Vermelho"],
    "Descrições": [
        "Menor Prioridade. Problemas que não podem vir a ser fatais, e, consequentemente, podem esperar pelo atendimento de outros.",
        "Problemas sérios aonde atenção imediata é necessária. Em alguns sistemas de triagem, etiquetas amarelas recebem até mesmo prioridade do que casos mais graves, pois são pacientes que podem se recuperar mais rapidamente",
        "Etiqueta criada durante o processo de produção dos modelos para diferenciar casos realmente graves e urgentes de outros exemplos.",
        "Prioridade Máxima. Necessário atenção imediata para sobrevivência."
    ]
}

dataframe = pd.DataFrame(data)

st.header("Etiquetas de Triagem")

st.table(dataframe)