from termcolor import colored

def gradient_text(text, colors):
    gradient_length = len(colors)
    text_length = len(text)
    step = text_length / gradient_length
    gradient_text = ""
    for i, char in enumerate(text):
        gradient_index = min(int(i // step), gradient_length - 1)
        gradient_color = colors[gradient_index]
        gradient_text += colored(char, gradient_color)
    return gradient_text

# Daftar warna gradien yang ingin Anda gunakan
colors = ['blue', 'cyan', 'green', 'yellow', 'red']

# Teks yang ingin Anda buat dengan gradien
text = "Hello, world in gradient!"
text = "Gradient Figlet"

# Buat teks dengan gradien
gr = gradient_text(text, colors)

# Cetak teks dengan gradien
print(gradient_text(text, colors))
