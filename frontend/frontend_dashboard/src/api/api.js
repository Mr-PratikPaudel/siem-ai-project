import axios from "axios";


const API = axios.create({
    baseURL: import.meta.env.VITE_API_URL,
    headers: {
        "X-API-Key": import.meta.env.VITE_API_KEY
    }
});


export const getAlerts = () => {

    return API.get("/logs").then((response) => {

        return {
            data: response.data.logs.map((log, index) => ({
                id: index + 1,          
                attack: log.event,
                source: log.source,
                severity: log.severity
                    ? log.severity.charAt(0).toUpperCase() + log.severity.slice(1).toLowerCase()
                    : "Info",
                time: log.timestamp,
            }))
        };

    });

};


export const getDashboard = () => {

    return API.get("/dashboard");

};


export const getIncidents = () => {

    return API.get("/incidents");

};


export default API;