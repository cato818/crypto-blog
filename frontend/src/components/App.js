import React from 'react';
import Header from './components/Header';
import PredictionList from './components/PredictionList';
import SubscriptionForm from './components/SubscriptionForm';
import './App.css';
function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <PredictionList />
        <SubscriptionForm />
      </main>
      <footer>
        <p>&copy; 2025 Crypto Blog</p>
      </footer>
    </div>
  );
}

export default App;