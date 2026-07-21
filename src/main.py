from detector import detect_failed_logins
from parser import parse_log_line

def main():
    parsed_logs = []

    with open("logs/sample.log", "r") as file:
        for line in file:
            result = parse_log_line(line)

            if result:
                parsed_logs.append(result)

    print(parsed_logs)

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