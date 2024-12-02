import pandas as pd
import streamlit as st
import streamlit_shadcn_ui as ui
from local_components import card_container

#Var
dollar_symbol = '$'

st.set_page_config(layout="wide", page_title="Panel de Facturación", page_icon=":bar_chart:")
st.title("Panel de Facturación")
st.markdown('##')

#read data from CSV
data_previous_year = pd.read_csv("data_2023")
data_actual_year = pd.read_csv("data_2024")

