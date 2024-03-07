import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('dadosFIIs_atual.xlsx')
df_datas = pd.read_csv("DadosArrec.csv")


df.head(10)

df_renomeado = df.rename(columns={'Setor':'TIPO_FUNDO', 'Codigo do fundo': 'CODIGO'})

qtd_linhas, qtd_colunas = df.shape

colunas = df.columns

tipo_dados = df.dtypes

df.tail(20)

desc_df = df.describe()

dados_unicos = df['TIPO_FUNDO'].unique()

dados_filtrados = df.loc[df['TIPO_FUNDO'] == 'SHOPPINGS']

grupoby_dados_valores = df.groupby('TIPO_FUNDO')['CODIGO'].unique()
grupoby_dados_contagem = df.groupby('TIPO_FUNDO')['CODIGO'].nunique()

grupoby_dados_media = df.groupby('TIPO_FUNDO')['Preço Atual'].mean()

merge_dados = pd.merge(grupoby_dados_contagem, grupoby_dados_media, how='left', on='TIPO_FUNDO')


df1 = df.head(100).tail(20)

df2 = df.tail(100).head(20)

df_junto = pd.concat([df1, df2])

amostra = df_junto.sample(10)

val_nulos = df.isnull().sum()

df['DY Patrimonial'].fillna(0, inplace=True)

df.dropna(subset='Preço Atual',inplace=True)

df['VAL_MULT'] = df['Preço Atual'].mul(3)

df['VAL_MULT'].max()
df['VAL_MULT'].min()

df.nlargest(10, 'Ultimo Dividendo')
df.nlargest(10, 'DY (12M) Acumulado')
df.nsmallest(10, 'Ultimo Dividendo')


df.sort_values('DY (12M) Acumulado', ascending=False).head(10)

df_datas.head(10)

df_datas.dtypes

df_datas['DATA_REFERENCIA_FATURA'] = pd.to_datetime(df_datas['DATA_REFERENCIA_FATURA']) 


df_datas['DATA_BAIXA'] = pd.to_datetime(df_datas['DATA_BAIXA'])
df_datas['DATA_PAGAMENTO'] = pd.to_datetime(df_datas['DATA_PAGAMENTO'])
df_datas['DATA_CREDITO'] = pd.to_datetime(df_datas['DATA_CREDITO'])
df_datas['DATA_VENCIMENTO'] = pd.to_datetime(df_datas['DATA_VENCIMENTO'])

df_datas.groupby(df_datas['DATA_REFERENCIA_FATURA'].dt.year)['A_VALOR_PAGO'].sum()

df_datas['ANO_REF'] = df_datas['DATA_REFERENCIA_FATURA'].dt.year

df_datas['DATA_REFERENCIA_FATURA'].min()
df_datas['DATA_REFERENCIA_FATURA'].max()

df_datas['DIF_REF'] = df_datas['DATA_REFERENCIA_FATURA'] - df_datas['DATA_REFERENCIA_FATURA'].min()
df_datas['TRIMESTRE_REF'] = df_datas['DATA_REFERENCIA_FATURA'].dt.quarter



df_datas['ANO_REF'].value_counts(ascending=False).plot.bar()

df_datas['ANO_REF'].value_counts(ascending=False).plot.barh()

df_datas.groupby(df_datas['DATA_REFERENCIA_FATURA'].dt.year)['A_VALOR_PAGO'].sum().plot.pie()

df_datas['BANCO'].value_counts().plot.bar(title='Total vendas por banco', color='green')

plt.xlabel('Banco')

plt.ylabel('Total contas pagas')

plt.style.use('ggplot')

df_datas['TIPO ARREC'].value_counts().plot.bar(title='Total vendas por banco', color='green')

plt.xlabel('Tipo arrecadacao')

plt.ylabel('Total contas pagas')

df_datas['BANCO'].value_counts().plot(title='Total vendas por banco', color='green')
plt.xlabel('Banco')

plt.ylabel('Total contas pagas')


df_datas.groupby(df_datas['DATA_REFERENCIA_FATURA'].dt.year)['A_VALOR_PAGO'].sum().plot(marker='v')
plt.xlabel('Referencia Fat')

plt.ylabel('Total arrecadado')
plt.legend()

plt.hist(df_datas['BANCO'])


plt.scatter(df_datas['DATA_REFERENCIA_FATURA'],y=df_datas['A_VALOR_PAGO'])

plt.savefig('imagem_grafico.png')

