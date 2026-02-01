# La Programmazione Orientata agli Oggetti (OOP) è un paradigma di programmazione che utilizza "oggetti" per rappresentare dati e metodi.
# Una 'classe' è un progetto, un modello, per creare oggetti.
# Un 'oggetto' è un'istanza di una classe.

# 1. Definire una classe
# Si usa la parola chiave 'class'. Per convenzione, i nomi delle classi usano il formato 'CamelCase'.
class Cane:
    # Questo è un 'attributo di classe'. È condiviso da tutte le istanze (oggetti) della classe.
    specie = "Canis lupus familiaris"

    # Il metodo '__init__' è un metodo speciale chiamato "costruttore".
    # Viene eseguito automaticamente quando si crea un nuovo oggetto dalla classe.
    # 'self' si riferisce all'istanza specifica dell'oggetto che viene creata.
    def __init__(self, nome, eta):
        # Questi sono 'attributi di istanza'. Ogni oggetto Cane avrà il proprio nome e la propria età.
        self.nome = nome
        self.eta = eta
        print(f"È nato un cane di nome {self.nome}!")

    # Questo è un 'metodo di istanza'. Può accedere e modificare gli attributi dell'istanza.
    def abbaia(self):
        return f"{self.nome} fa: Bau bau!"

    def compleanno(self):
        self.eta += 1
        return f"Buon compleanno, {self.nome}! Ora hai {self.eta} anni."

    # Anche i metodi speciali (chiamati 'dunder' o 'magic methods') sono importanti.
    # '__str__' definisce come l'oggetto deve essere rappresentato come stringa (es. quando si usa print()).
    def __str__(self):
        return f"Cane(nome='{self.nome}', eta={self.eta}, specie='{self.specie}')"


# 2. Creare un oggetto (un'istanza della classe)
# Ora che abbiamo il progetto (la classe Cane), possiamo creare degli oggetti cane.
mio_cane = Cane("Fido", 3) # Questo chiama il metodo __init__
altro_cane = Cane("Lilli", 1)


# 3. Accedere agli attributi e chiamare i metodi
# Si usa la notazione col punto (.) per accedere agli attributi e ai metodi di un oggetto.

# Accesso agli attributi di istanza
print(f"\nIl nome del mio cane è {mio_cane.nome}.")
print(f"L'età di Lilli è {altro_cane.eta} anni.")

# Accesso all'attributo di classe (si può accedere tramite la classe o l'istanza)
print(f"La specie di Fido è {mio_cane.specie}.")
print(f"Tutti i cani appartengono alla specie {Cane.specie}.")

# Chiamata dei metodi di istanza
print(f"\n{mio_cane.abbaia()}")
print(altro_cane.compleanno())
print(f"L'età di Lilli ora è {altro_cane.eta} anni.")


# 4. Usare la rappresentazione in stringa
# Chiamando print() su un oggetto, Python cerca e usa il metodo __str__ se definito.
print("\nStampa degli oggetti cane:")
print(mio_cane)
print(altro_cane)

# Cosa succederebbe se __str__ non fosse definito?
# Python stamperebbe una rappresentazione di default, meno leggibile, come:
# <__main__.Cane object at 0x10f4e3c50>
