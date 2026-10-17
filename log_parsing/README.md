# Log Parsing

0-stats.py reads web server log lines from standard input, skips malformed lines, and prints accumulated file size and supported HTTP status counts every 10 lines. Pending statistics are printed at end of input or when interrupted with Ctrl+C.
