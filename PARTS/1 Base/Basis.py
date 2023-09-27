from pyfiglet import figlet_format as fig

def main():
    tx = "Hello, world!"
    
    # Cara biasa
    print(f"{tx}")
    
    # Pakai Figlet
    print(f"{fig(tx)}")
    
if __name__ == "__main__":
    main()