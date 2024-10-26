#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_codes_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
valid_status_codes = set(status_codes_count.keys())
line_count = 0

def print_stats():
    """Function to print the metrics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def parse_line(line):
    """Parse a line and update the metrics if the format is correct"""
    global total_file_size, status_codes_count
    try:
        parts = line.split()
        if len(parts) < 7:
            return

        # Extract status code and file size
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update total file size
        total_file_size += file_size

        # Update status code count if it is valid
        if status_code in valid_status_codes:
            status_codes_count[status_code] += 1

    except (IndexError, ValueError):
        # Ignore lines with incorrect format or conversion errors
        pass

def handle_interrupt(signal, frame):
    """Handle KeyboardInterrupt (CTRL + C)"""
    print_stats()
    sys.exit(0)

# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_interrupt)

# Main loop to read stdin
for line in sys.stdin:
    parse_line(line.strip())
    line_count += 1

    # Print stats every 10 lines
    if line_count % 10 == 0:
        print_stats()
