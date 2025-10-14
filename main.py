#!/usr/bin/env python3
"""Main entry point for DART MCP Server - completely standalone."""

import os
import sys

def main():
    """Main function."""
    port = int(os.environ.get('PORT', 8000))
    host = '0.0.0.0'
    
    print(f"🚀 Starting DART MCP Server...")
    print(f"📍 Host: {host}")
    print(f"🔌 Port: {port}")
    print(f"🌐 Environment: {os.environ.get('RAILWAY_ENVIRONMENT', os.environ.get('RENDER', 'local'))}")
    
    try:
        # Install dependencies if needed
        try:
            import fastapi
            import uvicorn
            print("✅ Dependencies already installed")
        except ImportError:
            print("📦 Installing dependencies...")
            os.system("pip install fastapi uvicorn")
            import fastapi
            import uvicorn
            print("✅ Dependencies installed successfully")
        
        # Create the FastAPI app inline
        from fastapi import FastAPI
        from datetime import datetime
        
        app = FastAPI(title="DART MCP Server")
        
        @app.get("/")
        async def root():
            return {"message": "DART MCP Server is running!", "status": "ok"}
        
        @app.get("/health")
        async def health_check():
            return {"status": "healthy", "timestamp": datetime.now().isoformat()}
        
        @app.get("/test")
        async def test_endpoint():
            return {"message": "Test endpoint working!", "status": "ok"}
        
        @app.get("/mcp/routes")
        async def list_routes():
            return {
                "success": True,
                "data": "Available DART bus routes:\n• UNIVERSITY\n• FAIRGROUNDS\n• MAURY ST\n• FRANKLIN AVE\n• E 14TH ST\n• SW 9TH ST\n• INDIANOLA AVE\n• UNIVERSITY / INGERSOLL",
                "error": None
            }
        
        @app.get("/mcp/stations")
        async def list_stations():
            return {
                "success": True,
                "data": "Available DART bus stops:\n• DART Central Station\n• University\n• Fairgrounds\n• Maury St\n• Franklin Ave\n• E 14th St\n• SW 9th St\n• Indianola Ave\n• University / Ingersoll",
                "error": None
            }
        
        @app.get("/mcp/tools")
        async def mcp_tools():
            return {
                "tools": [
                    {
                        "name": "list_routes",
                        "description": "List all available DART bus routes",
                        "input_schema": {"type": "object", "properties": {}}
                    },
                    {
                        "name": "list_stations",
                        "description": "List all available DART bus stops", 
                        "input_schema": {"type": "object", "properties": {}}
                    }
                ]
            }
        
        print("✅ FastAPI app created successfully")
        print(f"🎯 Starting server on {host}:{port}")
        
        uvicorn.run(app, host=host, port=port, log_level="info")
        
    except Exception as e:
        print(f"❌ Server error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
