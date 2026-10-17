#!/usr/bin/python3
"""Read log lines from stdin and print accumulated statistics."""

import re
import sys


STATUS_CODES = ("200", "301", "400", "401", "403", "404", "405", "500")
LOG_PATTERN = re.compile(
    r'^\S+ - \[[^\]]+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)\s*$'
)


def print_stats(total_size, status_counts):
    """Print the total file size and status counts in ascending order."""
    print("File size: {}".format(total_size))
    for code in STATUS_CODES:
        if status_counts[code]:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin, skipping malformed log lines."""
    total_size = 0
    status_counts = {code: 0 for code in STATUS_CODES}
    lines_since_report = 0

    try:
        for line in sys.stdin:
            lines_since_report += 1
            match = LOG_PATTERN.fullmatch(line.rstrip("\n"))

            if match:
                status, size = match.groups()
                total_size += int(size)
                if status in status_counts:
                    status_counts[status] += 1

            if lines_since_report == 10:
                print_stats(total_size, status_counts)
                lines_since_report = 0
    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
    else:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
