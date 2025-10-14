"""Remote HTTP server for DART MCP tools."""

from __future__ import annotations

import asyncio
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .server import next_trains, list_stations, list_routes

app = FastAPI(
    title="DART MCP Server",
    description="Model Context Protocol server for DART (Dallas Area Rapid Transit) schedules",
    version="0.1.0"
)


class NextTrainsRequest(BaseModel):
    origin: str
    destination: str
    when_iso: Optional[str] = None


class MCPResponse(BaseModel):
    success: bool
    data: str
    error: Optional[str] = None


@app.get("/")
async def root():
    """Root endpoint with server information."""
    return {
        "name": "DART MCP Server",
        "version": "0.1.0",
        "description": "Model Context Protocol server for DART bus schedules",
        "tools": [
            "next_trains",
            "list_stations", 
            "list_routes"
        ],
        "endpoints": {
            "next_trains": "POST /mcp/next_trains",
            "list_stations": "GET /mcp/stations",
            "list_routes": "GET /mcp/routes"
        }
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/mcp/next_trains", response_model=MCPResponse)
async def mcp_next_trains(request: NextTrainsRequest):
    """
    Get next DART bus departures.
    
    Args:
        request: NextTrainsRequest with origin, destination, and optional when_iso
        
    Returns:
        MCPResponse with bus schedule information
    """
    try:
        result = await next_trains(
            request.origin, 
            request.destination, 
            request.when_iso
        )
        return MCPResponse(success=True, data=result)
    except Exception as e:
        return MCPResponse(
            success=False, 
            data="", 
            error=f"Error getting next trains: {str(e)}"
        )


@app.get("/mcp/stations", response_model=MCPResponse)
async def mcp_list_stations():
    """
    List all available DART bus stops.
    
    Returns:
        MCPResponse with list of bus stops
    """
    try:
        result = await list_stations()
        return MCPResponse(success=True, data=result)
    except Exception as e:
        return MCPResponse(
            success=False, 
            data="", 
            error=f"Error listing stations: {str(e)}"
        )


@app.get("/mcp/routes", response_model=MCPResponse)
async def mcp_list_routes():
    """
    List all available DART bus routes.
    
    Returns:
        MCPResponse with list of bus routes
    """
    try:
        result = await list_routes()
        return MCPResponse(success=True, data=result)
    except Exception as e:
        return MCPResponse(
            success=False, 
            data="", 
            error=f"Error listing routes: {str(e)}"
        )


@app.get("/mcp/tools")
async def mcp_tools():
    """
    List available MCP tools and their schemas.
    
    Returns:
        Dictionary of available tools with their schemas
    """
    return {
        "tools": [
            {
                "name": "next_trains",
                "description": "Get next DART bus departures from origin to destination",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "origin": {
                            "type": "string",
                            "description": "Origin stop name (e.g., 'DART')"
                        },
                        "destination": {
                            "type": "string", 
                            "description": "Destination route name (e.g., 'UNIVERSITY')"
                        },
                        "when_iso": {
                            "type": "string",
                            "description": "Optional ISO-8601 datetime (default: now)"
                        }
                    },
                    "required": ["origin", "destination"]
                }
            },
            {
                "name": "list_stations",
                "description": "List all available DART bus stops",
                "input_schema": {
                    "type": "object",
                    "properties": {}
                }
            },
            {
                "name": "list_routes", 
                "description": "List all available DART bus routes",
                "input_schema": {
                    "type": "object",
                    "properties": {}
                }
            }
        ]
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
