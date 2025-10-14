#!/usr/bin/env python3
"""Simple server runner for deployment."""

import os
import sys

def main():
    """Main function."""
    port = int(os.environ.get('PORT', 8000))
    host = '0.0.0.0'
    
    print(f"🚀 Starting DART MCP Server...")
    print(f"📍 Host: {host}")
    print(f"🔌 Port: {port}")
    
    try:
        # Import and run the app
        from app import app
        import uvicorn
        
        print("✅ App imported successfully")
        print(f"🎯 Starting server on {host}:{port}")
        
        uvicorn.run(app, host=host, port=port, log_level="info")
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("📦 Installing dependencies...")
        os.system("pip install fastapi uvicorn")
        print("🔄 Retrying...")
        from app import app
        import uvicorn
        uvicorn.run(app, host=host, port=port, log_level="info")
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
