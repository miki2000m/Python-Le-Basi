# Questo è un modulo Python.
# Un modulo è semplicemente un file .py che contiene definizioni e istruzioni Python.
# Possiamo definire funzioni, classi e variabili in un modulo e riutilizzarle in altri file.

print("Il file 'mymodule.py' è stato importato o eseguito.")

# Una variabile definita nel modulo
PI_GRECO = 3.14159

# Una funzione definita nel modulo
def saluta(nome):
    """Saluta una persona."""
    return f"Ciao da mymodule, {nome}!"

# Una classe definita nel modulo
class CalcolatriceSemplice:
    def somma(self, a, b):
        return a + b
    
    def moltiplica(self, a, b):
        return a * b

# Blocco di codice che viene eseguito SOLO quando il file viene eseguito direttamente
# e NON quando viene importato come modulo in un altro file.
# È utile per testare il codice all'interno del modulo stesso.
if __name__ == "__main__":
    print("\nEsecuzione del modulo 'mymodule.py' come script principale.")
    print("Questo codice non viene eseguito quando 'mymodule' viene importato.")
    
    print(saluta("Test"))
    
    calcolatrice_test = CalcolatriceSemplice()
    print(f"Test della calcolatrice: 5 + 3 = {calcolatrice_test.somma(5, 3)}")
