from tkinter import Tk, ttk, constants
from tkinter.font import BOLD, Font
from ui.ui import UI


def main():
    window = Tk()
    window.eval('tk::PlaceWindow . center')
    window.title("Ajanvaraussovellus")
    ui = UI(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()