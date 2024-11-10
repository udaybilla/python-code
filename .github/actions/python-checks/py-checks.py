import subprocess
import sys

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(result.stdout.decode('utf-8'))
        print(result.stderr.decode('utf-8'))
        sys.exit(result.returncode)
    else:
        print(result.stdout.decode('utf-8'))

def main():
    # Run pylint for linting and code quality checks
    run_command("pylint **/*.py")

if __name__ == "__main__":
    main()