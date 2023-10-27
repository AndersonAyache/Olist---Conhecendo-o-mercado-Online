def verificacao_de_valores(df):
    for coluna in df.columns:

        print('#' * 10 + ' Verificando os valores ' + '#' * 10)
        print('\n')

        print(f'coluna { coluna.upper()}')
        print('\n')
        
        print('-' * 10 + ' Valores unicos ' + '-' * 10)
        print(f'Coluna: *{coluna}* - >{df[coluna].unique()}\n')

    
        print('-' * 10 + ' Contand os Valores ' + '-' * 10)
    
        print(f'{coluna} contagem -> {df[coluna].value_counts()}\n')
    
        if '' in  df[coluna].unique():
            print(f'A Coluna {coluna} possui valores vazios')
        else:
            print(f'A coluna {coluna} NÃO tem valores vazios')

        print('\n')