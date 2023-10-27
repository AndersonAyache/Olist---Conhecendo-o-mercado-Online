def verificacao_de_valores(df):
    
    df.info()
    print('\n')

    
    print('Valores nulos:')
    for coluna in df.columns:
        
        print(f'{coluna} -> {df[coluna].isnull().sum()}')

    print('\n')

    for coluna in df.columns:
        print('#'* 10 +' Verificando os valores ' +'#' * 10)
        print('\n')
        print(f'Coluna: {coluna.upper()}')
        print('\n')
    
        print('-' * 10 +' Valores únicos '+'-' * 10)
        print(f'{df[coluna].unique()}\n')

        print('-' * 10 + ' Contando os Valores ' + '-' * 10)
    
        print(f'{df[coluna].value_counts()}\n')

        if df[coluna].isnull().sum() > 0 :
            valores_vazios = df[coluna].isnull().sum()
            print(f'Existem {valores_vazios} valorez vazios.')
        else:
            print('Não existem valores vazios.')


        if '' in  df[coluna].unique():
            print(f'A Coluna {coluna} possui valores em branco')
        else:
            print(f'A coluna {coluna} NÃO tem valores em branco')

        print('\n')