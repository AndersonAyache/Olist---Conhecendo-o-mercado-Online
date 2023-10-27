def verificacao_valores_unicos(df):
    print('Verificando os valores')
    for coluna_v in df.columns:
        print(f'Coluna: *{coluna_v}* - >{df[coluna_v].unique()}\n')

    print('Contando os Valores')
    for coluna_c in df.columns:
        print(f'{coluna_c} contagem -> {df[coluna_c].value_counts()}\n')

def verificar_valor_vazio(df):
    valores_vazios = 0
    for coluna_va in df.columns:
        if ''in  df[coluna_va].unique():
            print(f'A Coluna {coluna_va} possui valores vazios')
        else:
            print(f'A coluna {coluna_va} NÃO tem valores vazios')