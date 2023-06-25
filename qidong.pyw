import ctypes
import os.path
import subprocess
from tkinter import Tk, BOTH, X, LEFT, RIGHT
from tkinter.ttk import Frame, Button, Label, Entry


DETACHED_PROCESS = 0x00000008


class QiDong(Frame):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.master.title("米忽悠，启动！")
        self.pack(fill=BOTH, expand=1)

        self.pack_game("原神", "C:\Program Files\Genshin Impact\Genshin Impact Game\YuanShen.exe")
        self.pack_game("星铁", "C:\Program Files\Star Rail\Game\StarRail.exe")
        self.pack_game("崩三", "C:\Program Files\Honkai Impact 3\Games\BH3.exe")


    def pack_game(self, name: str, path: str):
        frame = Frame(self)
        frame.pack(fill=X)

        label = Label(frame, text=name)
        label.pack(side=LEFT, padx=5, pady=5)

        entry = Entry(frame, state="normal", width=50)
        entry.insert(0, path)
        entry.pack(side=LEFT, fill=X, padx=5, pady=5, expand=True)

        command= lambda: subprocess.Popen(entry.get().split(), close_fds=True, creationflags=DETACHED_PROCESS, shell=True)
        button = Button(frame, text="启动！", command=command)
        button.pack(side=RIGHT, padx=5, pady=5)

        if not os.path.exists(entry.get()):
            button.state = "disabled"


def main():
    root = Tk()
    QiDong()
    root.mainloop()


if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    main()