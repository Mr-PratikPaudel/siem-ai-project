import "./eventchart.css";

import "../styles/eventchart.css";

const alerts = [
  {
    id: 1,
    attack: "DoS Attack",
    severity: "High",
    time: "10:30 AM",
  },
  {
    id: 2,
    attack: "Brute Force",
    severity: "Medium",
    time: "11:15 AM",
  },
  {
    id: 3,
    attack: "Port Scan",
    severity: "Low",
    time: "12:00 PM",
  },
  {
    id: 4,
    attack: "SQL Injection",
    severity: "High",
    time: "01:20 PM",
  },
  {
    id: 5,
    attack: "Malware",
    severity: "Medium",
    time: "02:10 PM",
  },
];

useEffect(() => {
  fetchAlerts();

  const interval = setInterval(() => {
    fetchAlerts();
  }, 5000);

  return () => clearInterval(interval);
}, []);

{loading ? (
  <p>Loading alerts...</p>
) : alerts.length === 0 ? (
  <p>No alerts found.</p>
) : (
  <AlertsTable alerts={alerts} />
)}

export default alerts;