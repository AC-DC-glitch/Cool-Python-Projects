phrase = input("Input the encoded phrase to get the decoded phrase:")

decode = {
    "0": "9",
    "1": "8",
    "2": "7",
    "3": "6",
    "4": "5",
    "5": "4",
    "6": "3",
    "7": "2",
    "8": "1",
    "9": "0",
    "A": "Z",
    "a": "z",
    "B": "Y",
    "b": "y",
    "C": "X",
    "c": "x",
    "D": "W",
    "d": "w",
    "E": "V",
    "e": "v",
    "F": "U",
    "f": "u",
    "G": "T",
    "g": "t",
    "H": "S",
    "h": "s",
    "I": "R",
    "i": "r",
    "J": "Q",
    "j": "q",
    "K": "P",
    "k": "p",
    "L": "O",
    "l": "o",
    "M": "N",
    "m": "n",
    "N": "M",
    "n": "m",
    "O": "L",
    "o": "l",
    "P": "K",
    "p": "k",
    "Q": "J",
    "q": "j",
    "R": "I",
    "r": "i",
    "S": "H",
    "s": "h",
    "T": "G",
    "t": "g",
    "U": "F",
    "u": "f",
    "V": "E",
    "v": "e",
    "W": "D",
    "w": "d",
    "X": "C",
    "x": "c",
    "Y": "B",
    "y": "b",
    "Z": "A",
    "z": "a",
    " ": " ",
    "`": "`",
    "~": "~",
    "!": "!",
    "@": "@",
    "#": "#",
    "$": "$",
    "%": "%",
    "^": "^",
    "&": "&",
    "*": "*",
    "(": "(",
    ")": ")",
    "-": "-",
    "_": "_",
    "+": "+",
    "=": "=",
    "[": "[",
    "]": "]",
    "{": "{",
    "}": "}",
    "\\": "\\",
    "|": "|",
    ";": ";",
    ":": ":",
    "'": "'",
    "\"": "\"",
    ",": ",",
    "<": "<",
    ".": ".",
    ">": ">",
    "/": "/",
    "?": "?"
}

blank_string = ""
for letter in phrase:
    secret_key = decode.get(letter)
    blank_string = blank_string + secret_key
print(blank_string)
