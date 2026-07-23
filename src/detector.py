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

