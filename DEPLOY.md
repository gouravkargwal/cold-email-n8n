# Free Hosting Guide for n8n

## Option 1: Railway (Recommended - Easiest)

### Steps:

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub (free)

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"

3. **Connect Your Repository**
   - Push this project to GitHub
   - Connect the repo to Railway

4. **Deploy Configuration**
   - Railway will auto-detect Docker
   - Or use the `railway.json` config below

5. **Set Environment Variables**
   - In Railway dashboard → Variables:
     ```
     N8N_BASIC_AUTH_ACTIVE=false
     N8N_HOST=0.0.0.0
     N8N_PORT=5678
     ```

6. **Add Volume for Data Persistence**
   - Railway → Settings → Volumes
   - Mount `/home/node/.n8n` for workflow storage

**Cost:** Free $5 credit/month (enough for n8n)

---

## Option 2: Render

### Steps:

1. **Create Render Account**
   - Go to https://render.com
   - Sign up (free)

2. **Create New Web Service**
   - Connect GitHub repo
   - Select "Docker"
   - Use `docker-compose.yml`

3. **Environment Variables**
   ```
   N8N_BASIC_AUTH_ACTIVE=false
   N8N_HOST=0.0.0.0
   N8N_PORT=5678
   ```

4. **Free Tier Limitations**
   - Service may sleep after 15 min inactivity
   - Wakes up on first request
   - Good for scheduled workflows

**Cost:** Free (with limitations)

---

## Option 3: Fly.io

### Steps:

1. **Install Fly CLI**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Create Account**
   ```bash
   fly auth signup
   ```

3. **Create Fly App**
   ```bash
   fly launch
   ```

4. **Deploy**
   ```bash
   fly deploy
   ```

**Cost:** Free tier available

---

## Option 4: Oracle Cloud (Always Free)

### Steps:

1. **Sign up** at https://cloud.oracle.com
   - Requires credit card (won't charge on free tier)

2. **Create Always Free VM**
   - Ubuntu 22.04
   - 1 OCPU, 1GB RAM

3. **SSH into VM and install:**
   ```bash
   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   
   # Install Docker Compose
   sudo apt install docker-compose -y
   
   # Clone your repo
   git clone <your-repo>
   cd cold-email-n8n
   
   # Start n8n
   docker-compose up -d
   ```

4. **Open Firewall Port**
   - Oracle Cloud → Networking → Security Lists
   - Allow port 5678

**Cost:** Always free (no credit card charges)

---

## Quick Setup Script for Railway

Create `railway.json`:

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "DOCKERFILE",
    "dockerfilePath": "Dockerfile"
  },
  "deploy": {
    "startCommand": "docker-compose up",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

Or use Railway's Dockerfile detection with `docker-compose.yml`.

---

## Important Notes:

1. **Data Persistence**: Use Railway volumes or external storage for workflows
2. **File Access**: Upload CSV files via n8n UI or use external storage (S3, etc.)
3. **Monitoring**: Check Railway/Render dashboard for logs
4. **Backup**: Export workflows regularly from n8n

---

## Recommended: Railway

**Why Railway:**
- ✅ Easiest setup
- ✅ Free $5 credit/month
- ✅ Stays awake 24/7
- ✅ Auto-deploys from GitHub
- ✅ Built-in monitoring

**Quick Start:**
1. Push code to GitHub
2. Connect to Railway
3. Deploy
4. Done!

