import streamlit as st

st.set_page_config(
    page_title="Calculadora de Lucro Enjoei",
    layout='wide',
    page_icon='random'
)
st.header('**PREÇO DE VENDA**')
valor = float(st.number_input("Digite um valor: ", value=0.00, format="%.2f"))
tarifa_fixa = 0.0
modo = ""

# Opções para o usuário escolher
opcoes = ["Turbinado", "Clássico"]

# Cria o seletor de rádio, permitindo que apenas uma opção seja escolhida
# O "Opção A" será a opção selecionada por padrão
selecao = st.radio("Modo de anúncio:",opcoes, index=0)


if st.button("Calcular"):

    if selecao == "Turbinado":
        modo = "turbinado"
    if selecao == "Clássico":
        modo = "classico"

    if modo == "turbinado":
        if valor <= 0:
            tarifa_fixa = 0
        elif valor <=15:
            tarifa_fixa = 3.5
        elif valor <=30:
            tarifa_fixa = 7.5
        elif valor <=50:
            tarifa_fixa = 8.5
        elif valor <=70:
            tarifa_fixa = 10.5
        elif valor <=100:
            tarifa_fixa = 12.5
        elif valor <=150:
            tarifa_fixa = 16.5
        elif valor <=300:
            tarifa_fixa = 27.5
        elif valor <=500:
            tarifa_fixa = 45
        else:
            tarifa_fixa = 50

        lucro = valor - (valor * 0.18) - tarifa_fixa

        st.write(f"Seu lucro é de: {lucro:.2f}")

        parte_enjoei = valor - lucro

        st.write(f"O enjei ficou com: {parte_enjoei:.2f}")  

    if modo == "classico":
        if valor <= 0:
            tarifa_fixa = 0
        elif valor <=15:
            tarifa_fixa = 2.5
        elif valor <=30:
            tarifa_fixa = 6
        elif valor <=50:
            tarifa_fixa = 6.5
        elif valor <=70:
            tarifa_fixa = 8
        elif valor <=100:
            tarifa_fixa = 10
        elif valor <=150:
            tarifa_fixa = 12.5
        elif valor <=300:
            tarifa_fixa = 21.5
        elif valor <=500:
            tarifa_fixa = 35
        else:
            tarifa_fixa = 40

        lucro = valor - (valor * 0.12) - tarifa_fixa

        st.write(f"Seu lucro é de: {lucro:.2f}")

        parte_enjoei = valor - lucro

        st.write(f"O enjei ficou com: {parte_enjoei:.2f}")



      





