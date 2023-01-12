# A Huffman Tree Node
import heapq
from prettytable import PrettyTable
import math
import docx2txt


class symbol_class:
    def __init__(self, symbol_char, char_freq, codeword, len_codeword):
        self.char_freq = char_freq
        self.symbol_char = symbol_char
        self.codeword = codeword
        self.len_codeword = len_codeword
class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (character)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

char_freq = {}
table = PrettyTable()
symbols = []
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)

    if (not node.left and not node.right):
        symbols.append(symbol_class(node.symbol, char_freq[node.symbol], newVal, len(newVal)))
        # print(f"{node.symbol} -> {newVal}")
def read_file():
    char_sum = 0
    # text = docx2txt.process("The+Boarding+House.docx")
    text = docx2txt.process("Shooting+an+elephant+by+George+Orwell+recovered.docx")
    # text = docx2txt.process("test.docx")

    for char in text:
        char_sum += 1
        char = char.lower()
        if char == " ":
            char = "space"
        if char == '\n':
            continue
        if not char_freq.__contains__(char):
            char_freq.__setitem__(char, 1)
        else:
            char_freq.__setitem__(char, char_freq.__getitem__(char) + 1)
    return char_sum

if __name__ == '__main__':
    char_sum = read_file()
    table.field_names = ["Symbol", "Symbol frequency", "Probability", "codeword", "Length of code  word in bits"]
    nodes = []
    for key, value in char_freq.items():
        heapq.heappush(nodes, node(value, key))
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        left.huff = 0
        right.huff = 1
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        heapq.heappush(nodes, newNode)

    # Huffman Tree is ready!
    printNodes(nodes[0])
    symbols.sort(key=lambda x: x.char_freq, reverse=True)
    avg_len = 0
    entropy = 0
    total_num_of_bits_from_huffman = 0
    total_num_of_bits_from_ASCII = char_sum*8
    for s in symbols:
        total_num_of_bits_from_huffman += s.char_freq*s.len_codeword
        table.add_row([s.symbol_char, s.char_freq, (s.char_freq / char_sum), s.codeword, s.len_codeword])
        avg_len += (s.char_freq / char_sum)*s.len_codeword
        entropy += abs((s.char_freq / char_sum)*math.log((s.char_freq / char_sum), 2))
    percentage_of_compression = (total_num_of_bits_from_huffman / total_num_of_bits_from_ASCII) * 100
    print(table)
    print("The average number of bits/character for the whole story == ", avg_len, "bit/character")
    print("The entropy of the alphabet == ", entropy, "bit/character")
    print("If ASCII code is used the number of bits needed to encode the story == ", total_num_of_bits_from_ASCII)
    print("If huffman code is used the number of bits needed to encode the story == ", total_num_of_bits_from_huffman)
    print("the percentage of compression accomplished by using the Huffman encoding as compared to ASCII code == ", percentage_of_compression, "%")

