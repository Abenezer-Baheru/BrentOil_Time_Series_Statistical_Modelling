import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import axios from 'axios';

function App() {
    const [data, setData] = useState([]);
    const [modelResults, setModelResults] = useState({});

    useEffect(() => {
        // Fetch data from Flask API
        axios.get('/api/data')
            .then(response => setData(response.data))
            .catch(error => console.error('Error fetching data:', error));

        // Fetch model results from Flask API
        axios.get('/api/model-results')
            .then(response => setModelResults(response.data))
            .catch(error => console.error('Error fetching model results:', error));
    }, []);

    return (
        <div className="App">
            <h1>Brent Oil Prices Dashboard</h1>
            <LineChart
                width={800}
                height={400}
                data={data}
                margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
            >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="Date" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="Price" stroke="#8884d8" activeDot={{ r: 8 }} />
            </LineChart>

            <h2>Model Results</h2>
            <p>VAR RMSE: {modelResults.var_rmse}</p>
            <p>VAR MAE: {modelResults.var_mae}</p>
            <p>LSTM RMSE: {modelResults.lstm_rmse}</p>
            <p>LSTM MAE: {modelResults.lstm_mae}</p>
        </div>
    );
}

export default App;