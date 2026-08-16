import uvicorn
import os
import sys

# Configure UTF-8 encoding on standard output for Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

PORT = int(os.getenv("PORT", 8088))

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    print("=================================================================")
    print("Maison d'Or Haute Joaillerie Showcase & Private Owner Studio")
    print(f"Public Showcase:       http://127.0.0.1:{PORT}")
    print(f"Private Owner Studio:  http://127.0.0.1:{PORT}/studio/login")
    print("Default Credentials:   admin / ImperialVault2026!")
    print("=================================================================")
    uvicorn.run("app.main:app", host="127.0.0.1", port=PORT, reload=True)
