import axios from "axios";


const API = axios.create({
    baseURL: "http://localhost:8000",
});


export const getAlerts = () => {
    return API.get("/logs");
};


export default API;