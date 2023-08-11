from tkinter import *

def convert():
    output_string.set(entry_int.get())


window = Tk()
window.title("Map app")
window.minsize(900, 600)  # width, height
window.geometry("300x300")

# Create Label in our window
text = Label(master = window, text="Title", font='Roboto 24')
text.pack()

#input field

input_frame = Frame(master = window)
entry_int = IntVar()
entry = Entry(master = input_frame, textvariable=entry_int)
button = Button(master= input_frame, text = 'Submit', command=convert)

entry.pack(side = 'left', padx = 10)
button.pack(side = 'left', padx = 10)
input_frame.pack(pady = 10)



# output
output_string = StringVar()
output_label=Label(
    master = window,
    text = 'output',
    textvariable=output_string)
output_label.pack()


window.mainloop()