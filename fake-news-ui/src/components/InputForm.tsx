import { useState } from 'react';
import {
  TextField, Button, MenuItem, Stack, Paper, Typography,
} from '@mui/material';
import axios from 'axios';

type InputType = 'text' | 'url';

interface Props {
  onResult: (result: any) => void;
}

export default function InputForm({ onResult }: Props) {
  const [inputType, setInputType] = useState<InputType>('text');
  const [content, setContent] = useState('');

  const handleSubmit = async () => {
    const res = await axios.post('http://localhost:8000/api/classificar-noticia', {
      input_type: inputType,
      content,
    });
    onResult(res.data);
  };

  return (
    <Paper sx={{ p: 3 }}>
      <Typography variant="h6">Classificar Notícia</Typography>
      <Stack spacing={2}>
        <TextField
          select
          label="Tipo de entrada"
          value={inputType}
          onChange={(e) => setInputType(e.target.value as InputType)}
        >
          <MenuItem value="text">Texto</MenuItem>
          <MenuItem value="url">URL</MenuItem>
        </TextField>
        <TextField
          label="Conteúdo"
          multiline
          rows={4}
          value={content}
          onChange={(e) => setContent(e.target.value)}
        />
        <Button variant="contained" onClick={handleSubmit}>Classificar</Button>
      </Stack>
    </Paper>
  );
}
