from pathlib import Path
import subprocess
import os 
import glob
def process_all_cnf_files(folder_path):
    folder = Path(folder_path)
    dimacs_files = folder.glob('*.dimacs')
    for dimacs_file in dimacs_files:
        print(f"Running ppsat.py on {dimacs_file}")
        # Run the command: python3 ppsat.py <file>
        result = subprocess.run(["python3", "/root/ppsat/py_ppsat/ppsat.py", dimacs_file],
                                capture_output=True, text=True)

        # Print or log the output
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)
        print("-" * 60)

# Example usage:
process_all_cnf_files('ssa-2')  # Replace 'xxx' with your actual folder path