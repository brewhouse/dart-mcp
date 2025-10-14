#!/usr/bin/env python3
"""Setup script for DART MCP Server."""

import subprocess
import sys
import os

def install_dependencies():
    """Install required dependencies."""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def main():
    """Main setup function."""
    print("🚀 DART MCP Server Setup")
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Test import
    try:
        import fastapi
        import uvicorn
        print("✅ All dependencies available")
    except ImportError as e:
        print(f"❌ Import test failed: {e}")
        sys.exit(1)
    
    print("🎉 Setup completed successfully!")

if __name__ == "__main__":
    main()
