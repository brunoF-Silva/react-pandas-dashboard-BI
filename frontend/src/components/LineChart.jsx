import React from 'react'
import { Line } from 'react-chartjs-2'
import 'chart.js/auto'

function LineChart({ curLegend, prevLegend, xKeys, curYKeys, prevYKeys }) {
  const data = {
    labels: xKeys,
    datasets: [
      {
        label: String(curLegend),
        data: curYKeys,
        borderColor: 'rgba(54, 162, 235, 1)',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        tension: 0.2,
      },
      {
        label: String(prevLegend),
        data: prevYKeys,
        borderColor: 'rgba(255, 99, 132, 1)',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        tension: 0.2,
      },
    ],
  }

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top',
      },
    },
  }

  return (
    <div className='w-[90%] h-[350px]'>
      <Line data={data} options={options} />
    </div>
  )
}

export default LineChart