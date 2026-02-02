# Le funzioni sono blocchi di codice riutilizzabili che eseguono un'azione specifica.
# Permettono di organizzare il codice in modo più logico, renderlo più leggibile e facile da manutenere.

# 1. Definire e chiamare una funzione
# Si usa la parola chiave 'def' per definire una funzione.
def saluta():
    """
    Questa è una docstring. Fornisce una breve spiegazione di cosa fa la funzione.
    Questa funzione stampa un semplice saluto.
    """
    print("Ciao! Benvenuto nel mondo delle funzioni Python.")

# Per eseguire il codice all'interno della funzione, dobbiamo "chiamarla".
print("Sto per chiamare la funzione 'saluta':")
saluta()


# 2. Parametri e argomenti
# Le funzioni possono accettare input, chiamati parametri.
# Quando chiamiamo la funzione, passiamo dei valori chiamati argomenti.
def saluta_persona(nome):
    """Questa funzione saluta una persona usando il nome fornito."""
    print(f"Ciao, {nome}!")

saluta_persona("Alice") # "Alice" è l'argomento
saluta_persona("Bob")


# 3. L'istruzione 'return'
# Le funzioni possono "restituire" un valore al codice che le ha chiamate.
def somma(a, b):
    """Questa funzione prende due numeri come input e restituisce la loro somma."""
    return a + b

risultato_somma = somma(5, 3)
print(f"\nIl risultato della funzione somma è: {risultato_somma}")
print(f"Puoi anche usarla direttamente: 10 + 20 = {somma(10, 20)}")


# 4. Parametri con valori di default
# È possibile specificare un valore di default per un parametro.
# Se l'argomento non viene fornito quando la funzione è chiamata, viene usato il valore di default.
def saluta_con_default(nome="Mondo"):
    """Saluta una persona, ma se non viene specificato il nome, saluta il mondo."""
    print(f"Ciao, {nome}!")

saluta_con_default("Giuseppe")
saluta_con_default() # Non passando l'argomento, usa il default "Mondo"


# 5. Argomenti posizionali e con parola chiave (keyword arguments)
def descrizione_animale(tipo_animale, nome_animale):
    """Mostra informazioni su un animale."""
    print(f"\nHo un {tipo_animale}.")
    print(f"Il mio {tipo_animale} si chiama {nome_animale}.")

# Chiamata con argomenti posizionali (l'ordine conta)
descrizione_animale("cane", "Fido")

# Chiamata con argomenti con parola chiave (l'ordine non conta)
descrizione_animale(nome_animale="Leo", tipo_animale="gatto")


# 6. Numero arbitrario di argomenti posizionali (*args)
# A volte non sai in anticipo quanti argomenti una funzione dovrà accettare.
# *args permette di passare un numero variabile di argomenti posizionali.
# Questi vengono raccolti in una tupla.
def somma_tutti(*numeri):
    """Somma tutti i numeri passati come argomenti."""
    print(f"\nArgomenti ricevuti con *args: {numeri}")
    totale = 0
    for numero in numeri:
        totale += numero
    return totale

print(f"La somma di 1, 2, 3 è: {somma_tutti(1, 2, 3)}")
print(f"La somma di 10, 20, 30, 40, 50 è: {somma_tutti(10, 20, 30, 40, 50)}")


# 7. Numero arbitrario di argomenti con parola chiave (**kwargs)
# **kwargs permette di passare un numero variabile di argomenti con parola chiave.
# Questi vengono raccolti in un dizionario.
def crea_profilo(nome, cognome, **info_aggiuntive):
    """Crea un profilo utente."""
    profilo = {'nome': nome, 'cognome': cognome}
    print(f"\nArgomenti ricevuti con **kwargs: {info_aggiuntive}")
    profilo.update(info_aggiuntive)
    return profilo

profilo_utente = crea_profilo("Maria", "Verdi", eta=28, citta="Napoli", professione="Avvocato")
print(f"Profilo creato: {profilo_utente}")


# 8. Ambito delle variabili (Scope)
# Le variabili definite all'interno di una funzione sono locali a quella funzione.
# Non possono essere viste o modificate dall'esterno.
def funzione_con_variabile_locale():
    variabile_locale = "Sono locale"
    print(variabile_locale)

funzione_con_variabile_locale()
# print(variabile_locale) # -> NameError: name 'variabile_locale' is not defined

# Le variabili definite all'esterno sono globali.
variabile_globale = "Sono globale"

def funzione_che_usa_globale():
    # Si può accedere in lettura a una variabile globale
    print(f"All'interno della funzione: {variabile_globale}")

funzione_che_usa_globale()

# Per modificare una variabile globale dall'interno di una funzione, si usa la parola chiave 'global'.
def funzione_che_modifica_globale():
    global variabile_globale
    variabile_globale = "Sono stata modificata!"

funzione_che_modifica_globale()
print(f"Dopo la modifica: {variabile_globale}")
