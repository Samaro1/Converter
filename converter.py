from tkinter import *


screen= Tk()
screen.title("Amaro's Mile to Kilometer COnverter")

##
##upper frame 
upper = Frame(screen, bg="white")
upper.grid(row=2, column=0, columnspan=3, sticky="ew")  # Spans across 3 columns
upper.grid_columnconfigure((0,1,2), weight=1)
##MILES##
mile= Entry(upper, width= 29)
mile.insert(END, "Insert your unit in miles")
mile.grid(column=0, row=0, padx= 10, pady= 10)
##
Label(upper, text="Miles").grid(column=1, row=0, padx=5,pady=5)

##TEXT BESIDE KM##
text = Label(upper, text="Your miles in KM is:", bg="white", font=("Arial", 12),padx=4, pady=4)
text.grid(column=0, row=1)
text.grid_columnconfigure

# Create a Text widget
text_box = Text(upper, height=1, width=7, padx= 10,pady=10)
text_box.insert(END, 0)  # Add initial text
text_box.config(state=DISABLED)  # Disable editing
text_box.grid(column=1,row=1)

Label(upper, text="KM").grid(column=2, row=1)


# Function to update the text
def update_text():
    try:
        miles = float(mile.get())  # Get input and convert to float
        km = miles * 1.609344  # Convert miles to km
        text_box.config(state=NORMAL)  # Enable text box
        text_box.delete("1.0", END)  # Clear previous result
        text_box.insert(END, f"{km:.3f}")  # Insert new value
        text_box.config(state=DISABLED)  # Disable text box again
    except ValueError:
        text_box.config(state=NORMAL)
        text_box.delete("1.0", END)
        text_box.insert(END, "Invalid Input")
        text_box.config(state=DISABLED)

lower = Frame(screen, bg="white")
lower.grid(row=3, column=0, columnspan=3, sticky="ew",padx=10)  # Spans across 3 columns
lower.grid_columnconfigure((0,1,2), weight=1)
##CALCULATE BUTTON##
calc = Button(lower, text="Calculate", font="arial", command= update_text )
calc.grid(column=1,row=3, padx=10, pady=5)


screen.mainloop()