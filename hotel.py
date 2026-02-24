from tkinter import *

screen =Tk()
screen.title("Grand hotel Booking")
screen.geometry("500x480")
screen.config(bg="lightgrey")

Label( screen,text="Grand Hotel Reservation",font=("Bold", 24, "bold"),bg="lightgrey").pack(pady=20)
Label(screen, text="Guest Name:", font=("Arial", 12), bg="lightgrey").pack()
Entry(screen, width=30).pack(pady=5)

Label(screen, text="Nights to Stay:", font=("Arial", 12), bg="lightgrey").pack()
Spinbox(screen, from_=1, to=30, width=5).pack(pady=5)

Label(screen, text="Room Type:", font=("Arial", 12), bg="lightgrey").pack(pady=10)

room_var = StringVar()

Radiobutton(screen,text="Standard ($100)",variable=room_var,value="Standard",bg="lightgrey").pack(anchor="center")
Radiobutton(screen,text="Deluxe ($200)", variable=room_var,value="Deluxe", bg="lightgrey").pack(anchor="center")
Radiobutton(screen,text="Suit ($500)",variable=room_var,value="Suit",bg="lightgrey").pack(anchor="center")

Button(screen,text="Check In",width=15).pack(pady=15)
Button(screen,text="Check Out",width=15).pack()

screen.mainloop()