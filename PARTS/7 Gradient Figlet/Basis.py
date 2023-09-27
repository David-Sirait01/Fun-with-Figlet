from gradient_figlet import print_with_gradient_figlet as g_fig
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
    def get_figletFont():
        username = os.getlogin()
        dir_path = r'C:\Users\{}\AppData\Local\Programs\Python\Python311\Lib\site-packages\pyfiglet\fonts'.format(username)

        return get_folder_files(dir_path, only="flf")
    
    fonts = get_figletFont()
    sz = len(fonts)
    
    tx = "Hello, world!"
    
    rand = rd.randint(0, sz-1)
    font = fonts[rand][:-4]
    print(f"\nFont = {font}")
    g_fig(tx, font=f"{font}", color1="yellow", color2="blue")
    
main()