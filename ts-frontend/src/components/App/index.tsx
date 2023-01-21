import React, { useEffect, useState } from 'react';
import './App.css';
import { ApiResponse, getApiResponse } from '../../services/api-example';
import { asyncSleep } from '../../utils/async';
import { Box, Button, Typography } from '@mui/material';

function App() {
  const [data, setData] = useState(false as ApiResponse | false);
  const [isLoading, setIsLoading] = useState(true);

  const getApiData = async () => {
    const data = await getApiResponse();
    console.log('data: ', data);
    setData(data);
    setIsLoading(false);
  };

  const clickHandler = async (): Promise<void> => {
    setIsLoading(true);
    setData(false);
    await asyncSleep(3000);
    await getApiData();
  }

  useEffect(() => {
    setIsLoading(true);
    void getApiData();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        {data && <Typography variant="h1">IP address: {data.origin}</Typography>}
        {isLoading && (
          <Box mb={2}>
            <Typography variant="h2">Loading...</Typography>
            <img src="https://emojis.slackmojis.com/emojis/images/1643514139/987/parrot.gif" style={{ height: '100px' }} />
          </Box>
        )}
        <Button variant="outlined" onClick={clickHandler}>Get Data!</Button>
      </header>
    </div>
  );
}

export default App;
