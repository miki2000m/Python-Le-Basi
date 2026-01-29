# L'ereditarietà è uno dei pilastri della Programmazione Orientata agli Oggetti (OOP).
# Permette a una nuova classe (chiamata 'classe figlia' o 'sottoclasse') di
# ereditare attributi e metodi da una classe esistente (chiamata 'classe madre' o 'superclasse').

# Questo promuove il riutilizzo del codice e una struttura logica gerarchica.

# --- Definiamo una classe madre ---
class Animale:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        print(f"Creato un Animale di nome {self.nome}")

    def mangia(self):
        return f"{self.nome} sta mangiando."

    def __str__(self):
        return f"Animale(nome='{self.nome}', eta={self.eta})"


# --- Definiamo una classe figlia ---
# Per ereditare da Animale, mettiamo il nome della classe madre tra parentesi.
class Cane(Animale):
    # La classe Cane eredita automaticamente __init__, mangia(), e __str__ da Animale.

    # Possiamo estendere la classe figlia con nuovi metodi.
    def abbaia(self):
        return f"{self.nome} fa: Bau bau!"


# --- Definiamo un'altra classe figlia che sovrascrive un metodo ---
class Gatto(Animale):
    # Possiamo sovrascrivere (override) un metodo della classe madre per cambiarne il comportamento.
    def mangia(self):
        return f"{self.nome} sta mangiando il suo cibo per gatti preferito."

    # Aggiungiamo un nuovo metodo specifico per Gatto.
    def miagola(self):
        return f"{self.nome} fa: Meeeow!"


# --- Usiamo le classi ---

# 1. Creiamo un oggetto della classe madre
animale_generico = Animale("Creatura", 5)
print(animale_generico.mangia())
print(animale_generico)


# 2. Creiamo un oggetto della classe figlia 'Cane'
print("\n--- Esempio con Cane ---")
fido = Cane("Fido", 3)
# Fido può usare il metodo 'mangia' ereditato da Animale
print(fido.mangia())
# Fido può usare il suo metodo specifico 'abbaia'
print(fido.abbaia())
# Anche il metodo __str__ è ereditato
print(fido)


# 3. Creiamo un oggetto della classe figlia 'Gatto'
print("\n--- Esempio con Gatto ---")
silvestro = Gatto("Silvestro", 2)
# Silvestro usa la versione sovrascritta (override) del metodo 'mangia'
print(silvestro.mangia())
# E può usare il suo metodo 'miagola'
print(silvestro.miagola())


# --- La funzione super() ---
# 'super()' permette di chiamare un metodo dalla classe madre all'interno della classe figlia.
# È molto utile quando si vuole estendere il costruttore __init__ senza riscriverlo da capo.

class PastoreTedesco(Cane):
    def __init__(self, nome, eta, pedigree):
        # Chiama l'__init__ della classe madre (Cane, che a sua volta chiama Animale)
        # per impostare nome ed età.
        super().__init__(nome, eta)

        # Ora aggiungiamo l'attributo specifico per PastoreTedesco.
        self.pedigree = pedigree
        print(f"È un Pastore Tedesco con pedigree: {self.pedigree}")

    # Estendiamo il metodo abbaia
    def abbaia(self):
        # Possiamo chiamare il metodo originale della classe madre se vogliamo
        abbaio_originale = super().abbaia()
        return f"{abbaio_originale} È un abbaio molto forte!"


print("\n--- Esempio con super() ---")
rex = PastoreTedesco("Rex", 4, "Sì")
print(rex.mangia()) # Ereditato da Animale
print(rex.abbaia()) # Metodo sovrascritto/esteso in PastoreTedesco
print(f"Rex ha il pedigree? {rex.pedigree}")
