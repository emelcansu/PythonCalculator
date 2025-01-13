import tkinter as tk

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Calculator")

# Pencerenin boyutlarını ayarla
root.geometry("400x500")

def calculate():
    try:
        # Giriş alanındaki ifadeyi al
        expression = entry.get()
        # İfade hesapla ve sonucu giriş alanına yaz
        result = eval(expression)
        entry.delete(0, tk.END)  # Önce mevcut metni sil
        entry.insert(tk.END, str(result))  # Sonuç metnini ekle
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear_entry():
    entry.delete(0, tk.END)  # Giriş alanındaki tüm metni sil

def backspace():
    # İmlecin pozisyonunu al
    index = entry.index(tk.INSERT)
    if index > 0:
        entry.delete(index-1, index)  # İmlecin önündeki karakteri sil


entry = tk.Entry(root, font=('Arial', 22), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.place(x=30, y=50)

button0 = tk.Button(root, text='0', font=('Arial', 22), command=lambda: entry.insert(tk.END, '0'))
button0.place(x=100, y=430, width=70, height=70)

button1 = tk.Button(root, text='1', font=('Arial', 22), command=lambda: entry.insert(tk.END, '1'))
button1.place(x=30, y=360, width=70, height=70)

button2 = tk.Button(root, text='2', font=('Arial', 22), command=lambda: entry.insert(tk.END, '2'))
button2.place(x=100, y=360, width=70, height=70)

button3= tk.Button(root, text='3', font=('Arial', 22), command=lambda: entry.insert(tk.END, '3'))
button3.place(x=170, y=360, width=70, height=70)

button4= tk.Button(root, text='4', font=('Arial', 22), command=lambda: entry.insert(tk.END, '4'))
button4.place(x=30, y=290, width=70, height=70)

button5 = tk.Button(root, text='5', font=('Arial', 22), command=lambda: entry.insert(tk.END, '5'))
button5.place(x=100, y=290, width=70, height=70)

button6 = tk.Button(root, text='6', font=('Arial', 22), command=lambda: entry.insert(tk.END, '6'))
button6.place(x=170, y=290, width=70, height=70)

button7 = tk.Button(root, text='7', font=('Arial', 22), command=lambda: entry.insert(tk.END, '7'))
button7.place(x=30, y=220, width=70, height=70)

button8 = tk.Button(root, text='8', font=('Arial', 22), command=lambda: entry.insert(tk.END, '8'))
button8.place(x=100, y=220, width=70, height=70)

button9 = tk.Button(root, text='9', font=('Arial', 22), command=lambda: entry.insert(tk.END, '9'))
button9.place(x=170, y=220, width=70, height=70)

button10 = tk.Button(root, text='+', font=('Arial', 22), command=lambda: entry.insert(tk.END, '+'))
button10.place(x=240, y=360, width=70, height=70)

button11 = tk.Button(root, text='-', font=('Arial', 22), command=lambda: entry.insert(tk.END, '-'))
button11.place(x=240, y=290, width=70, height=70)

button12 = tk.Button(root, text='*', font=('Arial', 22), command=lambda: entry.insert(tk.END, '*'))
button12.place(x=240, y=220, width=70, height=70)

button13 = tk.Button(root, text='/', font=('Arial', 22), command=lambda: entry.insert(tk.END, '/'))
button13.place(x=240, y=150, width=70, height=70)

button15 = tk.Button(root, text=',', font=('Arial', 22), command=lambda: entry.insert(tk.END, ','))
button15.place(x=170, y=430, width=70, height=70)

button16 = tk.Button(root, text='=', font=('Arial', 22), command=calculate)
button16.place(x=240, y=430, width=70, height=70)

button14 = tk.Button(root, text='C', font=('Arial', 22), command=clear_entry)
button14.place(x=30, y=150, width=70, height=70)

button17 = tk.Button(root, text='backspace', font=('Arial', 10), command=backspace)
button17.place(x=100, y=150, width=70, height=70)


# Pencereyi başlat
root.mainloop()