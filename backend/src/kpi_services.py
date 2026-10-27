from typing import Dict, Any
import pandas as pd

class BaseKpiStrategy:
    @classmethod
    def calculate(cls, df: pd.DataFrame, year: int) -> Dict[str, Any]:
        raise NotImplementedError("As subclasses devem implementar este método")

    @classmethod
    def _empty_payload(cls, kpi_id: int, title: str) -> Dict[str, Any]:
        return {'id': kpi_id, 'title': title, 'cur_value': 0, 'charts': {}}

class SolicitacoesKpi(BaseKpiStrategy):
    @classmethod
    def calculate(cls, df: pd.DataFrame, year: int) -> Dict[str, Any]:
        cur_df = df.query("data_da_solicitacao.dt.year == @year")
        prev_df = df.query("data_da_solicitacao.dt.year == @year - 1")
        
        if cur_df.empty:
             return cls._empty_payload(4, 'Total de Itens Solicitados')
            
        cur_value = int(cur_df['quantidade_solicitada'].sum())
        
        tendencia_mensal = cur_df.groupby(cur_df['data_da_solicitacao'].dt.month)['quantidade_solicitada'].sum()
        prev_tendencia_mensal = prev_df.groupby(cur_df['data_da_solicitacao'].dt.month)['quantidade_solicitada'].sum()
        ranking_filiais = cur_df.groupby('filial')['quantidade_solicitada'].sum().sort_values(ascending=False)
        
        return {
            'id': 1,
            'title': 'Total de Itens Solicitados',
            'cur_value': cur_value,
            'charts': {
                'linha_mensal': {
                    'x_keys': tendencia_mensal.index.tolist(),
                    'cur_y_keys': tendencia_mensal.tolist(),
                    'prev_y_keys': prev_tendencia_mensal.tolist(),
                    'legend': year,
                },
                'barra_filiais': {
                    'x_keys': ranking_filiais.index.tolist(),
                    'cur_y_keys': ranking_filiais.tolist(),
                    'legend': year,
                }
            }
        }
        

class FaturadosKpi(BaseKpiStrategy):
    @classmethod
    def calculate(cls, df: pd.DataFrame, year: int) -> Dict[str, Any]:
        cur_df = df.query("data_de_entrega.dt.year == @year")
        prev_df = df.query("data_da_solicitacao.dt.year == @year - 1")

        
        if cur_df.empty:
             return cls._empty_payload(4, 'Total de Itens Faturados')
            
        cur_value = int(cur_df['faturados'].sum())
        
        tendencia_mensal = cur_df.groupby(cur_df['data_de_entrega'].dt.month)['faturados'].sum()
        prev_tendencia_mensal = cur_df.groupby(prev_df['data_de_entrega'].dt.month)['faturados'].sum()
        ranking_filiais = cur_df.groupby('filial')['faturados'].sum().sort_values(ascending=False)
        
        return {
            'id': 2,
            'title': 'Total de Itens Faturados',
            'cur_value': cur_value,
            'charts': {
                'linha_mensal': {
                    'x_keys': tendencia_mensal.index.tolist(),
                    'cur_y_keys': tendencia_mensal.tolist(),
                    'prev_y_keys': prev_tendencia_mensal.tolist(),
                    'label': year,
                },
                'barra_filiais': {
                    'x_keys': ranking_filiais.index.tolist(),
                    'cur_y_keys': ranking_filiais.tolist(),
                    'label': year,
                }
            }
        }
        


        