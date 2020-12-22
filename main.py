from tkinter import Tk, NORMAL, END, DISABLED, LabelFrame, Canvas, Label, Entry, StringVar, OptionMenu, Frame, Button, RIDGE, NW
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
import webbrowser
import os
import getpass
import img_process

root = Tk()
root.title('Image Resize')
root.resizable(False, False)

file_name = None
render_in = None
load_in = None
render_out = None
user = None
directory = None

def make_dir():
    global user
    user = getpass.getuser()
    global directory
    directory=f'/home/{user}/Pictures/image_resize'
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        pass 
make_dir()




def open_file():
    
    global file_name
    file_name = filedialog.askopenfilename(initialdir=f'/home/{user}', title = 'Select image', filetypes=(('Images' , '*.jpeg *.jpg *.JPG *.JPEG *.png *.bmp'),('All files','*.*')))
    if file_name is not None:
        try:
            print (file_name)
            load_in = Image.open(file_name)
        except:
            messagebox.showerror('Error', 'Please select image')
        
    
        

    img_in = load_in.resize((250,250))
    global render_in
    render_in = ImageTk.PhotoImage(img_in)
    img_in_cnvs.itemconfigure(img_in_area, image=render_in)
    img_in_cnvs.update()
    status.configure(text='Image imported')
    size_in_txt.configure(text = f'{load_in.size[0]} x {load_in.size[1]}')
    format_in_txt.configure(text = load_in.format)
    size_w_txt.configure(state=NORMAL)
    size_h_txt.configure(state=NORMAL)
    click.set('JPG')
    format_out_txt.configure(state=NORMAL)
    convert_btn.configure(state=NORMAL)
    reset_btn.configure(state=NORMAL)


def convertor():
    try:
        height=int(size_w_txt.get())
        width=int(size_h_txt.get())
    except ValueError:
        messagebox.showerror('Error', 'Specify Height and Width as number')

    frmt=click.get()
    img_process.image_processing(file_name, height, width, frmt, directory)
    global render_out
    render_out = ImageTk.PhotoImage(img_process.new_img)
    img_out_cnvs.itemconfigure(img_out_area, image=render_out)
    open_folder_btn.configure(state=NORMAL)
    status.configure(text=f'Saved to {directory}')

def open_folder():
    webbrowser.open(directory)

def reset():
    status.configure(text='Reset')
    img_in_cnvs.delete('all')
    img_out_cnvs.delete('all')
    size_in_txt.configure(text='')
    format_in_txt.configure(text='')
    size_h_txt.delete(0, END)
    size_w_txt.delete(0, END)
    format_out_txt.configure(state=DISABLED)
    convert_btn.configure(state=DISABLED)
    open_folder_btn.configure(state=DISABLED)
    reset_btn.configure(state=DISABLED)

in_img_frame = LabelFrame(root, text = 'Input', labelanchor = 'n')
in_img_frame.grid(row= 4, column=0, padx=30)


img_in_cnvs = Canvas(in_img_frame, height =250,width=250)
img_in_area = img_in_cnvs.create_image(0,0, anchor=NW, image=None)
img_in_cnvs.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

size_in_label = Label(in_img_frame, text='Size')
size_in_label.grid(row=1, column=0, sticky='W', padx=40)

format_in_label = Label(in_img_frame, text='Format')
format_in_label.grid(row=2, column=0, sticky='W', padx=40)

size_in_txt = Label(in_img_frame)
size_in_txt.grid(row=1, column=1, sticky='W', pady=10)

format_in_txt = Label(in_img_frame)
format_in_txt.grid(row=2, column=1, sticky='W', pady=5)





out_img_frame = LabelFrame(root, text = 'Output', labelanchor = 'n')
out_img_frame.grid(row= 4, column=1, padx=30)

img_out_cnvs = Canvas(out_img_frame, height=250, width=250)
img_out_area = img_out_cnvs.create_image(0,0, anchor=NW, image=None)
img_out_cnvs.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

size_out_label = Label(out_img_frame, text='Specify size')
size_out_label.grid(row=1, column=0, sticky='W', padx=20)

format_out_label = Label(out_img_frame, text='Specify format')
format_out_label.grid(row=2, column=0, sticky='W', padx=20, pady=5)

size_h_txt = Entry(out_img_frame, state=DISABLED, width=5)
size_h_txt.grid(row=1, column=1, sticky='W', pady=10)

size_w_txt = Entry(out_img_frame, state=DISABLED, width=5)
size_w_txt.grid(row=1, column=1, sticky='E', pady=10)

click = StringVar()
format_out_txt = OptionMenu(out_img_frame, click, 'JPG','PNG','BMP')
format_out_txt.configure(width=6, state=DISABLED)
format_out_txt.grid(row=2, column=1, sticky='W')


btn_in_frame = Frame(root)
btn_in_frame.grid(row=5, column=0, pady=20)

open_btn = Button(btn_in_frame, text='Open', command=open_file)
open_btn.grid(row=0, column=0)

reset_btn = Button(btn_in_frame, text='Reset', state=DISABLED, command=reset)
reset_btn.grid(row=0, column=1)


btn_out_frame = Frame(root)
btn_out_frame.grid(row=5, column=1, pady=20)

convert_btn = Button(btn_out_frame, text='Convert', state=DISABLED, command=convertor)
convert_btn.grid(row=0, column=0)

open_folder_btn = Button(btn_out_frame, text='Open folder', state=DISABLED, command=open_folder)
open_folder_btn.grid(row=0, column=2)

status = Label(root, relief=RIDGE, width=50)
status.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()
