from pathlib import Path
import subprocess

def process_all_dimacs_with_time(folder_path: str):
    folder = Path(folder_path)
    
    # Match *.dimacs files, excluding .dimacs_time
    dimacs_files = sorted(folder.glob('*.dimacs'))
    for dimacs_file in dimacs_files:
        if str(dimacs_file).endswith('.dimacs_time'):
            continue  # Skip time files in main loop

        # Construct the corresponding .dimacs_time file path
        time_file = dimacs_file.with_name(dimacs_file.name + '_time')

        if not time_file.exists():
            print(f"[Warning] Time file not found for: {dimacs_file}")
            continue

        print(f"Running ppsat.py on {dimacs_file.name} and {time_file.name}")
        result = subprocess.run([
            "python3", "/home/ubuntu/ppsat/py_ppsat/ppsat.py",
            str(dimacs_file),
            str(time_file)
        ], capture_output=True, text=True)

        print("STDOUT:\n", result.stdout)
        print("STDERR:\n", result.stderr)
        print("-" * 60)

# Example usage:
process_all_dimacs_with_time('ssa-2')
