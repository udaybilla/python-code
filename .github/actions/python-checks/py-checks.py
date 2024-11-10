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
    if len(sys.argv) < 2:
        print("Usage: python py-checks.py <file1> <file2> ...")
        sys.exit(1)

    files = sys.argv[1:]
    for file in files:
        # Run pylint for linting and code quality checks on each file
        run_command(f"pylint {file}")

if __name__ == "__main__":
    main()