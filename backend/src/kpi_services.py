import pandas as pd
from typing import Dict, Any

class BaseKpiStrategy:
    @classmethod
    def calculate(cls, df: pd.DataFrame, year: int) -> Dict[str, Any]:
        raise NotImplementedError("As subclasses devem implementar este método")

    @classmethod
    def _empty_payload(cls, kpi_id: int, title: str) -> Dict[str, Any]:
        return {'id': kpi_id, 'title': title, 'cur_value': 0, 'charts': {}}
    
    @classmethod
    def _calculate_yoy(cls, cur_value: float, prev_value: float):
        if prev_value == 0:
            return 100.0 if cur_value > 0 else 0.0
        return round(((cur_value - prev_value) / prev_value) * 100, 2)

class SolicitacoesKpi(BaseKpiStrategy):
    @classmethod
    def calculate(cls, df: pd.DataFrame, year: int) -> Dict[str, Any]:
        prev_year = year - 1
        cur_df = df.query("data_da_solicitacao.dt.year == @year")
        prev_df = df.query("data_da_solicitacao.dt.year == @prev_year")
        
        if cur_df.empty:
             return cls._empty_payload(1, 'Total de Itens Solicitados')
            
        cur_value = int(cur_df['quantidade_solicitada'].sum())
        prev_value = int(prev_df['quantidade_solicitada'].sum()) if not prev_df.empty else 0
        yoy_growth = cls._calculate_yoy(cur_value, prev_value)
        
        tendencia_mensal = cur_df.groupby(cur_df['data_da_solicitacao'].dt.month)['quantidade_solicitada'].sum()
        
        if not prev_df.empty:
            prev_tendencia_mensal = prev_df.groupby(prev_df['data_da_solicitacao'].dt.month)['quantidade_solicitada'].sum()
        else:
            prev_tendencia_mensal = pd.Series(dtype=float)
            
        ranking_filiais = cur_df.groupby('filial')['quantidade_solicitada'].sum().sort_values(ascending=False)
        
        return {
            'id': 1,
            'title': 'Total de Itens Solicitados',
            'cur_value': cur_value,
            'yoy_growth': yoy_growth,
            'charts': {
                'linha_mensal': {
                    'x_keys': tendencia_mensal.reindex(range(1, 13), fill_value=0).index.tolist(),
                    'cur_y_keys': tendencia_mensal.reindex(range(1, 13), fill_value=0).tolist(),
                    'prev_y_keys': prev_tendencia_mensal.reindex(range(1, 13), fill_value=0).tolist(),
                    'cur_legend': year,
                    'prev_legend': prev_year,
                },
                'barra_filiais': {
                    'x_keys': ranking_filiais.index.tolist(),
                    'cur_y_keys': ranking_filiais.tolist(),
                }
            }
        }

class FaturadosKpi(BaseKpiStrategy):
    @classmethod
    def calculate(cls, df: pd.DataFrame, year: int) -> Dict[str, Any]:
        prev_year = year - 1
        cur_df = df.query("data_da_solicitacao.dt.year == @year")
        prev_df = df.query("data_da_solicitacao.dt.year == @prev_year")
        
        if cur_df.empty:
             return cls._empty_payload(2, 'Total de Itens Faturados')
            
        cur_value = int(cur_df['faturados'].sum())
        prev_value = int(prev_df['faturados'].sum()) if not prev_df.empty else 0
        yoy_growth = cls._calculate_yoy(cur_value, prev_value)
        
        tendencia_mensal = cur_df.groupby(cur_df['data_da_solicitacao'].dt.month)['faturados'].sum()
        
        if not prev_df.empty:
            prev_tendencia_mensal = prev_df.groupby(prev_df['data_da_solicitacao'].dt.month)['faturados'].sum()
        else:
            prev_tendencia_mensal = pd.Series(dtype=float)
            
        ranking_filiais = cur_df.groupby('filial')['faturados'].sum().sort_values(ascending=False)
        
        return {
            'id': 2,
            'title': 'Total de Itens Faturados',
            'cur_value': cur_value,
            'yoy_growth': yoy_growth,
            'charts': {
                'linha_mensal': {
                    'x_keys': tendencia_mensal.reindex(range(1, 13), fill_value=0).index.tolist(),
                    'cur_y_keys': tendencia_mensal.reindex(range(1, 13), fill_value=0).tolist(),
                    'prev_y_keys': prev_tendencia_mensal.reindex(range(1, 13), fill_value=0).tolist(),
                    'cur_legend': year,
                    'prev_legend': prev_year,
                },
                'barra_filiais': {
                    'x_keys': ranking_filiais.index.tolist(),
                    'cur_y_keys': ranking_filiais.tolist(),
                }
            }
        }