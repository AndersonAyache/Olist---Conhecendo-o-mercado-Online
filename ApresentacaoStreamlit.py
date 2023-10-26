import streamlit as st
import pandas as pd
import io

clientes = pd.read_csv('dados/olist_customers_dataset.csv')
pedidos  = pd.read_csv('dados/olist_orders_dataset.csv')
itens_pedidos = pd.read_csv('dados/olist_order_items_dataset.csv')
pagamentos = pd.read_csv('dados/olist_order_payments_dataset.csv')
avalicao = pd.read_csv('dados/olist_order_reviews_dataset.csv')
produtos = pd.read_csv('dados/olist_products_dataset.csv')
vendedores = pd.read_csv('dados/olist_sellers_dataset.csv')


st.sidebar.write('Pesquisa 🔍')
with st.sidebar:
    opcao = st.selectbox('DataFrame:', ['Clientes', 'Pedidos', 'Itens por Pedido', 'Pagamentos', 'Avaliação', 'Vendedores'])


def selecionarDf(df):
    if df == "Clientes":
        return clientes
    elif df == "Pedidos":
        return pedidos
    elif df == "Itens por Pedido":
        return itens_pedidos
    elif df == 'Pagamentos':
        return pagamentos
    elif df == 'Avaliação':
        return avalicao
    else:
        return vendedores

with st.container():
    st.subheader('Visualização do DataFrame')
    st.dataframe(selecionarDf(opcao).head(),use_container_width=True)

with st.container():
    with st.container():

        tab1, tab2, tab3 = st.tabs(['Quantidade', 'Colunas', 'Informações'])

        with tab1:
            # Quantidade de linhas e colunas
            st.write(f"O dataframe {opcao} tem:") 
            st.write(f"LINHAS: {selecionarDf(opcao).shape[0]}")
            st.write(f"COLUNAS: {selecionarDf(opcao).shape[1]}")

        with tab2:
            # Monstrando colunas
            st.write('As colunas são:')
            lista = [i for i in selecionarDf(opcao).columns]
            s = ''
            for n in lista:
                s += "- " + n + "\n"
            st.markdown(s)
        with tab3: 
            buffer = io.StringIO()
            selecionarDf(opcao).info(buf=buffer)
            s = buffer.getvalue()
            st.text(s)



