#!/bin/bash

# End a process by name. Accepts a cmd line arg, name of the process.
# The PID will then be automatically located from the active process lists
# When attempting to terminate, the script will check if this was successful.

endProcess() {
    if [ -z "$1" ]; then
        echo "Usage: endProcess <process_name>"
        return 1
    fi

    # Find the first PID, excluding the script's own PID
    pid=$(pgrep -f "$1" | grep -v "$$" | head -n 1)

    if [ -z "$pid" ]; then
        echo "No process with name '$1' found"
        return 1
    fi

    # Kill the process
    echo "Killing process '$1' with PID $pid"
    kill "$pid"
    if [ $? -eq 0 ]; then
        echo "Process $pid terminated"
    else
        echo "Failed to terminate process $pid"
    fi
}

endProcess "$1"