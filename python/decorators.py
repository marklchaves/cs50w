print("\nDecorators\n")

def announce(f):
    def wrapper():
        print("\nAbout to run the function ...")
        f()
        print("Done with the function.\n")
    return wrapper

@announce
def hello():
    print("\n\tHello, world!\n")

hello()