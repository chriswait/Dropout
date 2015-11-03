#!/usr/local/bin/python
from httplib import HTTPConnection
from time import time, sleep
from sys import exit
# Configuration
## Network
host = "www.google.com.au"
period = 5
## Logging
log_path = 'log.csv'
csv_row_format = "%i,%i"
log_failures = False
log_changes = True
log_all = False
## Output
output_failures = True
output_changes = False
output_all = False

def internet_on():
    conn = HTTPConnection(host)
    try:
        conn.request("HEAD", "/")
        return True
    except Exception: return False

def should_output(state): return ((output_all) or (output_changes and state != previous_state) or (output_failures and state == False))
def should_log(state): return ((log_all) or (log_changes and state != previous_state) or (log_failures and state == False))

def error(message): exit("Error: " + message)

previous_state = None
if (should_log(True) and not(log_path)): error("Logging enabled but no path set")

while True:
    timestamp = int(time())
    state = int(internet_on())
    # output
    if should_output(state): print state
    # logging
    if should_log(state):
        try:
            with open(log_path, 'a') as csv_file:
                try: row = (csv_row_format + "\n") % (timestamp, state)
                except ValueError: error("Invalid row format")
                csv_file.write(row)
                csv_file.close()
        except Exception: error("Failed to open log file")
    if (previous_state != state): previous_state = state
    sleep(period)
