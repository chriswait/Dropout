#!/usr/local/bin/python
import urllib2
import httplib
import time

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

def internet_on():
    conn = httplib.HTTPConnection(host)
    try:
        conn.request("HEAD", "/")
        return True
    except:
        return False

def should_output(state, previous_state):
        return ((output_all) or (output_changes and state != previous_state) or (output_failures and state == False))

def should_log(state, previous_state):
        return ((log_all) or (log_changes and state != previous_state) or (log_failures and state == False))

previous_state = None
while True:
    with open(log_path, 'a') as csvFile:
        timestamp = int(time.time())
        state = int(internet_on())
        row = (csv_row_format + "\n") % (timestamp, state)

        # output
        if should_output(state, previous_state):
            print state

        # logging
        if should_log(state, previous_state):
            csvFile.write(row)
            csvFile.close()

        if (previous_state != state): previous_state = state
        time.sleep(period)
