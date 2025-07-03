import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FilteredNews = ({ refresh }) => {
  const [filtered, setFiltered] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:8000/news/filtered')
      .then(res => {
        setFiltered(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching filtered news:', err);
        setLoading(false);
      });
  }, [refresh]);

  return (
    <div style={{ padding: '2rem', background: '#eef6ff' }}>
      <h2>🎯 News Related to Your Portfolio</h2>
      {loading ? (
        <p>Loading filtered news...</p>
      ) : filtered.length === 0 ? (
        <p>No matching news found for your portfolio.</p>
      ) : (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {filtered.map((item, idx) => (
            <li
              key={idx}
              style={{
                marginBottom: '1rem',
                paddingBottom: '0.75rem',
                borderBottom: '1px solid #ccc',
              }}
            >
              <a
                href={item.link}
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  fontWeight: 'bold',
                  color: '#1e3a8a',
                  textDecoration: 'none',
                  display: 'block',
                }}
              >
                {item.title}
              </a>
              {/* <div style={{ fontSize: '0.75rem', color: '#888', marginTop: '0.25rem' }}>
                Source: {item.source}
              </div> */}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default FilteredNews;
