import tkinter as tk

rekenen = ""

def add_to_rekenen(symbol):
    global rekenen
    rekenen += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, rekenen)

def evaluate_rekenen():
    global rekenen
    try:
        rekenen = str(eval(rekenen))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, rekenen)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global rekenen
    rekenen = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("650x600")

text_result = tk.Text(root, height=2, width=16, font=("Magnolia Script", 50))
text_result.grid(columnspan=5)

#row 2
btn_1 = tk.Button(root, text="1", command=lambda: add_to_rekenen(1), width=5, font=("Magnolia Script", 30))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_rekenen(2), width=5, font=("Magnolia Script", 30))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_rekenen(3), width=5, font=("Magnolia Script", 30))
btn_3.grid(row=2, column=3)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_rekenen("+"), width=5, font=("Magnolia Script", 30))
btn_plus.grid(row=2, column=4)
#row 3
btn_4 = tk.Button(root, text="4", command=lambda: add_to_rekenen(4), width=5, font=("Magnolia Script", 30))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_rekenen(5), width=5, font=("Magnolia Script", 30))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_rekenen(6), width=5, font=("Magnolia Script", 30))
btn_6.grid(row=3, column=3)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_rekenen("-"), width=5, font=("Magnolia Script", 30))
btn_minus.grid(row=3, column=4)
#row 4
btn_7 = tk.Button(root, text="7", command=lambda: add_to_rekenen(7), width=5, font=("Magnolia Script", 30))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_rekenen(8), width=5, font=("Magnolia Script", 30))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_rekenen(9), width=5, font=("Magnolia Script", 30))
btn_9.grid(row=4, column=3)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_rekenen("*"), width=5, font=("Magnolia Script", 30))
btn_mul.grid(row=4, column=4)
#row 5
btn_0 = tk.Button(root, text="0", command=lambda: add_to_rekenen(0), width=5, font=("Magnolia Script", 30))
btn_0.grid(row=5, column=2)
btn_dev = tk.Button(root, text="/", command=lambda: add_to_rekenen("/"), width=5, font=("Magnolia Script", 30))
btn_dev.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: add_to_rekenen("("), width=5, font=("Magnolia Script", 30))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_rekenen(")"), width=5, font=("Magnolia Script", 30))
btn_close.grid(row=5, column=3)
#row 6
btn_is  = tk.Button(root, text="=", command=evaluate_rekenen, width=11, font=("Magnolia Script", 30))
btn_is.grid(row=6, column=1, columnspan=2)
btn_clear  = tk.Button(root, text="C", command=clear_field, width=11, font=("Magnolia Script", 30))
btn_clear.grid(row=6, column=3, columnspan=2)

root.mainloop()
