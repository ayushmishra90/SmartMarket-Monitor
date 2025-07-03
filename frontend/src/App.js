import './App.css';
import Portfolio from './components/Portfolio';
import GeneralNews from './components/GeneralNews';
import FilteredNews from './components/FilteredNews';
import React, { useState } from 'react';

function App() {
  const [refreshKey, setRefreshKey] = useState(0);

  const handlePortfolioChange = () => {
    setRefreshKey((prev) => prev + 1); // 🔄 triggers FilteredNews reload
  };
  return (
    <div style={{ display: 'flex', minHeight: '100vh' }}>
      {/* Left Section: Portfolio */}
      <div style={{ flex: 1 }}>
        {/* <Portfolio />
        <FilteredNews /> */}
        <Portfolio onPortfolioChange={handlePortfolioChange} />
        <FilteredNews refresh={refreshKey} />
      </div>
      

      {/* Right Section: General News */}
      <div style={{ display: 'flex' }}>
        <GeneralNews />
      </div>
    </div>
  );
}

export default App;
