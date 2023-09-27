# Impor module

from pyfiglet import figlet_format as fig
from colorama import Fore, Back, Style, init

import io, sys, os

def printmid(text, p=True):
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
    content = top_border + f"[{text}]" + bottom_border + "\n"
    if p == True:
        print(content)
        return content
    else:
        return content
    
def writeto(file, content, clr=False):
    with io.open(file, "a") as fl:
        if clr:
            fl.truncate(0)
            fl.write(content)
        else:
            fl.write(content)

def get_folder_files(path, only=None):
    file_names = []
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                if only is None or item.endswith(f".{only}"):
                    file_names.append(item)
    return file_names

def main():
    init(autoreset=True)

    printmid(f"{Fore.CYAN}Figlet {Style.BRIGHT}{Fore.GREEN}all fonts{Style.RESET_ALL}")

    def get_figletFont():
        username = os.getlogin()
        dir_path = r'C:\Users\{}\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyfiglet\fonts'.format(username)

        return get_folder_files(dir_path, only="flf")
    
    fonts = get_figletFont()
    sz = len(fonts)
    
    # print("Hello, world!")

    import sty_arr as sy
    
    # GACHA FONT
    # from random import randint as rd
    # rnd_font = fonts[rd(0, len(fonts)-1)][:-4]
    # warna = sty_arr.color.fore_arr[rd(0, 14)]
    
    # print(f"Jumlah font =  {len(fonts)}\n\ngacha = {rnd_font}")
    # content = Fore.GREEN + fig(f"Hello, world!", font=f"{rnd_font}")
    # writeto("figlet.txt", content)
    # print(content)
    
    # Buat file .txt
    file = "figlet.txt"
    
    # Kosongkan file
    sy.clr(file)

    # Input textnya
    # text = "Hello, world!"
    try:
        text = input("Enter massage : \n> ")
    
    # Menghindari error
    except EOFError or KeyboardInterrupt:
        print(f"\n {Back.LIGHTBLACK_EX}{Fore.YELLOW}Woops! Wrong key buddy!")
        os.system("pause")
        exit()
    
    prev = f"{Style.RESET_ALL}{Style.BRIGHT}" + fig(f" {text } ")
    print(f"\n\nPreview with {Fore.BLUE}standard.flf\n{prev}\n\n")
    
    if not os.path.exists("__fonts__"):
        os.makedirs("__fonts__")

    for i in range(0, sz):
        # Hitung persentase
        percentage = (i + 1) / sz * 100

        # Cetak progress bar
        bar_length = 40
        fl_sz = 0

        progress = int(bar_length * (i + 1) / sz)
        progress_bar = r"=" * progress + " " * (bar_length - progress)
        fl_sz = fl_sz + os.path.getsize(file)
        
        # Yellow back + Bright White fore
        # print(Back.YELLOW + Style.BRIGHT + Fore.WHITE + f"[{progress_bar}] {percentage:.2f}% | Size: {(fl_sz/1024)*2:.2F} KB ", end='\r')
        
        # Yellow bar only
        print(Style.BRIGHT + Fore.YELLOW + f"[{progress_bar}] {percentage:.2f}% {Style.RESET_ALL}| Size: {(fl_sz/1024)*2:.2F} KB ", end='\r')

        f = fonts[i][:-4]
        fg = fig(f"{text}", font=f)
        content = f"{i+1}. Font = {fonts[i]}\n\n{fg} \n\n"
        writeto(file, content)

        folder = os.path.join("__fonts__\\" + fonts[i] + ".txt")
        with open(folder, 'w', encoding='utf8') as fl:
            fl.write(content)

    print("\r")
    print("Finished!")

if __name__ == "__main__":
    main()
    # os.system("pause")