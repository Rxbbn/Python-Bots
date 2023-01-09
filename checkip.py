import os

# Open the file with the list of IP addresses
with open('ip_list.txt', 'r') as f:
    # Read the IP addresses from the file
    ip_list = f.readlines()

# Strip the newline characters from the IP addresses
ip_list = [ip.strip() for ip in ip_list]

# Open a file for writing the results
with open('ping_results.txt', 'w') as f:
    # Iterate through the list of IPs
    for ip in ip_list:
        # Use the 'ping' command to send a request to the IP
        response = os.system("ping -n 1 " + ip)
        # If the response is 0, the ping was successful
        if response == 0:
            print(ip + ": Success\n")
        else:
            f.write(ip + ": Failed to connect (on ping test)\n")
