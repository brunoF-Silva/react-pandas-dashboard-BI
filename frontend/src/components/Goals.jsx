import Card from './ui/Card'

function Goals({goals}) {
  return (
    <section className="grid p-5 justify-center w-full space-x-3" style={{gridTemplateColumns: 'repeat(auto-fit, 250px)'}}>
        {goals.map((goal)=>(
            <Card 
            key={goal.id}
            id={goal.id}
            description={goal.description}
            outcome={goal.is_met}
            onCardClick={() =>  null}/>
        ))}
    </section>
  )
}

export default Goals