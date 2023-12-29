import streamlit as st
from st_pages import Page, add_page_title, show_pages

show_pages(
    [
        Page("pagina_principal.py", "Lista de Pacientes"),
        Page("pagina_modelos.py", "Modelos de Triagem"),
        Page("pagina_tabela.py", "Etiquetas de Triagem")
    ]
)
