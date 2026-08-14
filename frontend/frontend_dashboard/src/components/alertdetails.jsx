function AlertDetails({alert}){


return(

<div className="card">


<h2>
Alert Investigation
</h2>


<p>
<b>Attack Type:</b> {alert.attack}
</p>


<p>
<b>Severity:</b> {alert.severity}
</p>


<p>
<b>Source IP:</b> {alert.source_ip}
</p>


<p>
<b>Destination IP:</b> {alert.destination_ip}
</p>


<p>
<b>Anomaly Score:</b> {alert.score}
</p>


<p>
<b>Time:</b> {alert.time}
</p>


</div>

);


}


export default AlertDetails;