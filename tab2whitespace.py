import re
from pathlib import Path

def convert_tabs_to_spaces(input_file):
    input_path = Path(input_file)
    output_file = input_path.with_suffix('.dimacs')

    with input_path.open('r') as fin, output_file.open('w') as fout:
        for line in fin:
            if line.lstrip().startswith('c'):
                continue  # Skip comment lines
            normalized = re.sub(r'\t', ' ', line)
            fout.write(normalized)

    return output_file

def process_all_cnf_files(folder_path):
    folder = Path(folder_path)
    cnf_files = folder.glob('*.cnf')
    for cnf_file in cnf_files:
        output = convert_tabs_to_spaces(cnf_file)
        print(f"Processed: {cnf_file.name} → {output.name}")

# Example usage:
process_all_cnf_files('ssa-2')  # Replace 'xxx' with your actual folder path