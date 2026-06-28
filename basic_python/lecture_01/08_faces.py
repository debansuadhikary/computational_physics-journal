# defing the main part of the code 
def main():
    txt = input("How do you feel? ")
    convert(txt)

# defining the function 'convert'
def convert(str):
    str = str.replace(":)","🙂").replace(":(","🙁")
    print(str)

# calling the main function
main()
