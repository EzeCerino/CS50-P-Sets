# TODO
from cs50 import get_string

def main():
    phrase = get_string("Phrase: ")
    s=0
    l=0
    w=1
    for char in phrase:
        if char == '!' or char =='?' or char =='.':
            s += 1
        elif char == " ":
            w += 1
        else:
            l += 1

    print(f"Number of letters: {l}")
    print(f"Number of sentences: {s}")
    print(f"Number of words: {w}")

    ll = l/w * 100
    ss = s/w * 100

    index = 0.0588 * ll - 0.296 * ss - 15.8
    index = round(index)
    if index < 1 :
        print("Before Grade 1")
    elif index > 15 :
        print("Grade 16+")
    else:
        print(f"Grade {index}")

main()