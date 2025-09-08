# Imports

class Wonderhoy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    __str__ = lambda self : f"{self.name}, {self.color}\n"

def main():
    the_stupids = [
        Wonderhoy("Tenma Tsukasa", "Yellow"),
        Wonderhoy("Otori Emu", "Pink"),
        Wonderhoy("Kusanagi Nene", "Green"),
        Wonderhoy("Kamishiro Rui", "Purple"),
        Wonderhoy("Hatsune Miku", "Cyan")
    ]

    for i in range(len(the_stupids)):
        if i in [2, 3]:
            print(f"{the_stupids[i]}W-Wonderhoy...\n")
        else:
            print(f"{the_stupids[i]}WONDERHOY!!!\n")

if __name__ == "__main__":
    main()
