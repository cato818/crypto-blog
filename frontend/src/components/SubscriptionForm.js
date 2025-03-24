import React, { useState } from 'react';
import './SubscriptionForm.css';

const SubscriptionForm = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: Implement subscription logic
    setMessage('Thanks for subscribing!');
    setEmail('');
  };

  return (
    <section className="subscription">
      <h2>Get Crypto Predictions</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Enter your email"
          required
        />
        <button type="submit">Subscribe</button>
      </form>
      {message && <p className="message">{message}</p>}
    </section>
  );
};

export default SubscriptionForm;