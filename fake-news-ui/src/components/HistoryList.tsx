import { useEffect, useState } from 'react';
import axios from 'axios';
import { Typography, Stack } from '@mui/material';
import ResultCard from './ResultCard';

export default function HistoryList() {
  const [items, setItems] = useState<any[]>([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/historico')
      .then((res) => setItems(res.data));
  }, []);

  return (
    <>
      <Typography variant="h6" sx={{ mt: 4, mb: 2 }}>Histórico</Typography>
      <Stack spacing={2}>
        {[...items].reverse().map((item, i) => (
          <ResultCard key={i} result={item} />
        ))}
      </Stack>
    </>
  );
}
