
import "../styles/AnomalyChart.css";
import { LineChart, Line, XAxis, YAxis, Tooltip } from "recharts";



const data = [
  { time: "10:00", score: 20 },
  { time: "10:05", score: 80 },
  { time: "10:10", score: 95 },
  { time: "10:15", score: 40 },
];

function AnomalyChart() {
  return (
    <div className="card">
      <h2>Anomaly Score Trend</h2>

      <LineChart width={500} height={300} data={data}>
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="score" />
      </LineChart>
    </div>
  );
}

export default AnomalyChart;