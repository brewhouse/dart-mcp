# 🚀 DART MCP Remote Server Deployment Guide

This guide will help you deploy your DART MCP server to work with CustomGPT.ai and other remote MCP clients.

## 📋 What We've Built

Your DART MCP now includes:
- ✅ **Local MCP Server**: `dart-mcp` (original functionality)
- ✅ **Remote HTTP Server**: `dart-mcp-server` (new for CustomGPT.ai)
- ✅ **FastAPI Endpoints**: REST API for MCP tools
- ✅ **Docker Support**: Containerized deployment
- ✅ **Multiple Platform Configs**: Railway, Render, Fly.io, Heroku

## 🔧 Available Endpoints

Your remote server provides these HTTP endpoints:

### **Base Endpoints**
- `GET /` - Server information and available tools
- `GET /health` - Health check endpoint
- `GET /mcp/tools` - List available MCP tools with schemas

### **MCP Tool Endpoints**
- `POST /mcp/next_trains` - Get next bus departures
- `GET /mcp/stations` - List all bus stops
- `GET /mcp/routes` - List all bus routes

## 🚀 Deployment Options

### **Option 1: Railway (Recommended) 🚄**

Railway is the easiest and most reliable option:

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway:**
   ```bash
   railway login
   ```

3. **Deploy:**
   ```bash
   railway init
   railway up
   ```

4. **Get your URL:**
   ```bash
   railway domain
   ```
   Your server will be at: `https://your-app-name.railway.app`

### **Option 2: Render 🌐**

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add remote server support"
   git push origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Connect your GitHub repository
   - Use the `render.yaml` configuration
   - Your server will be at: `https://dart-mcp-server.onrender.com`

### **Option 3: Fly.io ✈️**

1. **Install flyctl:**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Deploy:**
   ```bash
   flyctl launch
   flyctl deploy
   ```

3. **Get your URL:**
   ```bash
   flyctl info
   ```
   Your server will be at: `https://your-app.fly.dev`

### **Option 4: Heroku 🟣**

1. **Install Heroku CLI:**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   ```

2. **Deploy:**
   ```bash
   heroku create dart-mcp-server
   git push heroku main
   ```

3. **Your server will be at:** `https://dart-mcp-server.herokuapp.com`

## 🧪 Testing Your Deployment

Once deployed, test your server:

### **1. Health Check:**
```bash
curl https://your-server-url/health
```

### **2. List Available Tools:**
```bash
curl https://your-server-url/mcp/tools
```

### **3. Get Bus Routes:**
```bash
curl https://your-server-url/mcp/routes
```

### **4. Get Next Trains:**
```bash
curl -X POST https://your-server-url/mcp/next_trains \
  -H "Content-Type: application/json" \
  -d '{"origin": "DART", "destination": "UNIVERSITY"}'
```

## 🔗 Using with CustomGPT.ai

1. **Get your server URL** from the deployment platform
2. **In CustomGPT.ai:**
   - Go to MCP configuration
   - Enter your server URL (e.g., `https://your-app.railway.app`)
   - The server will be available at the base URL

### **Example CustomGPT.ai Configuration:**

```
MCP Server URL: https://dart-mcp-server.railway.app
```

## 📊 Server Response Format

All endpoints return JSON in this format:

```json
{
  "success": true,
  "data": "Formatted response text",
  "error": null
}
```

## 🔍 Monitoring & Debugging

### **Check Server Logs:**
- **Railway:** `railway logs`
- **Render:** Dashboard → Logs
- **Fly.io:** `flyctl logs`
- **Heroku:** `heroku logs --tail`

### **Test Endpoints:**
```bash
# Test all endpoints
curl https://your-server-url/
curl https://your-server-url/health
curl https://your-server-url/mcp/tools
curl https://your-server-url/mcp/stations
curl https://your-server-url/mcp/routes
```

## 🚨 Troubleshooting

### **Common Issues:**

1. **Server won't start:**
   - Check Python version (needs 3.9+)
   - Verify all dependencies are installed
   - Check logs for specific errors

2. **Endpoints not responding:**
   - Verify server is running on correct port
   - Check firewall/network settings
   - Ensure health check endpoint works

3. **MCP tools not working:**
   - Check GTFS data is accessible
   - Verify pandas is installed
   - Test local server first

### **Local Testing:**
```bash
# Test locally before deploying
uvicorn dart_mcp.remote_server:app --host 0.0.0.0 --port 8000

# In another terminal
curl http://localhost:8000/health
```

## 🎯 Next Steps

1. **Deploy to your chosen platform**
2. **Test all endpoints**
3. **Configure CustomGPT.ai with your server URL**
4. **Monitor logs and performance**

## 📞 Support

If you encounter issues:
1. Check the server logs
2. Test endpoints individually
3. Verify your deployment platform status
4. Check this guide for common solutions

---

**🎉 Congratulations!** Your DART MCP server is now ready for remote access!
