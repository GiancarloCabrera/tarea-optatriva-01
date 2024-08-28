import tkinter as tk
from tkinter import ttk

from perfect_destinations import generate_suggestion

def suggest_destinations():
    likes = likes_var.get() if likes_var.get() else None
    travel_type = travel_type_var.get() if travel_type_var.get() else None
    budget = budget_var.get() if budget_var.get() else None

    suggestions = generate_suggestion(likes, travel_type, budget)

    output_var.set(", ".join(suggestions) if suggestions else "No suggestions available")

window = tk.Tk()
window.title("Perfect Getaways")
window.geometry("400x300")

likes_var = tk.StringVar()
travel_type_var = tk.StringVar()
budget_var = tk.StringVar()
output_var = tk.StringVar()

frame = ttk.Frame(window, padding="20 20 20 20")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

ttk.Label(frame, text="Likes:").grid(column=1, row=1, sticky=tk.W, pady=5)
likes_menu = ttk.Combobox(frame, textvariable=likes_var)
likes_menu['values'] = ("adventure", "beach", "city", "nature", "culture")
likes_menu.grid(column=2, row=1, sticky=tk.EW, pady=5)

ttk.Label(frame, text="Travel Type:").grid(column=1, row=2, sticky=tk.W, pady=5)
travel_type_menu = ttk.Combobox(frame, textvariable=travel_type_var)
travel_type_menu['values'] = ("solo", "family", "group")
travel_type_menu.grid(column=2, row=2, sticky=tk.EW, pady=5)

ttk.Label(frame, text="Budget:").grid(column=1, row=3, sticky=tk.W, pady=5)
budget_menu = ttk.Combobox(frame, textvariable=budget_var)
budget_menu['values'] = ("low", "medium", "high")
budget_menu.grid(column=2, row=3, sticky=tk.EW, pady=5)

ttk.Button(frame, text="Suggest Destination", command=suggest_destinations).grid(column=2, row=4, pady=10)

ttk.Label(frame, text="Suggestions:").grid(column=1, row=5, sticky=tk.W, pady=5)
ttk.Label(frame, textvariable=output_var, wraplength=300).grid(column=2, row=5, sticky=tk.W, pady=5)

for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=5)

window.mainloop()
