import { Container, Typography } from '@mui/material';
import InputForm from './components/InputForm';
import ResultCard from './components/ResultCard';
import HistoryList from './components/HistoryList';
import { useState } from 'react';

function App() {
  const [result, setResult] = useState<any>(null);

  return (
    <Container sx={{ py: 5 }}>
      <Typography variant="h4" gutterBottom>Detector de Fake News</Typography>
      <InputForm onResult={setResult} />
      {result && <ResultCard result={result} />}
      <HistoryList />
    </Container>
  );
}

export default App;
