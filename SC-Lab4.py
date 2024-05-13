import sys
from ipaddress import IPv4Address, IPv4Network
from datetime import datetime

# Function to check if an IPv4 address belongs to a network
def check_ip_in_network(ip_address, network):
    """
    Checks if a given IPv4 address belongs to the IPv4 network using IPv4Address and IPv4Network classes.
    """
    return IPv4Address(ip_address) in IPv4Network(network)

# Function to parse timestamp string into datetime object
def parse_timestamp(timestamp_str):
    """
    Parses a timestamp string from the log file and returns a new datetime object.
    """
    timestamp_parts = timestamp_str.split('/')
    day = int(timestamp_parts[0])
    month = timestamp_parts[1]
    month_dict = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
        'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
        'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    month = month_dict[month]
    year = int(timestamp_parts[2].split(':')[0])
    hour = int(timestamp_parts[2].split(':')[1])
    minute = int(timestamp_parts[2].split(':')[2])
    second = int(timestamp_parts[2].split(':')[3])
    return datetime(year, month, day, hour, minute, second)



# Class to represent a single log entry
class LogEntry:
    def __init__(self, ip_address, timestamp, request_method, resource, status_code, response_size):
        self.ip_address = ip_address
        self.timestamp = timestamp
        self.request_method = request_method
        self.resource = resource
        self.status_code = status_code
        self.response_size = response_size

    def __str__(self):
        return f"{self.ip_address} - [{self.timestamp}] \"{self.request_method} {self.resource}\" {self.status_code} {self.response_size}"

    def __repr__(self):
        return f"LogEntry(ip_address={self.ip_address}, timestamp={self.timestamp}, request_method={self.request_method}, resource={self.resource}, status_code={self.status_code}, response_size={self.response_size})"

# Function to create a log entry object from a log line
def create_log_entry(log_line):
    """
    Creates a log entry object from a log line.
    """
    log_parts = log_line.split()
    ip_address = log_parts[0]
    timestamp = parse_timestamp(log_parts[3][1:])  # Remove '[' from the beginning
    request_method = log_parts[5][1:]  # Remove '"' from the beginning
    resource = log_parts[6]
    status_code = int(log_parts[8])
    response_size = int(log_parts[9])
    return LogEntry(ip_address, timestamp, request_method, resource, status_code, response_size)

# Function to read logfile and return a list of log entry objects
def read_logfile(filename):
    """
    Reads the content of the logfile and returns a list of log entry objects.
    """
    log_entries = []
    with open(filename, 'r') as file:
        for line in file:
            log_entries.append(create_log_entry(line))
    return log_entries

# Function to display requests between two given moments in time
def display_requests_between_times(log_entries, start_time, end_time):
    """
    Displays all requests between two given moments in time.
    """
    if end_time < start_time:
        print("Warning: End time is earlier than start time.")
        return
    requests_between_times = [entry for entry in log_entries if start_time <= entry.timestamp <= end_time]
    for request in requests_between_times:
        print(request)
    


# Main function
def main():
    # Task 1: Download logfile from ePortal
    # Assuming the logfile is already downloaded and provided as a command-line argument

    # Task 2: Learn about IPv4Address and IPv4Network classes
    # Documentation link: https://docs.python.org/3/library/ipaddress.html

    # Task 3: Learn about datetime class
    # Documentation link: https://docs.python.org/3/library/datetime.html

    # Task 7: Read logfile and create list of log entry objects
    logfile = sys.argv[1]
    log_entries = read_logfile(logfile)

    # Task 8: Display requests between two given moments in time
    start_time = datetime(2024, 1, 1, 0, 0, 0)
    end_time = datetime(2024, 1, 2, 0, 0, 0)
    display_requests_between_times(log_entries, start_time, end_time)

if __name__ == "__main__":
    main()
