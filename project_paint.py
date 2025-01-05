#GUI- graphic user interface apps are apps with good graphics and user interface
# library for GUI apps- tkinter, kivy


from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog

#tkinter is a python library for creating GUI apps
#PIL- python imaging library
#PIL= pillow

from PIL import Image, ImageDraw, ImageGrab,ImageTk
from tkinter import messagebox

#tkinter.messagebox is used to show messages to the user
#tkinter.messagebox.showinfo("title","message")

root= Tk()
root.title("Vasu's paint program")

brush_color= "black"

def paint(e):
    #my_canvas.config(bg= "black")

    #brush parameters
    brush_width= '%0.0f' % float(my_slider.get())
    brush_type2= brush_type.get()

    #starting position
    x1= e.x -1
    y1= e.y -1

    #ending position
    x2= e.x +1
    y2= e.y +1

    #draw on canvas
    my_canvas.create_line(x1,y1,x2,y2,fill= brush_color, width= brush_width, capstyle=brush_type2, smooth=True)

#change the size of brush
def change_brush_size(thing):
    slider_label.config(text='0.0f' % float(my_slider.get()))

# change brush color
def change_brush_color():
    global brush_color
    brush_color= "black"
    brush_color= colorchooser.askcolor(color= brush_color)[1]

#change canvas color
def change_canvas_color():
    global bg_color
    bg_color="black"
    bg_color= colorchooser.askcolor(color= bg_color)[1]
    my_canvas.config(bg=bg_color)

#clear screen
def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg="white")

def save_as():
    result= filedialog.asksaveasfilename(initialdir='',filetypes=(("png files", "*.png"),("all files","*.*")))

    if result.endswith('.png'):
        pass
    else:
        result= result + '.png'
    if result:
        x= root.winfo_rootx()+ my_canvas.winfo_x()
        y= root.winfo_rooty()+ my_canvas.winfo_y()
        x1= x + my_canvas.winfo_width()
        y1= y + my_canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)

        #Pop up success message
        messagebox.showinfo(title="image saved", message="image saved successfully")

    result_label= Label(root, text=result)
    result_label.pack(pady=20)





#create our canvas
w=600
h=400

#bind the canvas for mouse drag
my_canvas= Canvas(root, width=w, height=h,bg= "white" )
my_canvas.pack(pady= 20)
my_canvas.bind('<B1-Motion>',paint )

#Brush options frame
brush_options_frame= Frame(root)
brush_options_frame.pack(pady = 20)

# Brush size
brush_size_frame= LabelFrame(brush_options_frame, text="Brush size")
brush_size_frame.grid(row=0, column=0, padx=50)

## Brush slider
my_slider= ttk.Scale(brush_size_frame,from_ =1, to=50, command= change_brush_size) 
my_slider.pack(pady=10, padx=10)

#Brush slider label
slider_label= Label(brush_size_frame, text= my_slider.get())
slider_label.pack(pady=5)

#Brush type
brush_type_frame= LabelFrame(brush_options_frame, text="Brush type", height=400)
brush_type_frame.grid(row=0, column=1, padx=50 )

brush_type= StringVar()
brush_type.set("round")

#Create Radio Buttons for brush types

brush_type_radio1= Radiobutton(brush_type_frame, text="Round", variable=brush_type, value="round")
brush_type_radio2= Radiobutton(brush_type_frame, text="Slash", variable= brush_type, value="butt")
brush_type_radio3= Radiobutton(brush_type_frame,text= "Diamond", variable=brush_type, value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)


#change color
change_colors_frame= LabelFrame(brush_options_frame, text="change colors")
change_colors_frame.grid(row=0, column=2)

##change brush color button
brush_color_button= Button(change_colors_frame, text= "Brush Color", command = change_brush_color )
brush_color_button.pack(pady=10, padx=10)

##change canvas background color
canvas_color_button= Button(change_colors_frame, text= "Canvas Color", command= change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)

#Program option frame
options_frame= LabelFrame(brush_options_frame, text= "Program Options")
options_frame.grid(row=0, column=3, padx= 50)

# Clear screen button
clear_button= Button(options_frame, text= "Clear Screen", command=clear_screen)
clear_button.pack(padx=10, pady=10)

#save image
save_image_button= Button(options_frame, text= "Save to PNG", command=save_as)
save_image_button.pack(pady=10, padx=10)







root.mainloop()