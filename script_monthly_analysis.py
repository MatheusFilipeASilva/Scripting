import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

def monthly_analysis(df, value, index, aggfunc, ylabel, xlabel, opcao=None):
    if opcao == None:
        pd.pivot_table(df, values=value, index=index, aggfunc=aggfunc).plot(figsize=(15,5))
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=aggfunc).sort_values(value).plot(figsize = (15,5))
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=aggfunc).unstack().plot(figsize=(15, 5))
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)



meses = sys.argv
print(meses)
for mes in meses[1:]:
    df = pd.read_csv('./SINASC_RO_2019_'+mes+'.csv')

    monthly_analysis(df, 'IDADEMAE', 'DTNASC', 'count', 'idade da mae', 'data de nascimento')
    os.makedirs('./Scripting - Exercicio/'+ mes, exist_ok=True)
    plt.savefig('./Scripting - Exercicio/'+ mes +'/nascidos por dia.png')

    monthly_analysis(df, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe','data de nascimento','unstack')
    plt.savefig('./Scripting - Exercicio/'+ mes +'/media peso bebe por sexo.png')

    monthly_analysis(df, 'PESO', 'ESCMAE', 'median', 'apgar1 medio','gestacao','sort')
    plt.savefig('./Scripting - Exercicio/'+ mes +'/media apgar1 por escolaridade mae.png')

    monthly_analysis(df, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio','gestacao','sort')
    plt.savefig('./Scripting - Exercicio/'+ mes +'/media apgar1 por escolaridade mae.png')

    monthly_analysis(df, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio','gestacao','sort')
    plt.savefig('./Scripting - Exercicio/'+ mes +'/media apgar1 por gestacao')

    monthly_analysis(df, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio','gestacao','sort')
    plt.savefig('./Scripting - Exercicio/'+ mes +'/media apgar5 por gestacao')