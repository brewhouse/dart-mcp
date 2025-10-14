"""Standalone DART MCP Server for deployment."""

from fastapi import FastAPI
from datetime import datetime
import os

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

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get('PORT', 8000))
    print(f"🚀 Starting DART MCP Server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
