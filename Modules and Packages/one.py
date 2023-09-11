# python one.py
# All code at identation 0 gets called when you run the scrip file. This isn't like JS where there is some sort of main() function
def func():
    print('FUNC() IN ONE.PY')


print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    print("ONE.PY is being run directly!")
else:
    print("ONE.PY has been imported!")
