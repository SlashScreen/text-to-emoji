import pyperclip
import textwrap

def regionalCodeIt(string):
    topro = textwrap.wrap(string.lower(),25)
    print (topro)
    canbe = "abcdefghijklmnopqrstuvwxyz"
    nums = "1234567890"
    num2words = {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    out = ""
    for line in topro:
        for c in line:
            if c in canbe:
                out = out + ":regional_indicator_{c}: ".format(c = c)
            if c in nums:
                out = out + ':'+ num2words[int(c)].lower() + ': '
            if c == " ":
                out = out + " "*5
            if c == "!":
                out = out + ":exclamation: "
            if c == "?":
               out = out + ":question: "
        out = out + "\n"
    return out

if __name__ == "__main__":
    pyperclip.copy(regionalCodeIt(input("What would you like to turn to indicators? ")))
    print("Output was automatically copied to clipboard.")
