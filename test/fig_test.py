from pyfiglet import figlet_format as fig
from colorama import init, Fore,Style
init(autoreset=True)

cmd = f"{Fore.YELLOW}" + r"print(fig(f'{Fore.YELLOW}Hello, world!'))" + Style.RESET_ALL

print(f"\ncommand: {cmd}\n", fig(f"{Fore.YELLOW}Hello, world!"))

cmd = f"{Fore.YELLOW}" + r"print(Fore.YELLOW + fig(f'Hello, world!'))" + Style.RESET_ALL

print(f"\ncommand: {cmd}\n", Fore.YELLOW + fig(f"Hello, world!"))