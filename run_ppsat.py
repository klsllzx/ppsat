import subprocess
import glob
import re
# Directory containing dimacs files
dimacs_files = glob.glob("./ssa-2/*.dimacs")

# Fixed arguments
port = "12345"
limit = "20"
print("Running ppsat_exec on dimacs files",flush=True)

def find_one_step_time(out1:str,filepath:str):
    """
    Find the time taken for one step in the output of ppsat_exec.
    """
    lines = out1.splitlines()
    for line in lines:
        match = re.search(r"one step time:\s*([0-9.]+)\s*seconds", line)
        if match:
            time_value = float(match.group(1))
            with open(f"{filepath}_time", "w") as f:
                f.write(f"{time_value}\n")
    return None


for filepath in dimacs_files:

    print(f"Running on {filepath}",flush=True)

    # Commands for mode 2 and mode 1
    cmd1 = ["./build/src/ppsat_exec", "2", port, limit, filepath]
    cmd2 = ["./build/src/ppsat_exec", "1", port, limit, filepath]

    # Start both processes
    p1 = subprocess.Popen(cmd1,  text=True, start_new_session=True)
    p2 = subprocess.Popen(cmd2, text=True, start_new_session=True)
    # print("waiting for both processes to finish...")
    # # Wait for both to finish and collect outputs
    # out1, err1 = p1.communicate()

    # out2, err2 = p2.communicate()
    # find_one_step_time(out1, filepath)
    # print(f"[2] STDOUT:\n{out1}")
    # print(f"[2] STDERR:\n{err1}")
    # print(f"[1] STDOUT:\n{out2}")
    # print(f"[1] STDERR:\n{err2}")
    p1.wait()
    p2.wait()
    print(f"Finished running on {filepath}",flush=True)
    print("=" * 80,flush=True)

