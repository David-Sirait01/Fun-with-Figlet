from pyfiglet import figlet_format as fig
import os, random as rd

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
    print(f"\n\nFont = {font}\n\n{fig(tx, font=font)}")
    
if __name__ == "__main__":
    main()