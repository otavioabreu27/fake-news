import { Card, CardContent, Typography, Chip } from '@mui/material';

export default function ResultCard({ result }: { result: any }) {
  return (
    <Card sx={{ mt: 3 }}>
      <CardContent>
        <Typography variant="h6">
          {result.label === 'FAKE' ? '🚨 FAKE' : '✅ REAL'}
        </Typography>
        <Typography variant="body2" sx={{ my: 1 }}>
          {result.text}
        </Typography>
        <Chip label={`Score: ${result.score}%`} color={result.label === 'FAKE' ? 'error' : 'success'} />
      </CardContent>
    </Card>
  );
}
