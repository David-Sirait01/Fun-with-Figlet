from colorama import Fore, Back, init, Style

def printmid(text, p=True):
    import os
    # Mendapatkan lebar terminal saat ini
    terminal_width = os.get_terminal_size().columns

    # Menghitung panjang teks yang akan ditampilkan
    text_length = len(text)

    # Menghitung jumlah karakter "-" yang diperlukan untuk mengelilingi teks
    border_length = (terminal_width - text_length - 4) // 2  # 4 adalah untuk tanda "="

    # Membuat garis batas atas
    top_border = "=" * border_length

    # Membuat garis batas bawah
    bottom_border = "=" * (border_length + (text_length % 2))  # Menambahkan satu "=" jika panjang teks ganjil

    # Menampilkan teks di tengah layar dengan batasan atas dan bawah
    content = top_border + f"[{text}]" + bottom_border + ""
    if p == True:
        print(content, end="")
        return content
    else:
        return content
    
    
def main():
    init(autoreset=True)
    printmid(f"{Fore.BLUE} Time stamps {Style.RESET_ALL}")
    arr = [
        f"{Fore.MAGENTA}00:00 {Fore.CYAN} Notes",
        f"{Fore.MAGENTA}00:12 {Style.BRIGHT}{Fore.LIGHTYELLOW_EX} Introduction",
        f"{Fore.MAGENTA}01:21 {Style.BRIGHT}{Fore.LIGHTYELLOW_EX} Installing Modules",
        f"{Fore.MAGENTA}02:35 {Fore.YELLOW} Start coding",
        f"{Fore.MAGENTA}05:11 {Fore.YELLOW} Font Custom",
        f"{Fore.MAGENTA}08:45 {Fore.YELLOW} Warna + Gacha Font",
        f"{Fore.MAGENTA}10:25 {Fore.YELLOW} Warna + Font Custom (Fixed & Gacha)",
        f"{Fore.MAGENTA}12:50 {Fore.BLUE} Write to .txt",
        f"{Fore.MAGENTA}17:55 {Fore.BLUE} Write to .txt (1 file for each font)",
        f"{Fore.MAGENTA}23:41 {Fore.GREEN} Decorating the code",
        f"{Fore.MAGENTA}28:04 {Fore.LIGHTMAGENTA_EX} Gradient-figlet",
        f"{Fore.MAGENTA}31:48 {Fore.CYAN} Outro"
    ]
    print("\n")
    for i in range(0, len(arr)-1):
        print(arr[i])
    
main()