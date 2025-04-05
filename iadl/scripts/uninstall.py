import subprocess
import sys

DEPENDENCIES = ["requests", "beautifulsoup4", "tqdm"]

def uninstall_dependencies():
    """
    Uninstall dependencies
    """
    for dep in DEPENDENCIES:
        subprocess.check_call([sys.executable, "-m", "pip", "uninstall", "-y", dep])
        print(f"Uninstalled {dep}")


def main():
    print("Cleaning up dependencies...")
    uninstall_dependencies()

if __name__ == "__main__":
    main()