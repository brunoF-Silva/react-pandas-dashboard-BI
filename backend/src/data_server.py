import pandas as pd

cached_df = None

def read_df():

    global cached_df

    if(cached_df is None):
        cached_df = pd.read_excel('./franqueados.xlsx', sheet_name='Pagina1')

        cached_df.columns = cached_df.columns.str.lower().str.replace('ç', 'c').str.replace('ã', 'a').str.replace(' ', '_')

        cached_df['data_da_solicitacao'] = pd.to_datetime(cached_df['data_da_solicitacao'])
        cached_df['data_de_entrega'] = pd.to_datetime(cached_df['data_de_entrega'])

        cached_df.dropna()

    return cached_df