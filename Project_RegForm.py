from tkinter import *

root= Tk()
root.geometry("500x300")


def getvals():
    print("Your form has been submited !!")


Label(root, text="Registration Form", font="times 15 bold").grid(row=0, column=3)


Name= Label(root, text= "Name")
Name.grid(row=1, column=2)

Phone= Label(root, text="Phone")
Phone.grid(row=2, column=2)

Gender= Label(root, text="Gender")
Gender.grid(row=3, column=2)

Country= Label(root, text="Country")
Country.grid(row=4, column=2)

Payment_mode=Label(root, text="payment_mode")
Payment_mode.grid(row=5, column=2)


Name_value= StringVar
Phone_value= StringVar
Country_value= StringVar
Gender_value= StringVar
Payment_mode_value= StringVar
checkvalue= IntVar


Name_entry= Entry(root, textvariable=Name_value)
Name_entry.grid(row=1, column=3)

Phone_entry= Entry(root, textvariable=Phone_value)
Phone_entry.grid(row=2, column=3)

Gender_entry= Entry(root, textvariable=Gender_value)
Gender_entry.grid(row=3, column=3)

Country_entry= Entry(root, textvariable=Country_value)
Country_entry.grid(row=4, column=3)

Payment_mode_entry= Entry(root, textvariable=Payment_mode_value)
Payment_mode_entry.grid(row=5, column=3)

Check_btn= Checkbutton( text="Remember me", variable=checkvalue)
Check_btn.grid(row=6, column=3)


Button(text="Submit", command=getvals).grid(rows=7, column=3)




root.mainloop()
