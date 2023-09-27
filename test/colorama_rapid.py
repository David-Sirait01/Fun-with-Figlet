from colorama import Fore, Back, init
init(autoreset=True)
def main():
    i = 0
    while True:
        try:
            print(f"{Back.BLUE}Count = {Fore.YELLOW}{i}", end="\r")
            i = i + 1
        except KeyboardInterrupt:
            print("\n\n")
            exit(code=i)
            
main()