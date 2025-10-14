# 🚀 Final DART MCP Deployment Guide

After multiple deployment attempts, here's the definitive guide to get your DART MCP server deployed successfully.

## 🎯 **Recommended Approach: Manual Render Setup**

Since automatic deployments have been problematic, we'll use manual configuration:

### **Step 1: Go to Render Dashboard**
1. Visit [render.com](https://render.com)
2. Sign up/Login with GitHub
3. Click "New +" → "Web Service"

### **Step 2: Connect Repository**
1. Connect GitHub repository: `brewhouse/dart-mcp`
2. Select branch: `main`

### **Step 3: Configure Service (CRITICAL)**
```
Name: dart-mcp-server
Environment: Python 3
Region: Oregon (US West)
Branch: main
Root Directory: (leave empty)
```

### **Step 4: Build & Deploy Settings (CRITICAL)**
```
Build Command: echo "No build needed - dependencies installed at runtime"
Start Command: python3 main.py
```

### **Step 5: Environment Variables**
```
PORT = 8000
```

### **Step 6: Health Check**
```
Health Check Path: /health
```

### **Step 7: Deploy**
1. Click "Create Web Service"
2. Wait for deployment (2-3 minutes)
3. Monitor the logs

## 🧪 **Test Your Deployment**

Once deployed, test these endpoints:

```bash
# Health check
curl https://dart-mcp-server.onrender.com/health

# Test endpoint
curl https://dart-mcp-server.onrender.com/test

# List routes
curl https://dart-mcp-server.onrender.com/mcp/routes

# List stations
curl https://dart-mcp-server.onrender.com/mcp/stations

# List tools
curl https://dart-mcp-server.onrender.com/mcp/tools
```

## 🎯 **For CustomGPT.ai**

Use your Render URL as the MCP server URL:
```
https://dart-mcp-server.onrender.com
```

## 🔧 **Alternative Platforms (If Render Fails)**

### **Railway**
1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository: `brewhouse/dart-mcp`
3. Use `Dockerfile.simple` and `start_server.py`

### **Fly.io**
1. Go to [fly.io](https://fly.io)
2. Connect GitHub repository: `brewhouse/dart-mcp`
3. Use `main.py` as the entry point

### **Heroku**
1. Go to [heroku.com](https://heroku.com)
2. Connect GitHub repository: `brewhouse/dart-mcp`
3. Use `Procfile` with `python3 main.py`

## 📋 **Available Files for Deployment**

- **`main.py`** - Completely standalone server (RECOMMENDED)
- **`app.py`** - Simple FastAPI app
- **`run_server.py`** - Server with auto-install
- **`start_server.py`** - Server with debugging
- **`Procfile`** - Heroku compatibility
- **`Dockerfile.simple`** - Docker deployment
- **`render.yaml`** - Render configuration

## 🚨 **Troubleshooting**

### **If deployment still fails:**

1. **Check the logs** for specific error messages
2. **Try different start commands**:
   - `python3 main.py`
   - `python3 app.py`
   - `python3 run_server.py`
3. **Verify file structure** - ensure files are in the root directory
4. **Check environment variables** - ensure PORT is set
5. **Try different platforms** - Railway, Fly.io, or Heroku

### **Common Issues:**
- **Module not found**: Use `main.py` (completely standalone)
- **Port binding**: Ensure PORT environment variable is set
- **Health check fails**: Wait 30-60 seconds for startup
- **Build timeout**: Use minimal build commands

## 🎉 **Success Indicators**

You'll know deployment succeeded when you see:
```
🚀 Starting DART MCP Server...
📍 Host: 0.0.0.0
🔌 Port: [assigned port]
✅ Dependencies already installed
✅ FastAPI app created successfully
🎯 Starting server on 0.0.0.0:[port]
INFO: Uvicorn running on http://0.0.0.0:[port]
```

## 📞 **Support**

If you continue having issues:
1. **Check platform documentation**: Render, Railway, Fly.io docs
2. **Try different platforms**: Each has different strengths
3. **Use manual setup**: Gives you full control over configuration

---

**🎯 The manual Render setup with `main.py` should work reliably. This approach eliminates all external dependencies and module import issues.**
