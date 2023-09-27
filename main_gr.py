from gradient_figlet import print_with_gradient_figlet as figr
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
    
    index = rd.randint(0, len(fonts)-1)
    font = fonts[index][:-4]
    # with open("gradient.txt", "w") as gr:
    #     content = figr("Hello, world!", font=f"{font}",color1="Blue", color2="Red")
    #     gr.write(str(content))

    font = "chiseled"
    print(f"Font = {font}.flf\n")
    figr("Hello, world!", font=f"{font}",color1="Blue", color2="Red")
    
main()