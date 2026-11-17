import random
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def vzorec(x):
    return round(x * 1.20 + 5, 2)

def generuj_a_vykresli():
    pole = []
    for i in range(50):
        cislo = round(random.uniform(10, 100), 2)
        pole.append(cislo)

    pole.sort()
    priemer = round(sum(pole) / len(pole), 2)
    minimum = min(pole)
    maximum = max(pole)

    vypocitane_pole = []
    for x in pole:
        vypocitane_pole.append(vzorec(x))

    stats_label.config(text=f"Priemer: {priemer} €   |   Min: {minimum} €   |   Max: {maximum} €")

    ax.clear()
    ax.plot(pole, label="Vstupná cena bez DPH (€)", color="#1f77b4", marker="o", markersize=3)
    ax.plot(vypocitane_pole, label="Cena s 20 % DPH + 5 €", color="#ff7f0e", linewidth=2)
    ax.set_title("Porovnanie vstupných a vypočítaných hodnôt (50 prvkov)")
    ax.set_xlabel("Poradie prvku")
    ax.set_ylabel("Cena (€)")
    ax.legend()
    ax.grid(True)
    canvas.draw()

def vypocitaj_jednu():
    text = entry_cislo.get().replace(",", ".")
    try:
        hodnota = float(text)
        vysledok = vzorec(hodnota)
        vysledok_label.config(text=f"Výsledok: {vysledok} €", fg="green")
    except ValueError:
        vysledok_label.config(text="Chyba: zadajte číslo!", fg="red")

root = tk.Tk()
root.title("Zadanie 2 – Spracovanie poľa a výpočet ceny")
root.geometry("900x620")

top_frame = tk.Frame(root, padx=10, pady=10)
top_frame.pack(side=tk.TOP, fill=tk.X)

btn_generuj = tk.Button(
    top_frame,
    text="Vygenerovať nové pole (50 prvkov)",
    command=generuj_a_vykresli,
    bg="#0052cc",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5
)
btn_generuj.pack(side=tk.LEFT)

stats_label = tk.Label(top_frame, text="", font=("Arial", 10, "bold"), padx=15)
stats_label.pack(side=tk.LEFT)

calc_frame = tk.LabelFrame(root, text="Výpočet podľa vzorca: y = x * 1.20 + 5", padx=10, pady=8)
calc_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

tk.Label(calc_frame, text="Zadajte základnú cenu (€):", font=("Arial", 10)).pack(side=tk.LEFT)

entry_cislo = tk.Entry(calc_frame, width=15, font=("Arial", 10))
entry_cislo.insert(0, "50")
entry_cislo.pack(side=tk.LEFT, padx=8)

btn_vypocitaj = tk.Button(calc_frame, text="Vypočítať", command=vypocitaj_jednu, font=("Arial", 10), padx=10)
btn_vypocitaj.pack(side=tk.LEFT)

vysledok_label = tk.Label(calc_frame, text="", font=("Arial", 10, "bold"), padx=12)
vysledok_label.pack(side=tk.LEFT)

fig = Figure(figsize=(8, 4.5), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

generuj_a_vykresli()
vypocitaj_jednu()

root.mainloop()