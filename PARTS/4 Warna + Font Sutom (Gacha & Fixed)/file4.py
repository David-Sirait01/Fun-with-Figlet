from pyfiglet import figlet_format as fig
from colorama import Fore, Back, init
import os, random as rd, sty_arr as sa

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
    tx = "Hello, world!"
    
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
    print(f"\n\nFont = {font}\nwarna = {warna}{warna_t}{sa.Style.RESET_ALL}\n\n{warna}{fig(tx, font=font)}")
    
if __name__ == "__main__":
    main()