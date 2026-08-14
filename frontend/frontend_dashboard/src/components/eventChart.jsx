import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  BarChart,
  Bar,
  Cell,
} from "recharts";

import "../styles/eventchart.css";


// ALERT TREND DATA

const alertTrend = [
  { time: "10:00", alerts: 12 },
  { time: "11:00", alerts: 18 },
  { time: "12:00", alerts: 9 },
  { time: "13:00", alerts: 25 },
  { time: "14:00", alerts: 17 },
  { time: "15:00", alerts: 32 },
  { time: "16:00", alerts: 21 },
  { time: "17:00", alerts: 40 },
];


// SEVERITY DATA

const severityData = [
  {
    name: "Critical",
    count: 8,
    color: "#ef4444",
  },
  {
    name: "High",
    count: 18,
    color: "#f97316",
  },
  {
    name: "Medium",
    count: 35,
    color: "#eab308",
  },
  {
    name: "Low",
    count: 24,
    color: "#3b82f6",
  },
  {
    name: "Info",
    count: 15,
    color: "#22c55e",
  },
];


// RECENT ALERTS

const recentAlerts = [
  {
    id: 1,
    type: "Brute Force Attack",
    source: "192.168.1.25",
    severity: "Critical",
    time: "2 min ago",
  },
  {
    id: 2,
    type: "Port Scanning",
    source: "10.0.0.15",
    severity: "High",
    time: "5 min ago",
  },
  {
    id: 3,
    type: "Suspicious Login",
    source: "192.168.1.42",
    severity: "Medium",
    time: "8 min ago",
  },
  {
    id: 4,
    type: "Unusual Network Traffic",
    source: "10.0.0.21",
    severity: "Low",
    time: "12 min ago",
  },
];


// DASHBOARD

