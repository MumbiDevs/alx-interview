#!/usr/bin/python3

"""
Python 3 interpreter
"""
import sys
import signal

# Initialize variables to hold total file size and status code counts
total_file_size = 0
status_codes_count = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0

def print_statistics():
    """Function to print the statistics collected so far."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def process_line(line):
    """Process each line and update total file size and status code counts."""
    global total_file_size, line_count
    try:
        # Split line and validate structure
        parts = line.split()
        if len(parts) < 7 or parts[2] != "-" or not parts[3].startswith("[") or not parts[5].startswith('"GET'):
            return  # Skip invalid format

        # Parse file size and status code
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update total file size
        total_file_size += file_size

        # Update status code count if the status code is in our list
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        # Increment line count and print stats every 10 lines
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

    except (ValueError, IndexError):
        # Skip lines that don't match the expected format or have invalid values
        return

# Define signal handler for keyboard interrupt (Ctrl+C)
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from standard input line by line
for line in sys.stdin:
    process_line(line.strip())

