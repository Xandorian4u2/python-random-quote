import random


def main():
    print("Keep it logically awesome.")
    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()
    last = len(quotes) - 1
    rnd = random.randint(0, last)
    print(quotes[rnd])
    print("What was is the file:")
    for i in list(range(len(quotes))):
        print(str(i + 1) + ". " + (quotes[i]))
    print("Change has occurred")


if __name__ == "__main__":
    main()
