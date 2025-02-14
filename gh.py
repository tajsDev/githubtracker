import requests
import sys

def main():
    user = sys.argv[1]
    x = requests.get(f"https://api.github.com/users/{user}/events")
    print(x.text)

main()


