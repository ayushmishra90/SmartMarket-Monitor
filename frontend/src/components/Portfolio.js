import React, { useState, useEffect } from 'react';
import axios from 'axios';

const Portfolio = ({ onPortfolioChange }) => {
  const [input, setInput] = useState('');
  const [portfolio, setPortfolio] = useState([]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const symbols = input
      .split(',')
      .map(s => s.trim().toUpperCase())
      .filter(Boolean);
    try {
      const res = await axios.post('http://localhost:8000/portfolio/', {
        symbols
      });
      setPortfolio(res.data.symbols);
      setInput('');
      if (onPortfolioChange) onPortfolioChange();
    } catch (err) {
      console.error('Failed to save portfolio', err);
    }
  };

  useEffect(() => {
    axios.get('http://localhost:8000/portfolio/').then(res => {
      setPortfolio(res.data.symbols);
    });
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>📊 Link Your Portfolio</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="e.g. RELIANCE, INFY, TCS"
          style={{ padding: '0.5rem', width: '100%', marginBottom: '0.5rem' }}
        />
        <button
          type="submit"
          style={{
            padding: '0.5rem 1rem',
            backgroundColor: '#007bff',
            color: '#fff',
            border: 'none',
            borderRadius: '4px'
          }}
        >
          Submit
        </button>
      </form>

      {portfolio.length > 0 && (
        <div style={{ marginTop: '1rem' }}>
          <strong>🔗 Linked Stocks:</strong>
          <ul>
            {portfolio.map((sym, idx) => (
              <li key={idx}>{sym}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Portfolio;
