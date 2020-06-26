import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('SaniText text editor')



###################################### main menu ########################################
main_menu = tk.Menu()
#file menu icons
new_icon = tk.PhotoImage(file ='icons2/new.png')
open_icon = tk.PhotoImage(file ='icons2/open.png')
save_icon = tk.PhotoImage(file ='icons2/save.png')
save_as_icon = tk.PhotoImage(file ='icons2/save_as.png')
exit_icon = tk.PhotoImage(file ='icons2/exit.png')
file = tk.Menu(main_menu, tearoff= False)

file.add_command(label ="New", image=new_icon, compound=tk.LEFT)

edit = tk.Menu(main_menu, tearoff= False)
view = tk.Menu(main_menu, tearoff= False)
color_theme = tk.Menu(main_menu, tearoff= False)

# cascade

main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

#------------------------------------ end main menu ------------------------------------#

###################################### toolbar ########################################

#------------------------------------ end toolbar ------------------------------------#

###################################### text editor ########################################

#------------------------------------ end text editor ------------------------------------#

###################################### status bar ########################################

#------------------------------------ end status bar ------------------------------------#

###################################### main menu functionality ########################################

#------------------------------------ end main menu functionality ------------------------------------#


main_application.config(menu=main_menu)
main_application.mainloop()