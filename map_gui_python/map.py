from tkinter import *
import tkintermapview


root = Tk()
root.title('Codemy.com - Tkinter MapView')
# root.iconvitmap()
root.geometry('900x600')

my_label = LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=800, height=600, corner_radius=5)
map_widget.pack()

map_widget.set_position( 52.26,21.0)
map_widget.set_zoom(18)

marker_1 = map_widget.set_position(52.26,21.0, marker=True)
marker_1.set_text("geoinformatyka rządzi oouuu yeah")
marker_2 = map_widget.set_marker(52.516268, 13.377695, text="Brandenburger Tor")


def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")


map_widget.add_right_click_menu_command(label="Add Marker",
                                        command=add_marker_event,
                                        pass_coords=True)


def left_click_event(coordi
    nates_tuple):
    print("Left click event with coordinates:", coordinates_tuple)


map_widget.add_left_click_map_command(left_click_event)

root.mainloop()