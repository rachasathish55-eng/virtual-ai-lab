
import sys
import subprocess


    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    return {
        'status': 'success' if result.returncode == 0 else 'error',
        'output': result.stdout + result.stderr
    }
