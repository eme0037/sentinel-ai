def detect_failed_logins(parsed_logs):
    """
    Counts failed login attempts (HTTP 401) for each IP address.

    Args:
        parsed_logs (list): A list of parsed log dictionaries.

    Returns:
        dict: A dictionary where the key is the IP address and the value is
              the number of failed login attempts.
    """

    failed_logins = {}

    for log in parsed_logs:

        # Only count failed login attempts
        if log["status"] == 401:
            ip = log["ip"]

            # Increase the count for this IP
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

    return failed_logins

def detect_directory_scans(parsed_logs):

    pages_by_ip = {}

    for log in parsed_logs:
        ip = log["ip"]
        path = log["path"]

        if ip not in pages_by_ip:
            pages_by_ip[ip] = set()

        pages_by_ip[ip].add(path)

    return pages_by_ip