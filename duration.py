import subprocess
import time
import sys

def main():
    # Get the command-line arguments: python_script_path and duration_seconds
    python_script_path = sys.argv[1]
    duration_seconds = int(sys.argv[2])

    # Start the Python script in a separate process
    process = subprocess.Popen(["python", python_script_path])

    # Wait for the specified duration
    time.sleep(duration_seconds)

    # Terminate the process
    process.terminate()

if __name__ == "__main__":
    main()