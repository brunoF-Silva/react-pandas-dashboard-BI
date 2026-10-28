import Card from './ui/Card'

function Kpis({kpis, selectedKpi, onCardClick}) {
  return (
    <section className="grid p-5 justify-center w-full space-x-3" style={{gridTemplateColumns: 'repeat(auto-fit, 270px)'}}>
        {kpis.map((kpi)=>(
            <Card 
            key={kpi.id}
            id={kpi.id}
            title={kpi.title}
            totalValue={kpi.cur_value}
            yoy_growth={kpi.yoy_growth}
            outcome={5}
            selectedKpi={selectedKpi}
            onCardClick={onCardClick}/>
        ))}
    </section>
  )
}

export default Kpis