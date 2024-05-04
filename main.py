from tkinter import *


#In object-oriented programming, a class is a blueprint for creating objects. When you call a class constructor like Tk(), it creates a new instance (or object) of that class.
def miles_to_kilometer():
     miles =float(miles_input.get())
     km = miles * 1.609
     kilometer_result_lable.config(text =f"{km}")


window =Tk()
window.title("miles to kilometer converter")
window.config(padx=20 , pady=20)

#In Tkinter, an Entry widget is a field where the user can enter text or data. It's commonly used for input fields where the user needs to type something, such as their name, age, or in this case, miles.
miles_input =Entry(width=7)
miles_input.grid(column=1,row=0)


miles_lable =Label(text ="Miles")
miles_lable.grid(column=2,row=0)


is_equal_to =Label(text ="is equal to")
is_equal_to.grid(column=0,row=1)



kilometer_result_lable =Label(text ="0")
kilometer_result_lable.grid(column=1,row=1)

kilometer_lable =Label(text ="KM")
kilometer_lable.grid(column=2,row=1)



calculate_button =Button(text ="calculate" , command=miles_to_kilometer)
calculate_button.grid(column=1,row=2)


#use the grid to layout all of these component to correct position



#When you call window.mainloop(), it's like starting the heartbeat of your GUI. It begins listening for any actions the user might take, like clicking buttons or typing.
window.mainloop()