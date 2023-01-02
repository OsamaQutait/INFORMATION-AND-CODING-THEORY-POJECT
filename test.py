char_freq = {}

def read_file():
    file = open('store.txt', 'r')
    while 1:
        # read by character
        char = file.read(1)
        if not char:
            break
        if not char_freq.__contains__(char):
            char_freq.__setitem__(char, 1)
        else:
            char_freq.__setitem__(char, char_freq.__getitem__(char) + 1)
    file.close()


if __name__ == '__main__':
    read_file()
    # char_freq = sorted(char_freq)
    # print(char_freq)
    for key, value in char_freq.items():
        if key == '\n':
            print("-", "\\n", "-", " -> ", value)
        else:
            print("-", str(key), "-", " -> ", value)