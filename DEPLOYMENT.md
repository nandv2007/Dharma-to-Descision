# Deployment Guide — Dharma to Decisions

This document provides production deployment instructions for **Dharma to Decisions**, an interactive decision-learning web experience.

---

## Architecture Overview

- **Frontend**: React 18, TypeScript, Tailwind CSS, Vite. Compiles to static assets (`dist/`).
- **Backend**: FastAPI (Python 3.10+), SQLAlchemy ORM, Pydantic v2, Uvicorn ASGI server.
- **Database**: SQLite (default, self-contained in `dharma_decisions.db`) or PostgreSQL.

---

## 1. Quickstart: Local Development

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt   # or fastapi uvicorn sqlalchemy pydantic

# Seed the database
python -m app.seed_data

# Start development server
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Frontend

```bash
cd frontend
npm install

# Start Vite dev server (proxies /api to http://127.0.0.1:8000)
npm run dev
```

The frontend will be available at `http://127.0.0.1:5173`.

---

## 2. Environment Variables

Create `.env` in the root or inside `backend/` and `frontend/`:

### Backend Environment Variables (`backend/.env`)

| Variable | Default | Description |
|---|---|---|
| `DATABASE_URL` | `sqlite:///./app/dharma_decisions.db` | SQLAlchemy connection string |
| `PORT` | `8000` | Port for the ASGI server |
| `HOST` | `0.0.0.0` | Host binding for production |
| `CORS_ORIGINS` | `["http://localhost:5173", "https://yourdomain.com"]` | Allowed CORS origins in `main.py` |

### Frontend Environment Variables (`frontend/.env.production`)

| Variable | Default | Description |
|---|---|---|
| `VITE_API_URL` | `""` (empty string for same-origin or reverse proxy) | Base URL for FastAPI backend (e.g. `https://api.yourdomain.com`) |

---

## 3. Production Build & Deployment Options

### Option A: Render Blueprint (One-Click with `render.yaml`)

This repository contains a ready-to-use `render.yaml` Blueprint file that deploys both the FastAPI backend and React frontend together.

1. Push your repository to GitHub or GitLab.
2. Log in to [Render Dashboard](https://dashboard.render.com).
3. Click **New +** and select **Blueprint**.
4. Connect your repository.
5. Render reads `render.yaml` and sets up:
   - **`dharma-backend`**: FastAPI web service with automatic database seeding (`/api/health`).
   - **`dharma-frontend`**: High-performance static site with SPA routing and automatic `VITE_API_URL` wiring.
6. Click **Apply**. Render will deploy both services automatically!

---

### Option B: Decoupled Deploy (Vercel / Netlify + Render / Railway)

This is an alternative decoupled architecture:

#### 1. Deploy Frontend (e.g., Vercel / Netlify)
1. Set Root Directory to `frontend`.
2. Build Command: `npm run build`
3. Output Directory: `dist`
4. Set Environment Variable: `VITE_API_URL=https://your-backend-domain.com`
5. Configure SPA fallback rule (e.g., `_redirects` or `vercel.json` with rewrite `/*` to `/index.html`).

#### 2. Deploy Backend (e.g., Render / Railway)
1. Set Root Directory to `backend`.
2. Build Command: `pip install -r requirements.txt && python -m app.seed_data`
3. Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. In `backend/app/main.py`, ensure CORS origins include your frontend domain.

---

### Option B: Single VM / VPS (Ubuntu / Debian + Nginx + Systemd)

#### 1. Build the Frontend
```bash
cd frontend
npm ci
npm run build
# Assets compiled to frontend/dist/
```

#### 2. Configure Systemd Service for Uvicorn
Create `/etc/systemd/system/dharma-backend.service`:
```ini
[Unit]
Description=Dharma to Decisions FastAPI Backend
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/dharma/backend
Environment="PATH=/var/www/dharma/backend/venv/bin"
ExecStart=/var/www/dharma/backend/venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000 --workers 2

Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable dharma-backend
sudo systemctl start dharma-backend
```

#### 3. Configure Nginx Reverse Proxy
Create `/etc/nginx/sites-available/dharma`:
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # Static frontend files
    root /var/www/dharma/frontend/dist;
    index index.html;

    # Serve static assets with caching
    location /assets/ {
        expires 1y;
        add_header Cache-Control "public, no-transform";
    }

    # SPA routing fallback
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API reverse proxy
    location /api/ {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable site and restart Nginx:
```bash
sudo ln -s /etc/nginx/sites-available/dharma /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### 4. Enable SSL with Certbot
```bash
sudo certbot --nginx -d yourdomain.com
```

---

### Option C: Docker & Docker Compose

Create a `docker-compose.yml` in the project root:

```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    volumes:
      - ./backend/app/dharma_decisions.db:/app/app/dharma_decisions.db
    restart: unless-stopped

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "80:80"
    depends_on:
      - backend
    restart: unless-stopped
```

#### Backend `backend/Dockerfile`:
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
RUN python -m app.seed_data
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Frontend `frontend/Dockerfile`:
```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## 4. Health Checks & Verification

After deployment, verify that both the backend and frontend are healthy:

1. **API Health Check**:
   ```bash
   curl http://127.0.0.1:8000/api/health
   # Expected response: {"status": "healthy", ...}
   ```
2. **List Cases**:
   ```bash
   curl http://127.0.0.1:8000/api/cases
   # Returns the 6 BORI critical edition cases
   ```
3. **A Question for the Gita Endpoints**:
   ```bash
   # List verified verses
   curl http://127.0.0.1:8000/api/gita/verses

   # Test perspective retrieval
   curl -X POST http://127.0.0.1:8000/api/gita/perspective \
     -H "Content-Type: application/json" \
     -d '{"question": "I am afraid I will fail."}'
   ```
4. **Frontend Asset Delivery**:
   Visit the configured URL in your browser. Verify that the editorial homepage loads with Newsreader typography, paper background (`#F8F5ED`), and smooth navigation through `#explore`, `#gita`, `#story/:id`, and `#decide/:id`.
