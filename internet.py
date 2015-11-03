#!/usr/local/bin/python
import httplib
import time
import sys

# Network
host = "www.google.com.au"
timeout_seconds = 5
period = 5

# Logging
log_path = 'log.csv'
csv_row_format = "%i,%i"
log_failures = False
log_changes = False
log_all = False

# Output
output_failures = False
output_changes = False
output_all = True

previous_state = None

def internet_on():
    conn = httplib.HTTPConnection(host)
    try:
        conn.request("HEAD", "/")
        return True
    except:
        return False

def should_output(state):
    return ((output_all) or (output_changes and state != previous_state) or (output_failures and state == False))

def should_log(state):
    return ((log_all) or (log_changes and state != previous_state) or (log_failures and state == False))

while True:
    with open(log_path, 'a') as csvFile:
        timestamp = int(time.time())
        state = int(internet_on())
        try:
            row = (csv_row_format + "\n") % (timestamp, state)
        except ValueError as error:
            print "Invalid row format"
            sys.exit()

        # output
        if should_output(state):
            print state

        # logging
        if should_log(state):
            csvFile.write(row)
            csvFile.close()

        if (previous_state != state): previous_state = state
        time.sleep(period)
