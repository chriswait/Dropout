# Dropout
Outputs and/or logs internet connection state

## Usage:
./dropout.py

## Behaviour
Dropout periodically makes a HEAD request to a specified host to check for internet connection.
Depending on the resulting connection state, Dropout can output or log the result to a specified csv file.
For both logging and outputting, we can opt to record failures, changes, or everything.

By default:
* Dropout attempts to reach www.google.com.au every 5 seconds
* If it cannot, it outputs a 0
* When the state changes, it appends a csv row to log.csv with a unix timestamp and the new state

```python
# Configuration
## Network
host = "www.google.com.au"
timeout_seconds = 5
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
```
