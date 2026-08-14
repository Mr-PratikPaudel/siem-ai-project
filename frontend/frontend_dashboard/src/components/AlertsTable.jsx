import { useState, useEffect } from "react";
import { getAlerts } from "../api/api";
import AlertDetails from "./AlertDetails";

function AlertsTable() {
  const [alerts, setAlerts] = useState([]);
  const [search, setSearch] = useState("");
  const [severity, setSeverity] = useState("All");
  const [selectedAlert, setSelectedAlert] = useState(null);

  // Fetch alerts from API
  useEffect(() => {
    getAlerts()
      .then((response) => {
        setAlerts(response.data);
      })
      .catch((error) => {
        console.log("API Error:", error);
      });
  }, []);

  // Search and filter
  const filteredAlerts = alerts.filter((alert) => {
    const searchMatch = alert.attack
      ?.toLowerCase()
      .includes(search.toLowerCase());

    const severityMatch =
      severity === "All" || alert.severity === severity;

    return searchMatch && severityMatch;
  });

  // Severity color
  const getColor = (level) => {
    switch (level) {
      case "Critical":
        return "#ef4444";
      case "High":
        return "#f97316";
      case "Medium":
        return "#eab308";
      case "Low":
        return "#22c55e";
      case "Info":
        return "#3b82f6";
      default:
        return "#000";
    }
  };

  return (
    <div className="card">

      {/* Header */}
      <h2>Security Alerts</h2>

      <h4>
        Total Alerts: {filteredAlerts.length}
      </h4>

      {/* Search and Filter */}
      <div
        style={{
          marginBottom: "15px",
          display: "flex",
          gap: "10px",
          alignItems: "center",
        }}
      >
        <input
          type="text"
          placeholder="Search attack..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          style={{
            padding: "8px 12px",
            width: "220px",
          }}
        />

        <select
          value={severity}
          onChange={(e) => setSeverity(e.target.value)}
          style={{
            padding: "8px 12px",
          }}
        >
          <option value="All">All Severity</option>
          <option value="Critical">Critical</option>
          <option value="High">High</option>
          <option value="Medium">Medium</option>
          <option value="Low">Low</option>
          <option value="Info">Info</option>
        </select>
      </div>

      {/* Alerts Table */}
      <table
        border="1"
        cellPadding="10"
        style={{
          width: "100%",
          borderCollapse: "collapse",
        }}
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Attack</th>
            <th>Severity</th>
            <th>Time</th>
          </tr>
        </thead>

        <tbody>
          {filteredAlerts.length > 0 ? (
            filteredAlerts.map((alert) => (
              <tr
                key={alert.id}
                onClick={() => setSelectedAlert(alert)}
                style={{
                  cursor: "pointer",
                }}
              >
                <td>{alert.id}</td>

                <td>{alert.attack}</td>

                <td
                  style={{
                    color: getColor(alert.severity),
                    fontWeight: "bold",
                  }}
                >
                  {alert.severity}
                </td>

                <td>{alert.time}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4" align="center">
                No Alerts Found
              </td>
            </tr>
          )}
        </tbody>
      </table>

      {/* Alert Details */}
      {selectedAlert && (
        <AlertDetails
          alert={selectedAlert}
          onClose={() => setSelectedAlert(null)}
        />
      )}
    </div>
  );
}

export default AlertsTable;