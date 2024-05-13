import sys
import logging

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG)

def read_log():
    """
    Reads all lines of the input at once, splits each line into separate attributes,
    converts strings to the proper data type, and stores each entry as a tuple.
    """
    log_entries = []
    lines = sys.stdin.readlines()  # Read all lines from standard input
    logging.debug(f"Number of lines read: {len(lines)}")  # Log number of lines read
    for line in lines:
        if line.strip():  # Check if the line is not empty
            entry = tuple(line.split())  # Split the line into attributes
            # Convert necessary attributes to proper data types
            entry = (entry[0], int(entry[1]), entry[2], int(entry[3]))
            log_entries.append(entry)  # Add entry to log_entries list
    logging.debug(f"Number of entries in the list: {len(log_entries)}")  # Log number of entries
    return log_entries

def successful_reads(log_entries):
    """
    Takes a list of all entries in the log, filters successful reads (HTTP result codes 2xx),
    logs the number of successful reads, and returns a new list containing only successful reads.
    """
    success_entries = [entry for entry in log_entries if 200 <= entry[1] < 300]  # Filter successful reads
    logging.info(f"Number of successful reads: {len(success_entries)}")  # Log number of successful reads
    return success_entries

def failed_reads(log_entries):
    """
    Takes a list of all entries in the log, separates entries with HTTP codes 4xx and 5xx,
    merges both lists, logs the number of entries with 4xx and 5xx result codes, and
    returns the merged list.
    """
    # Filter entries with 4xx and 5xx codes separately
    failed_4xx = [entry for entry in log_entries if 400 <= entry[1] < 500]
    failed_5xx = [entry for entry in log_entries if 500 <= entry[1] < 600]
    # Merge both lists
    merged_failed = failed_4xx + failed_5xx
    # Log number of entries with 4xx and 5xx codes
    logging.info(f"Number of entries with 4xx codes: {len(failed_4xx)}")
    logging.info(f"Number of entries with 5xx codes: {len(failed_5xx)}")
    return merged_failed

def html_entries(log_entries):
    """
    Returns a list containing entries of successfully retrieved pages with .html extension.
    """
    # Filter entries with .html extension
    html_entries = [entry for entry in log_entries if entry[0].endswith('.html')]
    return html_entries

def print_html_entries(html_entries):
    """
    Prints a list containing entries of successfully retrieved pages with .html extension.
    """
    for entry in html_entries:
        print(entry)

def run():
    """
    Main function to run the program. Reads the log, performs operations, and prints results.
    """
    log_entries = read_log()  # Read log entries
    successful = successful_reads(log_entries)  # Filter successful reads
    failed = failed_reads(log_entries)  # Filter failed reads
    html = html_entries(successful)  # Filter HTML entries from successful reads
    print_html_entries(html)  # Print HTML entries

# Check if the script is run directly
if __name__ == "__main__":
    
    run()  # Call the main function
