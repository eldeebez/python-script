import json
import logging
import os

DEFAULT_CONFIG = {
    "log_file_path": "C:/Users/aelde/OneDrive/Desktop/university materials/4th semester/Script languages/SC-lab6/lab6.txt",
    "ip_address": "127.0.0.1",
    "logging_level": "INFO",
    "lines_displayed": 10,
    "custom_parameter": "100"
}

def get_config():
    try:
        with open('C:/Users/aelde/OneDrive/Desktop/university materials/4th semester/Script languages/SC-lab6/lab6.txt', 'r', encoding='utf-8') as file:
            config = json.load(file)
    except FileNotFoundError:
        logging.info("Configuration file does not exist. Using default values.")
        config = DEFAULT_CONFIG
    except json.JSONDecodeError:
        logging.error("Configuration file is not a correct JSON file.")
        raise
    else:
        # Check if all required keys are present in the loaded configuration
        for key in DEFAULT_CONFIG.keys():
            if key not in config:
                logging.info(f"Configuration file does not contain {key}. Using default value.")
                config[key] = DEFAULT_CONFIG[key]
    return config

def setup_logging(logging_level):
    logging.basicConfig(level=logging_level)

def read_log(log_file_path):
    log_data = {}
    with open(log_file_path, 'r') as file:
        for line in file:
            parts = line.split()
            ip_address = parts[0]
            request_string = parts[6]
            if ip_address in log_data:
                log_data[ip_address].append(request_string)
            else:
                log_data[ip_address] = [request_string]
    return log_data

def load_web_server_log(log_file_path):
    if not os.path.exists(log_file_path):
        logging.error(f"Logfile '{log_file_path}' does not exist.")
        raise FileNotFoundError
    log_data = read_log(log_file_path)
    return log_data

def print_requests_from_ip(log_data, ip_address):
    if ip_address not in log_data:
        logging.error(f"IP address {ip_address} not found in log data.")
        return
    for request in log_data[ip_address]:
        print(request)

def print_requests_with_method(log_data, method, lines_displayed):
    if lines_displayed <= 0:
        logging.warning("Number of lines to display is less than or equal to zero.")
        return
    count = 0
    for ip_address, requests in log_data.items():
        for request in requests:
            if method in request:
                print(request)
                count += 1
                if count >= lines_displayed:
                    input("Press any key to continue...")
                    count = 0

def custom_log_processing(log_data, custom_parameter):
    # Custom log processing based on the custom parameter goes here
    pass

def main():
    config = get_config()
    setup_logging(config["logging_level"])

    try:
        log_data = load_web_server_log(config["log_file"])
    except FileNotFoundError:
        logging.error("Exiting application.")
        return

    print_requests_from_ip(log_data, config["ip_address"])
    print_requests_with_method(log_data, config["custom_parameter"], config["lines_displayed"])
    custom_log_processing(log_data, config["custom_parameter"])

if __name__ == "__main__":
    main()
