import React, { useState, useEffect } from 'react';
import './PredictionList.css';

const PredictionList = () => {
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // TODO: Fetch predictions from API
    setLoading(false);
  }, []);

  return (
    <section className="predictions">
      <h2>Latest Predictions</h2>
      {loading ? (
        <p>Loading predictions...</p>
      ) : (
        <div className="predictions-grid">
          {predictions.map((prediction, index) => (
            <div key={index} className="prediction-card">
              <h3>{prediction.cryptocurrency}</h3>
              <p>Predicted Price: ${prediction.price}</p>
              <p>Confidence: {prediction.confidence}%</p>
            </div>
          ))}
        </div>
      )}
    </section>
  );
};

export default PredictionList;