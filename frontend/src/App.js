import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get('/api/health_metrics')
      .then(response => setData(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Health Tracking System</h1>
        <ul>
          {data.map(metric => (
            <li key={metric.id}>{metric.value} - {metric.metric_type}</li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;
