# FastAPI + Vue 3 SPA Boilerplate

A minimal FastAPI + Vue 3 SPA boilerplate for rapid application development. Includes health check endpoints, CORS configuration, and one-command setup. Perfect starting point for modern web applications.

## Features

- **FastAPI Backend** with automatic API documentation
- **Vue 3 Frontend** with Vite for fast development
- **Health Check Endpoints** for monitoring
- **CORS Configuration** for cross-origin requests
- **One-Command Setup** with Docker Compose
- **Hot Reload** for both frontend and backend development
- **Modern Development Stack** with the latest versions

## Project Structure

```
├── backend/                 # FastAPI application
│   ├── app/
│   │   ├── main.py         # FastAPI app with health checks and CORS
│   │   └── api/            # API routes (extensible)
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile         # Backend container
├── frontend/               # Vue 3 SPA
│   ├── src/
│   │   ├── App.vue        # Main Vue component
│   │   └── main.js        # Vue app entry point
│   ├── package.json       # Frontend dependencies
│   ├── vite.config.js     # Vite configuration with proxy
│   └── Dockerfile         # Frontend container
├── docker-compose.yml     # One-command setup
├── package.json           # Root scripts for convenience
└── README.md              # This file
```

## Quick Start

![FastAPI Vue SPA Boilerplate](https://github.com/user-attachments/assets/295ac5fd-63a1-4ec6-b331-e4650cbcd881)

### Option 1: One-Command Start Script (Recommended)

```bash
# Clone the repository
git clone https://github.com/CodingCru/fastapi-vue-spa-boilerplate.git
cd fastapi-vue-spa-boilerplate

# One-command setup and start
./start.sh
```

### Option 2: Docker Compose

```bash
# Clone the repository
git clone https://github.com/CodingCru/fastapi-vue-spa-boilerplate.git
cd fastapi-vue-spa-boilerplate

# One-command setup and start
npm run dev
```

This will start both backend (port 8000) and frontend (port 3000) services.

### Option 3: Manual Setup

```bash
# Install frontend dependencies
npm run install

# Install backend dependencies  
npm run install:backend

# Start backend (in one terminal)
npm run dev:backend

# Start frontend (in another terminal)
npm run dev:frontend
```

## Available Endpoints

### Backend (http://localhost:8000)
- `GET /` - Root endpoint
- `GET /health` - Health check endpoint
- `GET /api/health` - API health check endpoint  
- `GET /api/status` - Service status endpoint
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

### Frontend (http://localhost:3000)
- Vue 3 SPA with status dashboard
- Automatically proxies API calls to backend
- Shows real-time backend connectivity status

## Development

### Adding New API Endpoints

1. Create new route files in `backend/app/api/`
2. Import and include them in `backend/app/main.py`

### Extending the Frontend

1. Add new Vue components in `frontend/src/components/`
2. Update `frontend/src/App.vue` or create new views
3. Vite will automatically hot-reload your changes

### Environment Configuration

- Backend runs on port 8000 by default
- Frontend runs on port 3000 by default  
- CORS is configured to allow frontend-backend communication
- Vite proxy forwards `/api` and `/health` requests to backend

## Production Deployment

```bash
# Build frontend for production
npm run build

# Backend can be deployed using the Dockerfile or by installing requirements
pip install -r backend/requirements.txt
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000
```

## Technologies Used

- **Backend**: FastAPI, Uvicorn, Python 3.11+
- **Frontend**: Vue 3, Vite, JavaScript ES6+
- **DevOps**: Docker, Docker Compose
- **Development**: Hot reload, CORS, Proxy configuration

## License

MIT License - see LICENSE file for details.
