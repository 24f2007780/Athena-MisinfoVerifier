# Misinformation Reporting System

This module provides functionality for reporting and analyzing potential misinformation with severity and confidence scoring.

## Features

- Report potential misinformation with severity and confidence scores
- Automatic source finding using Google Custom Search
- AI-powered analysis using Gemini Flash 2.5
- Database storage for tracking and managing reports
- RESTful API for integration with frontend applications

## Setup

1. Copy the example environment file and update with your API keys:
   ```bash
   cp .env.example .env
   ```

2. Update the `.env` file with your API keys:
   - `GOOGLE_API_KEY`: Your Google Cloud API key with Custom Search API enabled
   - `GOOGLE_CX`: Your Custom Search Engine ID
   - `GEMINI_API_KEY`: Your Google Gemini API key

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```python
   from src.database import init_db
   init_db()
   ```

## API Endpoints

### Create a Report

```http
POST /api/reports/
Content-Type: application/json

{
  "misinformation": "The Earth is flat.",
  "severity": "high",
  "confidence_score": 0.9,
  "reporter_contact": "reporter@example.com",
  "notes": "This is a test report"
}
```

### Get a Report

```http
GET /api/reports/{report_id}
```

### List Reports

```http
GET /api/reports/
```

### Update a Report

```http
PATCH /api/reports/{report_id}
Content-Type: application/json

{
  "status": "verified",
  "notes": "Verified by moderator"
}
```

### Verify a Report

```http
POST /api/reports/{report_id}/verify
Content-Type: application/json

{
  "verified_by": "moderator@example.com",
  "notes": "Verified by moderator"
}
```

## Models

### Report

```typescript
{
  id: string;
  misinformation: string;
  severity: "low" | "medium" | "high" | "critical";
  confidence_score: number; // 0.0 to 1.0
  status: "pending" | "verified" | "rejected";
  sources: Array<{
    url: string;
    title?: string;
    snippet?: string;
    is_primary?: boolean;
  }>;
  reporter_contact?: string;
  notes?: string;
  verified_by?: string;
  verification_date?: string; // ISO 8601 datetime
  created_at: string; // ISO 8601 datetime
  updated_at: string; // ISO 8601 datetime
}
```

## Environment Variables

- `GOOGLE_API_KEY`: Google Cloud API key with Custom Search API enabled
- `GOOGLE_CX`: Google Custom Search Engine ID
- `GEMINI_API_KEY`: Google Gemini API key
- `DATABASE_URL`: Database connection URL (default: `sqlite:///./athena.db`)
- `DEBUG`: Enable debug mode (default: `False`)
- `ENVIRONMENT`: Application environment (e.g., `development`, `production`)

## Development

1. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

2. Run tests:
   ```bash
   pytest
   ```

3. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
