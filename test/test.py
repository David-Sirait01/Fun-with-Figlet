import os, random as rd, time as t, io
from colorama import Fore, Style, init

init(autoreset=True)

# print("Back colours:",sa.Text.back_arr)
# print("\nFore colours:",sa.Text.fore_arr)
from termcolor import colored

def gradient_text(text, gradient_colors):
    gradient_length = len(gradient_colors)
    text_length = len(text)
    step = text_length / gradient_length
    gradient_text = ""

    for i, char in enumerate(text):
        gradient_index = min(int(i // step), gradient_length - 1)
        gradient_color = gradient_colors[gradient_index]
        gradient_text += colored(char, gradient_color)

    return gradient_text

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
    content = top_border + f"[{text}]" + bottom_border + ""
    if p == True:
        print(content, end="")
        return content
    else:
        return content
    
def classic(font):
    from pyfiglet import figlet_format as fig
    print(f"{fig('Hello, world!', font=f'{font}')}")

def rainbow(font):
    from gradient_figlet import print_with_gradient_figlet as figR
    figR("Hello, world!", font=f"{font}", color1="Blue", color2="Yellow")

def get_folder_files(path, only=None):
    file_names = []
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                if only is None or item.endswith(f".{only}"):
                    file_names.append(item)
    return file_names

def execution(start, end):
    elapsed = (end - start) * 1000
    if 0.0 < elapsed < 50.0:
        x_tx = f"{Fore.CYAN}{elapsed:.2F}"
    elif 50.0 < elapsed < 100.0:
        x_tx = f"{Fore.YELLOW}{elapsed:.2F}"
    else:
        x_tx = f"{Fore.RED}{elapsed:.2F}"
        

    # print(f"\n> {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Time elapsed: {x_tx} {Style.RESET_ALL}ms")
    return x_tx


def main():
    start = t.time()
    
    def get_figletFont():
        username = os.getlogin()
        dir_path = r'C:\Users\{}\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyfiglet\fonts'.format(username)

        return get_folder_files(dir_path, only="flf")
    
    fonts = get_figletFont()
    
    index = rd.randint(0, len(fonts)-1)
    font = fonts[index][:-4]
    
    txt = f" Testing \"{Fore.BLUE}{font}{Style.RESET_ALL}.flf\" "
    # print(f"{txt}")
    printmid(f"{txt}");print("\n")
    
    # printmid(" PyFiglet "); print("\n")
    print("PyFiglet")
    start = t.time()
    classic(font)
    end = t.time()
    print(f"> {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Time elapsed: {execution(start, end)} {Style.RESET_ALL}ms")

    print("\n")

    gradient_colors = ['blue', 'cyan', 'green', 'yellow', 'red']
    tx = gradient_text('Gradient PyFiglet', gradient_colors)
    
    # print("============================", end="")
    # printmid(f" {tx} ")
    # print("============================\n")
    # printmid(f" Gradient PyFiglet ")
    # print(f"Gradient PyFiglet ")
    print(tx)
    start = t.time()
    rainbow(font)
    end = t.time()
    print(f"\n> {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Time elapsed: {execution(start, end)} {Style.RESET_ALL}ms")

    end = t.time()
    var = execution(start, end)
    path = os.path.join("avg.txt")
    with io.open(f"{path}", "a") as fl:
        fl.write(f"    {var[5:]},\n")
    
def exe():
    start = t.time()
    main()
    end = t.time()
    var = execution(start, end)
    print(f"\nOverall: {var} ms")
    
    # path = os.path.abspath(sys.argv[0])[:-len(sys.argv[0])]
    # print(__file__[:-7])
    # path = os.path.join("avg.txt")
    # with io.open(f"{path}", "a") as fl:
    #     fl.write(f"    {var[5:]},\n")

# exe()
main()

# exit(code=var)