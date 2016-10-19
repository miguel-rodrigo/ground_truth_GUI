import tkinter as tk
import database

root = tk.Tk()
root.geometry("400x300+30+30")

db = database.Database('docs_osborne', 'testuser', 'test123', ('sellos', 'documentos'))
db.load_seals()

# POINT 1 DISPLAY
pt1_label = tk.Label(root, text="Point 1:")
pt1_label.place(x=20, y=10)

pt1x_value = tk.StringVar()
pt1x_info = tk.Entry(root, state=tk.DISABLED, textvariable=pt1x_value)
pt1x_info.place(x=70, y=10, width=50)
pt1x_value.set("hola")

pt1y_value = tk.StringVar()
pt1y_info = tk.Entry(root, state=tk.DISABLED, textvariable=pt1y_value)
pt1y_info.place(x=130, y=10, width=50)
pt1y_value.set("hola")


# POINT 2 DISPLAY
pt2_label = tk.Label(root, text="Point 2:")
pt2_label.place(x=20, y=30)

pt2x_value = tk.StringVar()
pt2x_info = tk.Entry(root, state=tk.DISABLED, textvariable=pt2x_value)
pt2x_info.place(x=70, y=30, width=50)
pt2x_value.set("hola")

pt2y_value = tk.StringVar()
pt2y_info = tk.Entry(root, state=tk.DISABLED, textvariable=pt2y_value)
pt2y_info.place(x=130, y=30, width=50)
pt2y_value.set("hola")


# SEAL TYPE LIST
type_label = tk.Label(root, text="Type:")
type_label.place(x=20, y=70)

OPTIONS = []
for seal in db.seal_list:
    OPTIONS.append(seal.name)

seal_type = tk.StringVar(root)
seal_type.set(OPTIONS[0])  # initial value

option = tk.OptionMenu(root, seal_type, *OPTIONS)
option.place(x=55, y=70)

root.mainloop()

# TODO: Create control panel
