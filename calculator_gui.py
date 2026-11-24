import tkinter as tk

# button functions - same logic as before
def click(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def delete_last():
    if display.get():
        display.delete(len(display.get()) - 1, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error: Division by Zero")
    except Exception:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")


# window - dark theme looks more modern
window = tk.Tk()
window.title("Calculator")
window.geometry("340x520")
window.resizable(False, False)
window.configure(bg="#111111")

# outer border frame
main_frame = tk.Frame(window, bg="#1c1c1c", borderwidth=2, relief="solid")
main_frame.pack(fill="both", expand=True, padx=8, pady=8)

for i in range(4):
    main_frame.columnconfigure(i, weight=1)
for i in range(6):
    main_frame.rowconfigure(i, weight=1)

# display - big white text on dark, no boxy border
display = tk.Entry(main_frame, font=("Segoe UI", 26, "bold"), justify="right",
                   bg="#1c1c1c", fg="white", borderwidth=0, insertbackground="white")
display.grid(row=0, column=0, columnspan=4, padx=12, pady=12, ipady=10, sticky="nsew")

buttons_list = [
    ['C', 'DEL', '/', '*'],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '='],
    ['00', '0', '.', ''],
]

row_no = 1
for row in buttons_list:
    col_no = 0
    for value in row:
        if value == "":
            col_no = col_no + 1
            continue

        if value == '=':
            action = calculate
        elif value == 'C':
            action = clear
        elif value == 'DEL':
            action = delete_last
        else:
            action = lambda v=value: click(v)

        # modern flat colours
        if value == 'C':
            colour = "#c0392b"
            text_colour = "white"
        elif value == 'DEL':
            colour = "#7d6608"
            text_colour = "white"
        elif value == '=':
            colour = "#e67e22"
            text_colour = "white"
        elif value in ['+', '-', '*', '/']:
            colour = "#2e86c1"
            text_colour = "white"
        else:
            colour = "#2d2d2d"
            text_colour = "white"

        button = tk.Button(main_frame, text=value, font=("Segoe UI", 15, "bold"),
                           bg=colour, fg=text_colour, activebackground="#444444",
                           activeforeground="white", borderwidth=0, relief="flat",
                           command=action, cursor="hand2")

        if value == '=':
            button.grid(row=row_no, column=col_no, rowspan=2,
                        padx=5, pady=5, sticky="nsew")
        else:
            button.grid(row=row_no, column=col_no,
                        padx=5, pady=5, sticky="nsew")

        col_no = col_no + 1
    row_no = row_no + 1

window.mainloop()