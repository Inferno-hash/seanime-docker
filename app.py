import os
import subprocess

# Start the application using the command defined in the Dockerfile
if __name__ == "__main__":
    subprocess.run(["/usr/bin/supervisord", "-c", "/config/Supervisord/supervisord.conf"])
