// frontend/src/components/GeneralNews.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const GeneralNews = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:8000/news/general')
      .then(res => {
        setNews(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching news:', err);
        setLoading(false);
      });
  }, []);

  return (
    // <div style={{ display: 'flex', minHeight: '100vh' }}>
        
        <div
          style={{
            // display: 'flex',
            // width: '38rem',
            padding: '1rem',
            borderLeft: '1px solid #ddd',
            backgroundColor: '#f9f9f9',
          }}
        >
          <h2 style={{ borderBottom: '2px solid #ccc', paddingBottom: '0.5rem' }}>
            📰 General Stock Market News
          </h2>

          {loading ? (
            <p>Loading...</p>
          ) : (
            <ul style={{ listStyle: 'none', padding: 0 }}>
              {news.map((item, idx) => (
                <li
                  key={idx}
                  style={{
                    marginBottom: '1rem',
                    paddingBottom: '0.75rem',
                    borderBottom: '1px solid #eee',
                  }}
                >
                  <a
                    href={item.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{
                      fontWeight: 'bold',
                      color: '#2c3e50',
                      textDecoration: 'none',
                      display: 'block',
                      textAlign:'left',
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
      // </div>


  );
};

export default GeneralNews;
