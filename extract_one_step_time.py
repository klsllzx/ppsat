import re
file = "running.log"
pattern = r"^Running on (\./ssa-2/.*\.dimacs)"
with open(file, "r") as f:
    record_time = False
    for line in f:
        match = re.match(pattern, line)
        if match:
            filaname = match.group(1)
            record_time = True
        if record_time:
            match = re.search(r"one step time:\s*([0-9.]+)\s*seconds", line)
            if match:
                time_value = float(match.group(1))
                with open(f"{filaname}_time", "w") as f:
                    f.write(f"{time_value}\n")


            