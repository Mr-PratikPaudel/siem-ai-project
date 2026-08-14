const alerts = [
  {
    id:1,
    time:"10:15 AM",
    ip:"192.168.1.10",
    attack:"Port Scan",
    severity:"High"
  },
  {
    id:2,
    time:"10:20 AM",
    ip:"192.168.1.15",
    attack:"Brute Force",
    severity:"Critical"
  },
  {
    id:3,
    time:"10:30 AM",
    ip:"192.168.1.25",
    attack:"Normal",
    severity:"Low"
  }
];

export default alerts;
import {
Bar
}
from "react-chartjs-2";

import {
Chart as ChartJS,
CategoryScale,
LinearScale,
BarElement
}
from "chart.js";

ChartJS.register(CategoryScale,LinearScale,BarElement);

function ThreatChart(){

const data={

labels:["Port Scan","Brute Force","DoS"],

datasets:[
{
label:"Threats",
data:[15,8,5]
}
]

}

return(

<div>

<h2>Threat Chart</h2>

<Bar data={data}/>
<div className="card">
   <h2>Security Alerts</h2>
</div>

</div>

)

}

export default ThreatChart;