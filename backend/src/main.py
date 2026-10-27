from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from http import HTTPStatus
from src.kpi_services import SolicitacoesKpi, FaturadosKpi
from src.goal_services import Goal
from src.data_server import read_df
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_headers=['*'],
    allow_methods=['*']
)

df = read_df()

@app.get('/')
def read_root():
    return {'message': 'Rodando'}


@app.get('/api/kips', status_code=HTTPStatus.OK)
def read_kpis():

    solicitacoes_kpi = SolicitacoesKpi.calculate(df, 2026)
    faturados_kpi = FaturadosKpi.calculate(df, 2026)
    return {
        'kpis': [solicitacoes_kpi, faturados_kpi]
    }

@app.get('/api/goals/{id_goal}', status_code=HTTPStatus.OK)
def read_goals(id_goal: int):
    kpi_data = read_kpis()

    cur_kpi = kpi_data['kpis'][id_goal - 1]

    if(id_goal == 1):

        meta_anual_min = Goal(40, 'equal_to', 'Total de itens solicitados deve ser igual a 40')
        meta_anual_esperada = Goal(50, 'greater_than', 'Total de itens solicitados deve ser igual a 50')
        meta_anual_ideal = Goal(60, 'greater_than', 'Total de itens solicitados deve ser maior que 60')

        meta_anual_min.evaluate(cur_kpi['cur_value'])
        meta_anual_esperada.evaluate(cur_kpi['cur_value'])
        meta_anual_ideal.evaluate(cur_kpi['cur_value'])


    elif(id_goal ==2):

        meta_anual_min = Goal(50, 'equal_to', 'Total de itens Faturados deve ser igual a 50')
        meta_anual_esperada = Goal(70, 'greater_than', 'Total de itens Faturados deve ser igual a 70')
        meta_anual_ideal = Goal(80, 'greater_than', 'Total de itens Faturados deve ser maior que 80')

        meta_anual_min.evaluate(cur_kpi['cur_value'])
        meta_anual_esperada.evaluate(cur_kpi['cur_value'])
        meta_anual_ideal.evaluate(cur_kpi['cur_value'])
    else:
        meta_anual_min = {}
        meta_anual_esperada = {}
        meta_anual_ideal = {}      

    return {
        'goals': [meta_anual_min, meta_anual_esperada, meta_anual_ideal]
    }