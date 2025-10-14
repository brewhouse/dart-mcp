#!/usr/bin/env python3
"""Startup script for DART MCP server."""

import os
import sys

def main():
    """Main startup function."""
    port = os.environ.get('PORT', '8000')
    host = '0.0.0.0'
    
    print(f"🚀 Starting DART MCP Server...")
    print(f"📍 Host: {host}")
    print(f"🔌 Port: {port}")
    print(f"🌐 Environment: {os.environ.get('RAILWAY_ENVIRONMENT', 'local')}")
    
    try:
        # Try to import and start the simple server
        from dart_mcp.simple_server import app
        print("✅ Successfully imported simple server")
        
        import uvicorn
        print("✅ Successfully imported uvicorn")
        
        print(f"🎯 Starting server on {host}:{port}")
        uvicorn.run(
            app, 
            host=host, 
            port=int(port), 
            workers=1,
            log_level="info"
        )
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Server error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
