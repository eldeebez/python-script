#task 4
def run():
    log_file_path = "C:/Users/aelde/OneDrive/Desktop/university materials/4th semester/Script languages/lab5.txt.txt"
    log_data = read_log(log_file_path)
    
    ip_requests = ip_requests_number(log_data)
    most_active_ips = ip_find(ip_requests, most_active=True)
    least_active_ips = ip_find(ip_requests, most_active=False)
    
    longest_req = longest_request(log_data)
    nonexistent_requests = non_existent(log_data)
    
    print("Most Active IP Addresses:")
    print(most_active_ips)
    print("\nLeast Active IP Addresses:")
    print(least_active_ips)
    print("\nLongest Request:")
    print(longest_req)
    print("\nNon-existent Requests:")
    print(nonexistent_requests)

#task5
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

#task 6
def ip_requests_number(log_data):
    ip_requests = {}
    for ip_address, requests in log_data.items():
        ip_requests[ip_address] = len(requests)
    return ip_requests

#task7
def ip_find(ip_requests, most_active=True):
    sorted_ips = sorted(ip_requests.items(), key=lambda x: x[1], reverse=most_active)
    max_requests = sorted_ips[0][1]
    result_ips = [ip for ip, requests in sorted_ips if requests == max_requests]
    return result_ips

#task 8
def longest_request(log_data):
    longest_req = ""
    longest_ip = ""
    for ip_address, requests in log_data.items():
        for request in requests:
            if len(request) > len(longest_req):
                longest_req = request
                longest_ip = ip_address
    return (longest_ip, longest_req)

#task 9
def non_existent(log_data):
    nonexistent_requests = set()
    for ip_address, requests in log_data.items():
        for request in requests:
            if "404" in request:
                nonexistent_requests.add(request)
    return list(nonexistent_requests)

if __name__ == "__main__":
    run()
