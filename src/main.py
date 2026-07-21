def main():
    with open("logs/sample.log", "r") as file:
        for line in file:
            print(line.strip())

if __name__ == "__main__":
    main()