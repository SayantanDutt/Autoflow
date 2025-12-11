# Python Automation Tool - API Documentation

## Overview

The Flask API backend connects the web dashboard to Python automation scripts. It provides RESTful endpoints for system monitoring, data processing, and file management.

## Base URL

\`\`\`
http://localhost:8000
\`\`\`

## Starting the API Server

\`\`\`bash
# Navigate to api directory
cd api

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
\`\`\`

The API will be available at `http://localhost:8000`

## API Endpoints

### Health & Status

#### Check API Health
\`\`\`http
GET /api/health
\`\`\`

**Response:**
\`\`\`json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00",
  "version": "1.0.0"
}
\`\`\`

#### Get API Status
\`\`\`http
GET /api/status
\`\`\`

**Response:**
\`\`\`json
{
  "api_status": "running",
  "dashboard_connected": true,
  "scripts_available": ["system_monitor", "data_processor", "file_manager"],
  "timestamp": "2024-01-15T10:30:00"
}
\`\`\`

---

## System Monitoring Endpoints

### Get System Health Report
\`\`\`http
GET /api/system/health
\`\`\`

**Response:**
\`\`\`json
{
  "timestamp": "2024-01-15T10:30:00",
  "overall_health": "HEALTHY",
  "cpu": {
    "usage_percent": 45.2,
    "core_count": 8,
    "alert": false
  },
  "memory": {
    "total_gb": 16.0,
    "used_gb": 8.5,
    "percent": 53.1,
    "alert": false
  },
  "disk": {
    "total_gb": 500.0,
    "used_gb": 250.0,
    "percent": 50.0,
    "alert": false
  },
  "network": {...},
  "processes": {...}
}
\`\`\`

### Get CPU Statistics
\`\`\`http
GET /api/system/cpu
\`\`\`

**Response:**
\`\`\`json
{
  "usage_percent": 45.2,
  "core_count": 8,
  "per_core_usage": [30.1, 45.2, 60.5, 28.9, ...],
  "alert": false
}
\`\`\`

### Get Memory Statistics
\`\`\`http
GET /api/system/memory
\`\`\`

**Response:**
\`\`\`json
{
  "total_gb": 16.0,
  "used_gb": 8.5,
  "available_gb": 7.5,
  "percent": 53.1,
  "alert": false
}
\`\`\`

### Get Disk Statistics
\`\`\`http
GET /api/system/disk?path=/
\`\`\`

**Parameters:**
- `path` (optional): Disk path to check (default: "/")

**Response:**
\`\`\`json
{
  "total_gb": 500.0,
  "used_gb": 250.0,
  "free_gb": 250.0,
  "percent": 50.0,
  "alert": false
}
\`\`\`

### Get Network Statistics
\`\`\`http
GET /api/system/network
\`\`\`

**Response:**
\`\`\`json
{
  "bytes_sent": 1048576000,
  "bytes_received": 2097152000,
  "packets_sent": 1000000,
  "packets_received": 2000000
}
\`\`\`

### Get Top Processes
\`\`\`http
GET /api/system/processes?top_n=5
\`\`\`

**Parameters:**
- `top_n` (optional): Number of top processes (default: 5)

**Response:**
\`\`\`json
{
  "top_processes": [
    {"pid": 1234, "name": "chrome", "memory_percent": 12.5},
    {"pid": 5678, "name": "python", "memory_percent": 8.3},
    ...
  ]
}
\`\`\`

---

## Data Processing Endpoints

### Upload and Process Data File
\`\`\`http
POST /api/data/upload
Content-Type: multipart/form-data

file: <binary file data>
\`\`\`

**Response:**
\`\`\`json
{
  "status": "success",
  "filename": "data.csv",
  "statistics": {
    "total_rows": 1000,
    "total_columns": 5,
    "memory_usage": "125000",
    "numeric_summary": {...},
    "data_types": {...}
  }
}
\`\`\`

### Analyze Existing File
\`\`\`http
GET /api/data/analyze/<filename>
\`\`\`

**Response:**
\`\`\`json
{
  "total_rows": 1000,
  "total_columns": 5,
  "memory_usage": "125000",
  "numeric_summary": {...},
  "data_types": {...}
}
\`\`\`

### Process Data with Parameters
\`\`\`http
POST /api/data/process
Content-Type: application/json

{
  "filepath": "/path/to/file.csv",
  "output_path": "processed_output.csv"
}
\`\`\`

**Response:**
\`\`\`json
{
  "status": "success",
  "output_file": "processed_output.csv",
  "message": "Data processed and saved"
}
\`\`\`

---

## File Management Endpoints

### List Files
\`\`\`http
GET /api/files/list?directory=.&recursive=false
\`\`\`

**Parameters:**
- `directory` (optional): Directory path (default: ".")
- `recursive` (optional): Recursive search (default: false)

**Response:**
\`\`\`json
{
  "status": "success",
  "count": 5,
  "files": [
    {
      "name": "data.csv",
      "path": "./data.csv",
      "size_bytes": 1024000,
      "modified": "2024-01-15T10:30:00",
      "type": ".csv"
    },
    ...
  ]
}
\`\`\`

### Get Directory Size
\`\`\`http
GET /api/files/size?directory=.
\`\`\`

**Response:**
\`\`\`json
{
  "total_bytes": 10485760,
  "total_mb": 10.0,
  "total_gb": 0.01,
  "file_count": 50
}
\`\`\`

### Cleanup Old Files
\`\`\`http
POST /api/files/cleanup
Content-Type: application/json

{
  "directory": "./logs",
  "days": 30,
  "extensions": [".log", ".tmp"]
}
\`\`\`

**Parameters:**
- `directory` (required): Directory to clean
- `days` (required): Delete files older than N days
- `extensions` (optional): Only delete specific extensions

**Response:**
\`\`\`json
{
  "status": "success",
  "deleted_count": 15
}
\`\`\`

### Organize Files by Extension
\`\`\`http
POST /api/files/organize
Content-Type: application/json

{
  "directory": "."
}
\`\`\`

**Response:**
\`\`\`json
{
  "status": "success",
  "message": "Files organized"
}
\`\`\`

### Create Backup
\`\`\`http
POST /api/files/backup
Content-Type: application/json

{
  "source": "./important_data",
  "destination": "./backup_important_data"
}
\`\`\`

**Response:**
\`\`\`json
{
  "status": "success",
  "message": "Backup completed"
}
\`\`\`

---

## Execution History Endpoints

### Get History
\`\`\`http
GET /api/history?limit=50
\`\`\`

**Parameters:**
- `limit` (optional): Number of recent entries (default: 50)

**Response:**
\`\`\`json
{
  "status": "success",
  "count": 100,
  "history": [
    {
      "timestamp": "2024-01-15T10:30:00",
      "task": "system_health",
      "status": "success",
      "details": {"health": "HEALTHY"}
    },
    ...
  ]
}
\`\`\`

### Clear History
\`\`\`http
POST /api/history/clear
\`\`\`

**Response:**
\`\`\`json
{
  "status": "success",
  "message": "History cleared"
}
\`\`\`

---

## Dashboard Endpoints

### Get Dashboard Summary
\`\`\`http
GET /api/dashboard/summary
\`\`\`

**Response:**
\`\`\`json
{
  "total_tasks": 248,
  "successful_tasks": 218,
  "failed_tasks": 12,
  "system_health": "HEALTHY",
  "cpu_usage": 45.2,
  "memory_usage": 53.1,
  "disk_usage": 50.0,
  "timestamp": "2024-01-15T10:30:00"
}
\`\`\`

---

## Error Handling

All errors return JSON response with status code:

\`\`\`json
{
  "error": "Error description"
}
\`\`\`

Common status codes:
- `200`: Success
- `400`: Bad Request
- `404`: Not Found
- `500`: Internal Server Error

---

## CORS Headers

The API includes CORS headers to allow requests from:
- `http://localhost:3000` (dashboard)
- Any origin in development

