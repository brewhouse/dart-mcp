#!/usr/bin/env python3
"""Deployment script for DART MCP Remote Server."""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"Error: {e.stderr}")
        sys.exit(1)

def main():
    """Main deployment function."""
    print("🚀 Starting DART MCP Remote Server deployment...")
    
    # Check if we're in the right directory
    if not os.path.exists("pyproject.toml"):
        print("❌ Error: pyproject.toml not found. Please run from the project root.")
        sys.exit(1)
    
    # Install dependencies
    run_command("pip install -e .", "Installing dependencies")
    
    # Build package
    run_command("python -m build", "Building package")
    
    # Test the server locally
    print("🧪 Testing server locally...")
    print("To test locally, run:")
    print("  python -m dart_mcp.remote_server")
    print("  or")
    print("  uvicorn dart_mcp.remote_server:app --host 0.0.0.0 --port 8000")
    print()
    
    # Deployment instructions
    print("📋 Deployment Instructions:")
    print()
    print("1. Railway (Recommended):")
    print("   - Install Railway CLI: npm install -g @railway/cli")
    print("   - Run: railway login")
    print("   - Run: railway init")
    print("   - Run: railway up")
    print()
    print("2. Render:")
    print("   - Push to GitHub")
    print("   - Connect repository to Render")
    print("   - Use render.yaml configuration")
    print()
    print("3. Fly.io:")
    print("   - Install flyctl: https://fly.io/docs/getting-started/installing-flyctl/")
    print("   - Run: flyctl launch")
    print("   - Run: flyctl deploy")
    print()
    print("4. Heroku:")
    print("   - Install Heroku CLI")
    print("   - Run: heroku create dart-mcp-server")
    print("   - Run: git push heroku main")
    print()
    print("🎯 Your MCP server will be available at:")
    print("   https://your-app-name.railway.app (Railway)")
    print("   https://dart-mcp-server.onrender.com (Render)")
    print("   https://your-app.fly.dev (Fly.io)")
    print("   https://dart-mcp-server.herokuapp.com (Heroku)")

if __name__ == "__main__":
    main()
