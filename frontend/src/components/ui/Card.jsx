import React from 'react'

function Card({id, title, description, yoy_growth, totalValue, outcome, selectedKpi, onCardClick}) {
    let cardColor = Number(outcome)
    const yoyNumber = Number(yoy_growth)

    if(cardColor === 0 ){
        cardColor = 'bg-red-300'
    } else if(cardColor === 1) {
      cardColor = 'bg-green-400'
    } else {
      cardColor = 'bg-slate-600'
    }
    
  return (
    <button className={`flex flex-col justify-center items-center rounded-2xl p-5 m-3 ${cardColor} ${id == selectedKpi ? 'border-2 border-yellow-300' : ''}`}
    onClick={() => onCardClick(id)}>
      <h3>{title}</h3>

      <h4>{description}</h4>

      <span className='flex space-x-2'>
        <h3>{totalValue}</h3>  <p>{yoyNumber > 0 && title && '+'}{yoyNumber < 0 && title && '-'}{yoy_growth}</p>
      </span>

    </button>
  )
}

export default Card