from detector import detect_failed_logins, detect_directory_scans
from parser import parse_log_line

def main():
    parsed_logs = []

    with open("logs/sample.log", "r") as file:
        for line in file:
            result = parse_log_line(line)

            if result:
                parsed_logs.append(result)

    failed_logins = detect_failed_logins(parsed_logs)
    unique_ips = set(log["ip"] for log in parsed_logs)

    print("=" * 40)
    print("SentinelAI Security Report")
    print("=" * 40)

    print(f"Total Requests: {len(parsed_logs)}")
    print(f"Unique IP Addresses: {len(unique_ips)}")
    print(f"IPs with Failed Logins: {len(failed_logins)}")
    total_failed = sum(failed_logins.values())
    print(f"Total Failed Login Attempts: {total_failed}")

    print("\nPotential Brute-Force Attacks")
    print("-" * 40)

    found_attack = False

    for ip, count in failed_logins.items():
        if count >= 5:
            print(f"ALERT: {ip} -> {count} failed login attempts")
            found_attack = True

    if not found_attack:
        print("No brute-force attacks detected.")


    failed_logins = detect_failed_logins(parsed_logs)

    print("\nFailed Login Summary")
    print("--------------------")

    for ip, count in failed_logins.items():
        print(f"{ip}: {count} failed login(s)")

    print("\nPotential Brute-Force Attacks")
    print("-----------------------------")

    found_attack = False

    for ip, count in failed_logins.items():
        if count >= 5:
            print(f"ALERT: {ip} has {count} failed login attempts!")
            found_attack = True

    if not found_attack:
        print("No brute-force attacks detected.")


if __name__ == "__main__":
    main()