import tkinter

window = tkinter.Tk()
window.title("fun fun")
window.minsize(width=500, height=300)
my_label = tkinter.Label(text="Input", font=("Arial", 24, "bold"))
my_label.pack(expand=True)


window.mainloop()