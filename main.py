import tkinter as tk
from tkinter import ttk
from Managers.WindowManager import WindowManager

wm = WindowManager()

def list_windows():
    windows = wm.get_active(search_entry.get())
    for item in tree.get_children():
        tree.delete(item)
    for w in windows:
        tree.insert("", "end", values=(w._hWnd, w.title, f"{w.left}, {w.top}"))

def on_tree_item_click(event):
    if not tree.selection():
        return
    selected_item = tree.selection()[0]
    if selected_item:
        item_values = tree.item(selected_item, "values")
        window_id = item_values[0]
        wm.focus_by_handle(window_id)

root = tk.Tk()
root.title("Window Manager")

search_frame = ttk.Frame(root)
search_frame.pack(pady=5, fill=tk.X)

search_label = ttk.Label(search_frame, text="Search:")
search_label.pack(side=tk.LEFT, padx=5)
search_entry = ttk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
search_entry.bind("<Return>", lambda event: list_windows())
button = ttk.Button(search_frame, text="List", command=list_windows)
button.pack(side=tk.LEFT, padx=10)

tree = ttk.Treeview(root, columns=("id", "title", "position"), show="headings")
tree.heading("id", text="ID")
tree.heading("title", text="Title")
tree.heading("position", text="Position (x, y)")
tree.pack(pady=5, fill=tk.BOTH, expand=True)
tree.bind("<Button-1>", on_tree_item_click)

root.mainloop()