## Authentication

Currently, the API has no authentication. For production, implement:
- JWT tokens
- API keys
- OAuth2

---

## Rate Limiting

Not implemented by default. For production, consider adding rate limiting using Flask-Limiter.

---

## Testing the API

### Using cURL

\`\`\`bash
# Health check
curl http://localhost:8000/api/health

# Get system health
curl http://localhost:8000/api/system/health

# List files
curl "http://localhost:8000/api/files/list?directory=."

# Cleanup old files
curl -X POST http://localhost:8000/api/files/cleanup \
  -H "Content-Type: application/json" \
  -d '{"directory":".","days":30}'
\`\`\`

### Using Python Requests

\`\`\`python
import requests

BASE_URL = 'http://localhost:8000'

# Get system health
response = requests.get(f'{BASE_URL}/api/system/health')
print(response.json())

# Get dashboard summary
response = requests.get(f'{BASE_URL}/api/dashboard/summary')
print(response.json())
\`\`\`

---

## Environment Variables

Set these in `.env` file or export them:

\`\`\`bash
FLASK_ENV=development
FLASK_DEBUG=1
API_PORT=8000
API_HOST=0.0.0.0
\`\`\`

---

## Deployment

For production deployment:

1. Set `FLASK_ENV=production`
2. Use production WSGI server: `gunicorn -w 4 app:app`
3. Add authentication
4. Enable rate limiting
5. Set up proper error logging
6. Use HTTPS

\`\`\`bash
# Install production server
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
\`\`\`

---

## Support

For issues or questions, check the logs:

\`\`\`bash
# Check API logs
tail -f api_output.log