function Dashboard() {
  return (
    <div className="dashboard">

      {/* =====================================
          HEADER
      ===================================== */}
      <div className="dashboard-header">

        <div>
          <h1>AI-Powered SIEM</h1>
          <p>Security Operations Dashboard</p>
        </div>

        <div className="live-status">
          <span></span>
          Live Monitoring
        </div>

      </div>


      {/* =====================================
          SUMMARY CARDS
      ===================================== */}
      <div className="stats-grid">

        {/* TOTAL */}
        <div className="stat-card total">
          <div>
            <p>Total Alerts</p>
            <h2>100</h2>
          </div>

          <div className="stat-icon">
            ⚠
          </div>
        </div>


        {/* CRITICAL */}
        <div className="stat-card critical">
          <div>
            <p>Critical</p>
            <h2>8</h2>
          </div>

          <div className="stat-icon">
            🔴
          </div>
        </div>


        {/* HIGH */}
        <div className="stat-card high">
          <div>
            <p>High</p>
            <h2>18</h2>
          </div>

          <div className="stat-icon">
            🟠
          </div>
        </div>


        {/* MEDIUM */}
        <div className="stat-card medium">
          <div>
            <p>Medium</p>
            <h2>35</h2>
          </div>

          <div className="stat-icon">
            🟡
          </div>
        </div>


        {/* LOW */}
        <div className="stat-card low">
          <div>
            <p>Low</p>
            <h2>24</h2>
          </div>

          <div className="stat-icon">
            🔵
          </div>
        </div>


        {/* INFO */}
        <div className="stat-card info">
          <div>
            <p>Info</p>
            <h2>15</h2>
          </div>

          <div className="stat-icon">
            🟢
          </div>
        </div>

      </div>


      {/* =====================================
          CHARTS
      ===================================== */}
      <div className="charts-grid">


        {/* =====================================
            ALERT TREND GRAPH
        ===================================== */}
        <div className="chart-card">

          <div className="card-header">

            <div>
              <h3>Alerts Over Time</h3>

              <p>
                Security events detected during
                the monitoring period
              </p>
            </div>

          </div>


          <ResponsiveContainer
            width="100%"
            height={320}
          >

            <LineChart
              data={alertTrend}
              margin={{
                top: 10,
                right: 20,
                left: 0,
                bottom: 10,
              }}
            >

              {/* GRID */}
              <CartesianGrid
                strokeDasharray="3 3"
                stroke="#2a2f3a"
                vertical={false}
              />


              {/* X AXIS */}
              <XAxis
                dataKey="time"
                stroke="#8b93a7"

                tick={{
                  fill: "#8b93a7",
                  fontSize: 12,
                }}

                tickLine={false}

                axisLine={{
                  stroke: "#343a46",
                }}
              />


              {/* Y AXIS */}
              <YAxis
                stroke="#8b93a7"

                tick={{
                  fill: "#8b93a7",
                  fontSize: 12,
                }}

                tickLine={false}

                axisLine={false}

                allowDecimals={false}
              />


              {/* TOOLTIP */}
              <Tooltip
                cursor={{
                  stroke: "#4b5563",
                  strokeDasharray: "4 4",
                }}

                contentStyle={{
                  backgroundColor: "#151922",
                  border: "1px solid #343a46",
                  borderRadius: "8px",
                  color: "#ffffff",
                  boxShadow:
                    "0 4px 12px rgba(0,0,0,0.4)",
                }}

                labelStyle={{
                  color: "#ffffff",
                  fontWeight: "600",
                  marginBottom: "4px",
                }}

                itemStyle={{
                  color: "#ef4444",
                }}
              />


              {/* LINE */}
              <Line
                type="monotone"
                dataKey="alerts"
                name="Security Alerts"

                stroke="#ef4444"

                strokeWidth={3}

                dot={{
                  r: 4,
                  fill: "#ef4444",
                  stroke: "#151922",
                  strokeWidth: 2,
                }}

                activeDot={{
                  r: 7,
                  fill: "#ef4444",
                  stroke: "#ffffff",
                  strokeWidth: 2,
                }}

                animationDuration={1000}

                animationEasing="ease-in-out"
              />

            </LineChart>

          </ResponsiveContainer>

        </div>


        {/* =====================================
            SEVERITY GRAPH
        ===================================== */}
        <div className="chart-card">

          <div className="card-header">

            <div>
              <h3>Alerts by Severity</h3>

              <p>
                Current security threat levels
              </p>
            </div>

          </div>


          <ResponsiveContainer
            width="100%"
            height={320}
          >

            <BarChart
              data={severityData}
              margin={{
                top: 10,
                right: 20,
                left: 0,
                bottom: 10,
              }}
            >

              <CartesianGrid
                strokeDasharray="3 3"
                stroke="#2a2f3a"
                vertical={false}
              />


              <XAxis
                dataKey="name"
                stroke="#8b93a7"

                tick={{
                  fill: "#8b93a7",
                  fontSize: 12,
                }}

                tickLine={false}

                axisLine={{
                  stroke: "#343a46",
                }}
              />


              <YAxis
                stroke="#8b93a7"

                tick={{
                  fill: "#8b93a7",
                  fontSize: 12,
                }}

                tickLine={false}

                axisLine={false}

                allowDecimals={false}
              />


              <Tooltip
                cursor={{
                  fill: "rgba(255,255,255,0.03)",
                }}

                contentStyle={{
                  backgroundColor: "#151922",
                  border: "1px solid #343a46",
                  borderRadius: "8px",
                  color: "#ffffff",
                }}

                labelStyle={{
                  color: "#ffffff",
                  fontWeight: "600",
                }}
              />


              <Bar
                dataKey="count"
                name="Alerts"

                radius={[
                  6,
                  6,
                  0,
                  0
                ]}
              >

                {severityData.map(
                  (entry, index) => (

                    <Cell
                      key={`cell-${index}`}
                      fill={entry.color}
                    />

                  )
                )}

              </Bar>

            </BarChart>

          </ResponsiveContainer>

        </div>

      </div>


      {/* =====================================
          RECENT ALERTS
      ===================================== */}
      <div className="alerts-card">

        <div className="card-header">

          <div>
            <h3>
              Recent Security Alerts
            </h3>

            <p>
              Latest detected security events
            </p>
          </div>


          <button className="view-all">
            View All
          </button>

        </div>


        <div className="table-container">

          <table>

            <thead>

              <tr>
                <th>Alert</th>
                <th>Source IP</th>
                <th>Severity</th>
                <th>Time</th>
              </tr>

            </thead>


            <tbody>

              {recentAlerts.map((alert) => (

                <tr key={alert.id}>

                  <td>
                    <strong>
                      {alert.type}
                    </strong>
                  </td>


                  <td>
                    {alert.source}
                  </td>


                  <td>

                    <span
                      className={`severity ${alert.severity.toLowerCase()}`}
                    >
                      {alert.severity}
                    </span>

                  </td>


                  <td>
                    {alert.time}
                  </td>

                </tr>

              ))}

            </tbody>

          </table>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;