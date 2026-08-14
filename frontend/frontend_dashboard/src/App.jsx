import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import AlertsTable from "./components/AlertsTable";
import EventChart from "./components/eventChart";
import SystemStatus from "./components/SystemStatus";
import AnomalyChart from "./components/AnomalyChart";
import Dashboard from "./components/eventChart";
function App(){


return(

<>

<Header/>


<div className="container">


<Sidebar/>


<main className="content">


<AlertsTable/>


<EventChart/>


<SystemStatus/>


</main>


</div>


</>


);


}


export default App;