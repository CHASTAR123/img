from tkinter import *
import pyautogui
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox

class Paint():
    DEFAULTPENSIZE = 5.0
    DEFAULTCOLOUR = 'black'
    DEFAULTCANVASCOLOUR = 'white'
    def __init__(self):
        self.screen = Tk()
        w,h = pyautogui.size()
        print(w,h)
        self.screen.geometry(f'{w}x{h}')
#
        self.menubar = Menu(self.screen)
        file = Menu(self.menubar, tearoff= 1, relief= 'sunken', background= 'lightblue')

#         self.new_btn = Button( self.menubar, text="🆕 NEW", width=15, height=3)
#         self.new_btn.pack(pady=10)

#         self.clear_btn = Button(self.menubar, text="🧹 CLEAR", width=15, height=3)
#         self.clear_btn.pack(pady=10)

#         self.save_btn = Button(self.menubar, text="💾 SAVE", width=15, height=3)
#         self.save_btn.pack(pady=10)

#         self.exit_btn = Button(self.menubar, text="❌ EXIT", width=15, height=3)
#         self.exit_btn.pack(pady=10)
# #
        self.penbutton = Button(self.screen, text = '🖊️PEN',width =20,height= 5,  command = self.use_pen)
        self.penbutton.grid(row = 0, column = 0, padx = 10)

        self.brush = Button(self.screen, text = '🖌️BRUSH',width =20,height= 5, command = self.use_brush)
        self.brush.grid(row = 0, column = 1, padx= 10)

        self.colourbutton = Button(self.screen, text = '🎨COLOUR',width =20,height= 5, command = self.choosecolour)
        self.colourbutton.grid(row = 0, column = 2 ,padx = 10)

        self.eraserbutton = Button(self.screen, text = '🧼ERASER',width =20,height= 5, command = self.use_eraser)
        self.eraserbutton.grid(row = 0, column = 3, padx = 10)

        self.scaler = Scale(self.screen, from_= 1, to = 10, orient= HORIZONTAL)
        self.scaler.grid(row = 0, column = 4)
        self.canvasbutton = Button(self.screen, text = '🖼️CANVASCOLOUR',width =20,height= 5,command=self.change_canvas_colour)
        self.canvasbutton.grid(row = 0, column = 5, padx =10)

        self.savebutton = Button(self.screen, text='💾 SAVE', width=20, height=5, command=self.saveImage)
        self.savebutton.grid(row=0, column=6, padx=10)
        
        self.canvas = Canvas(self.screen, bg = 'white', width = w, height= h - 50)
        self.canvas.grid(row= 1, columnspan = 6 )
        
        self.setup()
        self.screen.mainloop()

    def setup(self):
        self.oldx = None
        self.oldy = None
        self.linewidth = self.scaler.get()
        self.colour = self.DEFAULTCOLOUR
        self.eraseron = False
        self.activebutton = self.penbutton 
        self.canvascolour = self.DEFAULTCANVASCOLOUR
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
    def use_pen(self):
        self.activate_button(self.penbutton)
    def use_brush(self):
        self.activate_button(self.brush)
    def choosecolour(self):
        self.eraser = False
        self.colour  = askcolor(color = self.colour)[1]
    def use_eraser(self):
        self.activate_button(self.eraserbutton, eraserMode= True)

    def change_canvas_colour(self):
        colour = askcolor(color=self.canvascolour)[1]
        if colour:
            self.canvascolour = colour
            self.canvas.config(bg=self.canvascolour)

    def reset(self, event):
        self.oldx = None
        self.oldy = None

    def paint(self, event):
        print('paint')
        self.linewidth =self.scaler.get()
        paintcolour = self.canvascolour if self.eraser else self.colour
        if self.oldx and self.oldy:
            print('paint2')
            self.canvas.create_line(self.oldx, self.oldy, event.x, event.y, width = self.linewidth, fill = paintcolour,capstyle = ROUND, smooth = TRUE, splinesteps = 36)
        self.oldx =event.x
        self.oldy = event.y

    def activate_button(self, button, eraserMode = False):
        self.activebutton.config(relief = RAISED)
        button.config(relief = SUNKEN)
        self.activebutton = button
        self.eraser = eraserMode

    def saveImage(self):
        self.screen.update()

        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        filePath = asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png"), ("JPG Image", "*.jpg")]
        )

        if not filePath:
            messagebox.showwarning("Save Cancelled", "No file selected.")
            return

        screenshot = pyautogui.screenshot(region=(x, y, w, h))
        screenshot.save(filePath)

        messagebox.showinfo("Saved", "Your image has been saved successfully!")





Paint()
