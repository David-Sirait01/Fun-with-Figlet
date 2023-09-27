from pyfiglet import figlet_format as fig
from colorama import Fore, Back, Style, init
import os, random as rd, sty_arr as sa, io

def get_folder_files(path, only=None):
    file_names = []
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                if only is None or item.endswith(f".{only}"):
                    file_names.append(item)
    return file_names

def writeto(file, content, clr=False):
    with io.open(file, "a") as fl:
        if clr:
            fl.truncate(0)
            fl.write(content)
        else:
            fl.write(content)

def main():
    # Ganti dengan input()
    tx = "Hello, world!"
    file = "figlet.txt"
    writeto(file, tx)
    
    def get_figletFont():
        username = os.getlogin()
        dir_path = r'C:\Users\{}\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyfiglet\fonts'.format(username)

        return get_folder_files(dir_path, only="flf")
    
    fonts = get_figletFont()
    sz = len(fonts)
    
    # Cara biasa
    print(f"{tx}")
    
    rand = rd.randint(0, sz-1)
    font = fonts[rand][:-4]
    
    # Pakai Figlet
    # Pewarnaan harus pakai huruf besar
    rand2 = rd.randint(0, 14)
    warna = sa.Colour.fore_arr[rand2]
    warna_t = sa.Text.fore_arr[rand2]
    
    content = f"\n\nFont = {font}\nwarna = {warna}{warna_t}{sa.Style.RESET_ALL}\n\n{warna}{fig(tx, font=font)}"
    print(f"{content}")


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
        fg = fig(f"{tx}", font=f)
        content = f"{i+1}. Font = {fonts[i]}\n\n{fg} \n\n"
        writeto(file, content)

        folder = os.path.join("__fonts__\\" + fonts[i] + ".txt")
        with open(folder, 'w', encoding='utf8') as fl:
            fl.write(content)
    # content = f"Font = {font}\n\n{fig(tx, font=font)}"
    # writeto(file, content, clr=True)
    
    # os.system(f"notepad {file}")
    
if __name__ == "__main__":
    main()