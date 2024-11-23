#!/usr/bin/python3

"""
Python 3 interpreter
"""

import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

def print_stats():
    """Print the current metrics."""
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

def parse_line(line):
    """
    Parse a single line of log input.

    Expected format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    global total_size
    try:
        # Split the line into components
        parts = line.split()
        # Get status code and file size
        status_code = parts[-2]
        file_size = int(parts[-1])
        # Update metrics
        if status_code in status_counts:
            status_counts[status_code] += 1
        total_size += file_size
    except (IndexError, ValueError):
        # Skip malformed lines
        pass

def handle_interrupt(signal, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register signal handler for CTRL+C
signal.signal(signal.SIGINT, handle_interrupt)

if __name__ == "__main__":
    line_count = 0
    try:
        for line in sys.stdin:
            parse_line(line.strip())
            line_count += 1
            if line_count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        handle_interrupt(None, None)
    finally:
        print_stats()


