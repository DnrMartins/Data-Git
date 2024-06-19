import pandas as pd

gasolina_df = pd.read_csv('gasolina.csv', sep=',')
gasolina_df

import seaborn as sns

with sns.axes_style ('whitegrid'):
  grafico_gasolina = sns.lineplot(data=gasolina_df, x='dia', y='venda')
  grafico_gasolina.set(title='Gasolina em São Paulo/SP nos 10 primeiros dias de Julho de 2021', xlabel='Dia', ylabel='Preço')
  grafico_gasolina.get_figure().savefig(f"gasolina.png")
