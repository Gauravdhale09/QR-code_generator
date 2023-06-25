from tkinter import *
from customtkinter import *
import qrcode
from PIL import Image
from tkinter import messagebox as msg
import os
class Generate(Tk):
    def __init__(self):
        super(Generate, self).__init__()
        self.geometry('1200x750+180+30')
        self.config(background="#32a852")
        self.maxsize("1200", '750')
        self.minsize("1200", '750')
        self.title("QR_generator")
        self.wm_iconbitmap("")
        global e1
        e1 = StringVar()
        global e2
        e2 = StringVar()
        global e3
        e3 = StringVar()
        global frame1
        frame1 = CTkFrame(master=self, height=650, width=570, bg_color='#d4c8c7').place(x=15, y=70)
        global frame2
        frame2 = CTkFrame(master=self, height=650, width=560).place(x=620, y=70)

    def labels(self):
        CTkLabel(master=self, text="Welcome to QR-Generating platform!",text_color='white',font=("roboto", 25, 'bold')).place(x=400, y=10)
        CTkLabel(master=frame1, text="Paste the link of any website below and click to ok",text_color='black',bg_color='#d4c8c7',font=("roboto", 20)).place(x=60, y=100)
        CTkLabel(master=frame1, text="Give name to the genrated QR",text_color='black',bg_color='#d4c8c7',font=("roboto", 20)).place(x=60, y=200)
        CTkLabel(master=frame1, text="(e.g. ABC)",text_color='black',bg_color='#d4c8c7',font=("roboto", 20)).place(x=420, y=250)
        CTkLabel(master=frame2, text="Here is the QR",text_color='black',bg_color='#d4c8c7',font=("roboto", 35,'bold')).place(x=770, y=100)
        CTkLabel(master=frame1, text=f"Your png is saved at:", text_color='black', bg_color='#d4c8c7',font=("roboto", 20)).place(x=60, y=400)
        CTkLabel(master=frame1, text="~By GRD@developers", text_color='black', bg_color='#d4c8c7',font=("Sans serif", 20,'bold')).place(x=370, y=690)

    def entry(self):

        CTkEntry(master=frame1, text_color='black', textvariable=e1,bg_color='#d4c8c7', width=455, font=("roboto", 20)).place(x=60, y=150)
        CTkEntry(master=frame1, text_color='black', textvariable=e2,bg_color='#d4c8c7', width=355, font=("roboto", 20)).place(x=60, y=250)
        CTkEntry(master=frame1, textvariable=e3, text_color='black', bg_color='#d4c8c7', width=535, font=("roboto", 20)).place(x=30, y=450)

    def buttons(self):
        def reset():
            e1.set("")
            e2.set("")
            e3.set("")
        def ok():
            if ('https' or 'www') in e1.get():
                y = qrcode.make(e1.get())
                if not os.path.exists('C:/QR_create'):
                    os.makedirs('C:/QR_create')
                else:
                    file_location = 'C:/QR_create/' + e2.get() + '.png'
                    y.save(file_location)
                    e3.set(f"{file_location}")
                file_location = 'C:/QR_create/' + e2.get() + '.png'
                y.save(file_location)
                e3.set(f"{file_location}")
                my_image = CTkImage(light_image=Image.open(f"{file_location}"),
                                                  dark_image=Image.open(f"{file_location}"),
                                                  size=(400, 400))
                CTkLabel(master=frame2, image=my_image).place(x=700, y=200)

            else:
                if e2.get() == "":
                    msg.showinfo("png name", "Enter png name first")
                else:
                    msg.showinfo("only site", "only site link is applicable")
        CTkButton(master=frame1, text_color='black', text="SAVE",bg_color='#d4c8c7', width=50, font=("roboto", 20), command=ok).place(x = 60, y=325)
        CTkButton(master=frame1, text_color='black', text="RESET",bg_color='#d4c8c7', width=50, font=("roboto", 20), command=reset).place(x = 160, y=325)



if __name__ == '__main__':
    g = Generate()
    g.labels()
    g.entry()
    g.buttons()
    g.mainloop()
