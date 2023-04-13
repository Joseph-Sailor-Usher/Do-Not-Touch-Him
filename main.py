'''
    Shows a menu which says "Do Not Touch Him" and a button which says "Touch Him"
    When the application is opened, we log the time and date, when the button is pressed, we log the time and date again
    We also log the difference between the two times in a file called "log.txt" in the same directory as the application
    We change the "Do Not Touch Him" text to "You touched him" when the button is pressed, 
        and we display how long it took them to touch him in the menu
'''
import time
import datetime
import os
import sys
from tkinter import Tk, Label, Button, messagebox
from PIL import Image, ImageTk
#print(sys.executable)

# Log the time and date
original_time_and_date = datetime.datetime.now()

def main():
    # Create the window
    window = Tk()
    window.title("Do Not Touch Him")
    window.geometry("300x200")

    # Load the background image
    bg_image = Image.open("baby-monkey.jpg")  # Replace with your image path
    bg_image = bg_image.resize((300, 200), Image.ANTIALIAS)  # Resize the image to fit the window
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a label to display the background image
    bg_label = Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create the label
    label = Label(window, text="Do Not Touch Him", font=("Arial Bold", 32))
    label.pack(pady=20)

    # Create the button
    button = Button(window, text="Touch Him", command=lambda: button_clicked(label, button))
    button.pack()

    # Show the window
    window.mainloop()

def button_clicked(label, button):
    global original_time_and_date  # Add this line to indicate that you want to modify the global variable

    # Get the time and date
    time_and_date = datetime.datetime.now()

    # Calculate the time difference in seconds
    time_difference = time_and_date - original_time_and_date
    time_difference_seconds = round(time_difference.total_seconds(), 2)  # Adjust the number 2 to set the desired decimal places

    # Update the original_time_and_date variable
    original_time_and_date = time_and_date

    # Log the time and date in a file
    with open("log.txt", "a") as file:
        file.write(f"{time_difference_seconds} seconds until you touched him.\n")
    
    # Change the label text
    label.configure(text="You touched him")

    # Change the button text
    button.configure(text="Touch him again")

    # Display how long it took them to touch him
    messagebox.showinfo("You touched him", f"It took you {time_difference_seconds} seconds to touch him.")

    #update the original time and date
    original_time_and_date = datetime.datetime.now()

if __name__ == "__main__":
    main()
