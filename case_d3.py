import streamlit as st 
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

st.image('1_K6z_R8y5owlVNhZE0gvg-g.jpeg')

paginas = ['Pagina inicial', 'Probabilidade do cliente sair','Análise de dados dos tweets sobre covid']
pagina = st.sidebar.radio('Selecione uma página', paginas)

if pagina == 'Pagina inicial':
	st.title("Clientes do banco e Análise dos tweets")
	st.subheader('By Leon Emiliano Benenati')
	st.subheader('Para saber da probabilidade do cliente sair do banco ou ver a análise dos tweets utilize a aba ao lado')
	st.markdown('---')



if pagina == 'Probabilidade do cliente sair':
	st.subheader(' Probabilidade do cliente sair')
	st.subheader('Insira os dados do cliente')
	st.markdown('---')
	Pontuacao_de_credito  = st.slider('Entre com o score de crédito:', 100, 900, 500)
	idade = st.slider('Entre com a idade:', 18, 65, 30)
	tempo_de_conta = st.slider('Entre com a quantidade de anos que o cliente tem conta:', 1,15, 5)
	Saldo = st.number_input('Entre com o saldo do cliente:')
	numeros_de_produto = st.selectbox("Selecione com a quantidade de produtos que o cliente tem", [0, 1, 2, 3, 4])
	cliente_possui_cartao = st.selectbox("O cliente tem cartão?", ['sim', 'não'])
	if cliente_possui_cartao == "sim":
		cliente_possui_cartao = 1
	else:
		cliente_possui_cartao = 0
	cliente_e_ativo = st.selectbox("O cliente é ativo?", ['sim', 'não'])
	if cliente_e_ativo == "sim":
		cliente_e_ativo = 1
	else:
		cliente_e_ativo = 0
	Salario = st.number_input('Entre com o salario do cliente, por favor divida o valor por 100 mil:')
	mora_na_alemanha = st.selectbox("O cliente mora na Alemanha?", ['sim', 'não'])
	if mora_na_alemanha == "sim":
		mora_na_alemanha = 1
	else:
		mora_na_alemanha = 0
	mora_na_espanha = st.selectbox("O cliente mora na Espanha?", ['sim', 'não'])
	if mora_na_espanha == "sim":
		mora_na_espanha = 1
	else:
		mora_na_espanha = 0
	homem = st.selectbox("O cliente é homem?", ['sim', 'não'])
	if homem == "sim":
		homem = 1
	else:
		homem = 0
	

	st.markdown('---')

	dados_dicio = {'CreditScore': [Pontuacao_de_credito],'age': [idade], 'Tenure': [tempo_de_conta], 'Balance': [Saldo], 
			'NumOfProducts': [numeros_de_produto], 'HasCrCard': [cliente_possui_cartao], 'IsActiveMember': [cliente_e_ativo],
			'EstimatedSalary': [Salario],'Geography_Germany': [mora_na_alemanha], 'Geography_Spain': [mora_na_espanha], 
			'Gender_Male': [homem]}

	
	dados = pd.DataFrame(dados_dicio)
	#st.write(dados)

	

	if st.button('CLIQUE AQUI PARA EXECUTAR O MODELO'):
		with open('modelo_escolhido2', 'rb') as f:  
			model = pickle.load(f)
			saida = model.predict(dados)
		

	if saida == 0:
		("Baixa probabilidade de o cliente sair do banco")
	else:
		("Alta probabilidade de o cliente sair do banco")


   
if pagina == 'Análise de dados dos tweets sobre covid':
	st.title("Quantidades de tweets por cada sentimento")
	st.image('sentimentos por tweet.png')
	st.markdown('---')
	st.title("Quantidades de tweets por idiomas")
	st.image('idiomas.png')
	st.markdown('---')
	st.title("Boxplot de palavras por sentimeto")
	st.image('boxplot.png')
	st.markdown('---')
	st.title("Nuvem de palavras")
	st.image('nuvem_total.png')
	st.markdown('---')
	st.title("Nuvem de palavras do sentimento neutro")
	st.image('nuvem_neutro.png')
	st.markdown('---')
	st.title("Nuvem de palavras do sentimento positivo")
	st.image('nuvem_positivo.png')
	st.markdown('---')
	st.title("Nuvem de palavras do sentimento negativo")
	st.image('nuvem_negativo.png')
	st.markdown('---')
	st.title("Nuvem de palavras do sentimento extremamente negativo")
	st.image('nuvem_exnegativo.png')
	st.markdown('---')
	st.title("Nuvem de palavras do sentimento extremamente positivo")
	st.image('nuvem_expositivo.png')
	st.markdown('---')