def parse_log_line(line):
    parts = line.split()    # split log line into parts

    if len(parts) < 9 or line.startswith("#"):  # Skip blank lines or comments
        return None

    return {
        "ip": parts[0],
        "method": parts[5].replace('"', ''),    # remote quotes
        "path": parts[6],   # returns log path
        "status": int(parts[8])   # returns log status turns into integer
    }