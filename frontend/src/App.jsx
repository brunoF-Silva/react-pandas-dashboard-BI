import React, { useEffect, useState } from 'react'
import api from './services/api'
import Kpis from './components/Kpis'
import LineChart from './components/LineChart'
import Goals from './components/Goals'


function App() {
  const [kpis, setKpis] = useState(null)
  const [kpi, setKpi] = useState(null)
  const [selectedKpi, setSelectedKpi] = useState(1)
  const [goals, setGoals] = useState(null)

  const [isLoading, setIsLoading] = useState(true)

  useEffect(()=>{
    async function fetchData(){
      try{
        const [resKpis, resGoals] = await Promise.all([
          api.get('/kpis'),
          api.get(`/goals/${selectedKpi}`),
        ])

        setKpis(resKpis.data.kpis)
        setKpi(resKpis.data.kpis[selectedKpi - 1])

        setGoals(resGoals.data.goals)
        

      } catch(error){
        console.error("An error ocurred: ", error)
      } finally {
        setIsLoading(false)
      }
    }

    fetchData()
  }, [selectedKpi])

  if(isLoading === true){
    return "Loading"
  }

  return (
    <div className="flex flex-col items-center justify-center">
      <h1 className='text-4xl'>Dashboard</h1>

      <Kpis 
      kpis={kpis}
      selectedKpi={selectedKpi}
      onCardClick={setSelectedKpi}/>
      
      <LineChart
        curLegend={kpi.charts.linha_mensal.cur_legend}
        prevLegend={kpi.charts.linha_mensal.prev_legend}
        xKeys={kpi.charts.linha_mensal.x_keys}
        curYKeys={kpi.charts.linha_mensal.cur_y_keys}
        prevYKeys={kpi.charts.linha_mensal.prev_y_keys}
      />


      <Goals
      goals={goals} />

    </div>


  )
}

export default App