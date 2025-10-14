# 🚀 Manual Render Setup Guide

If automatic deployment fails, follow these steps to manually configure Render:

## 📋 **Step-by-Step Manual Setup:**

### **1. Go to Render Dashboard**
- Visit [render.com](https://render.com)
- Sign up/Login with GitHub

### **2. Create New Web Service**
- Click "New +" → "Web Service"
- Connect GitHub repository: `brewhouse/dart-mcp`

### **3. Configure Service Settings**
```
Name: dart-mcp-server
Environment: Python 3
Branch: main
Root Directory: (leave empty)
```

### **4. Build & Deploy Settings**
```
Build Command: pip install fastapi uvicorn
Start Command: python3 app.py
```

### **5. Environment Variables**
```
PORT = 8000
```

### **6. Health Check**
```
Health Check Path: /health
```

### **7. Deploy**
- Click "Create Web Service"
- Wait for deployment to complete

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
```

## 🎯 **For CustomGPT.ai**

Use your Render URL as the MCP server URL:
```
https://dart-mcp-server.onrender.com
```

## 🔧 **Troubleshooting**

If deployment still fails:

1. **Check Build Logs**: Look for specific error messages
2. **Verify Files**: Ensure `app.py` and `requirements.txt` are in the root directory
3. **Try Different Start Command**: Use `python3 run_server.py` instead
4. **Check Dependencies**: Ensure FastAPI and uvicorn are installed

## 📞 **Support**

- **Render Docs**: [render.com/docs](https://render.com/docs)
- **FastAPI Docs**: [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
