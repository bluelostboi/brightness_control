from tkinter import * 
import screen_brightness_control as sbc
  
root = Tk()  
root.title('Brightness Control')
monitors = sbc.list_monitors()

def create_slider(v, monitor):
    # v = IntVar()
    def change(v):
        sbc.set_brightness(v,display=monitor)
    s1 = Scale( root, variable = v, 
           from_ = 0, to = 100, 
           orient = HORIZONTAL,
           length = 250,
           command=change,
           label = monitor,
           )
    return s1

for monitor in monitors:
    v = IntVar()
    v.set(sbc.get_brightness(display=monitor))
    s = create_slider(v, monitor)
    s.pack(anchor=CENTER)

root.geometry(f"300x{70*len(monitors)}")
root.mainloop()
