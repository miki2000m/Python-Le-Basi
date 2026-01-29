# Il programmatore oltre a lavorare molto con i numeri e le operazioni matematiche, lavora anche con le stringhe.
# Le stringhe sono sequenze di caratteri racchiuse tra virgolette singole (' ') o virgolette doppie (" ").
# Python offre una vasta gamma di metodi per manipolare e lavorare con le stringhe in modo efficiente.

# 1. Creazione e lunghezza di stringhe
testo = "Python è fantastico!"
print(f"Testo originale: {testo}")

# len() -> conta quanti caratteri ci sono in una stringa
lunghezza = len(testo)
print(f"La lunghezza del testo è: {lunghezza}")


# 2. Metodi di trasformazione (modificano il formato della stringa)

# .upper() -> converte tutti i caratteri in maiuscolo
maiuscolo = testo.upper()
print(f"\n.upper(): {maiuscolo}")

# .lower() -> converte tutti i caratteri in minuscolo
minuscolo = testo.lower()
print(f".lower(): {minuscolo}")

# .capitalize() -> converte solo il primo carattere in maiuscolo
capitalizzato = "ciao mondo".capitalize()
print(f".capitalize(): {capitalizzato}")

# .title() -> converte la prima lettera di ogni parola in maiuscolo
titolo = "ciao mondo python".title()
print(f".title(): {titolo}")

# .swapcase() -> inverte maiuscole e minuscole
invertito = "Ciao Mondo".swapcase()
print(f".swapcase(): {invertito}")


# 3. Metodi di ricerca e verifica

# .find() -> trova la posizione della prima occorrenza di una sottostringa (ritorna -1 se non trovata)
posizione = testo.find("è")
print(f"\n.find('è'): {posizione}")

# .index() -> simile a find() ma genera un errore se non trova la sottostringa
posizione_index = testo.index("Python")
print(f".index('Python'): {posizione_index}")

# .count() -> conta quante volte appare una sottostringa
conteggio = "banana".count("a")
print(f".count('a') in 'banana': {conteggio}")

# .startswith() -> verifica se la stringa inizia con una determinata sottostringa
inizia = testo.startswith("Python")
print(f".startswith('Python'): {inizia}")

# .endswith() -> verifica se la stringa finisce con una determinata sottostringa
finisce = testo.endswith("!")
print(f".endswith('!'): {finisce}")


# 4. Metodi di validazione (restituiscono True o False)

# .isalpha() -> verifica se tutti i caratteri sono lettere
solo_lettere = "Python".isalpha()
print(f"\n.isalpha() su 'Python': {solo_lettere}")

# .isdigit() -> verifica se tutti i caratteri sono cifre
solo_numeri = "12345".isdigit()
print(f".isdigit() su '12345': {solo_numeri}")

# .isalnum() -> verifica se tutti i caratteri sono lettere o numeri
alfanumerico = "Python3".isalnum()
print(f".isalnum() su 'Python3': {alfanumerico}")

# .isspace() -> verifica se tutti i caratteri sono spazi bianchi
solo_spazi = "   ".isspace()
print(f".isspace() su '   ': {solo_spazi}")

# .isupper() -> verifica se tutti i caratteri sono maiuscoli
tutto_maiuscolo = "PYTHON".isupper()
print(f".isupper() su 'PYTHON': {tutto_maiuscolo}")

# .islower() -> verifica se tutti i caratteri sono minuscoli
tutto_minuscolo = "python".islower()
print(f".islower() su 'python': {tutto_minuscolo}")


# 5. Metodi di pulizia e formattazione

# .strip() -> rimuove spazi bianchi all'inizio e alla fine
con_spazi = "   ciao   "
senza_spazi = con_spazi.strip()
print(f"\n.strip() su '{con_spazi}': '{senza_spazi}'")

# .lstrip() -> rimuove spazi bianchi solo all'inizio
sinistra = con_spazi.lstrip()
print(f".lstrip() su '{con_spazi}': '{sinistra}'")

# .rstrip() -> rimuove spazi bianchi solo alla fine
destra = con_spazi.rstrip()
print(f".rstrip() su '{con_spazi}': '{destra}'")

# .replace() -> sostituisce una sottostringa con un'altra
sostituito = testo.replace("fantastico", "meraviglioso")
print(f".replace('fantastico', 'meraviglioso'): {sostituito}")


# 6. Metodi di divisione e unione

# .split() -> divide la stringa in una lista di sottostringhe
frase = "Python è un linguaggio potente"
parole = frase.split()  # Di default divide per spazi
print(f"\n.split() su '{frase}': {parole}")

# .split() con separatore personalizzato
data = "2024-01-15"
parti_data = data.split("-")
print(f".split('-') su '{data}': {parti_data}")

# .join() -> unisce gli elementi di una lista in una stringa
lista_parole = ["Python", "è", "fantastico"]
frase_unita = " ".join(lista_parole)
print(f".join() su {lista_parole}: {frase_unita}")


# 7. Metodi di allineamento e riempimento

# .center() -> centra la stringa in un campo di una data larghezza
centrato = "Python".center(20, "-")
print(f"\n.center(20, '-'): {centrato}")

# .ljust() -> allinea a sinistra
sinistra_align = "Python".ljust(20, "-")
print(f".ljust(20, '-'): {sinistra_align}")

# .rjust() -> allinea a destra
destra_align = "Python".rjust(20, "-")
print(f".rjust(20, '-'): {destra_align}")

# .zfill() -> riempie con zeri a sinistra
numero = "42"
con_zeri = numero.zfill(5)
print(f".zfill(5) su '42': {con_zeri}")


# 8. Accesso ai caratteri e slicing

# Accesso tramite indice (come le liste)
primo_carattere = testo[0]
print(f"\nPrimo carattere di '{testo}': {primo_carattere}")

ultimo_carattere = testo[-1]
print(f"Ultimo carattere: {ultimo_carattere}")

# Slicing (estrazione di sottostringhe)
sottostringa = testo[0:6]  # Dal carattere 0 al 5 (6 escluso)
print(f"Slicing [0:6]: {sottostringa}")

# Slicing con step
ogni_due = testo[::2]  # Prende un carattere ogni due
print(f"Slicing [::2] (ogni due caratteri): {ogni_due}")

# Inversione di una stringa
inverso = testo[::-1]
print(f"Stringa invertita [::-1]: {inverso}")


# 9. Formattazione avanzata

# f-strings (il modo migliore e più moderno)
nome = "Alice"
eta = 25
messaggio = f"{nome} ha {eta} anni."
print(f"\nf-string: {messaggio}")

# .format() (metodo più vecchio ma ancora usato)
messaggio_format = "{} ha {} anni.".format(nome, eta)
print(f".format(): {messaggio_format}")

# Con indici
messaggio_indici = "{1} ha {0} anni.".format(eta, nome)
print(f".format() con indici: {messaggio_indici}")

# Con nomi
messaggio_nomi = "{n} ha {e} anni.".format(n=nome, e=eta)
print(f".format() con nomi: {messaggio_nomi}")


# 10. Concatenazione di stringhe

# Operatore +
stringa1 = "Ciao"
stringa2 = "Mondo"
concatenata = stringa1 + " " + stringa2
print(f"\nConcatenazione con +: {concatenata}")

# Ripetizione con *
ripetuta = "Python! " * 3
print(f"Ripetizione con *: {ripetuta}")


# 11. Caratteri speciali ed escape

# \n -> nuova riga
# \t -> tabulazione
# \\ -> backslash
# \" -> virgolette doppie
# \' -> virgolette singole

testo_escape = "Prima riga\nSeconda riga\tcon tabulazione"
print(f"\nCaratteri di escape:\n{testo_escape}")

# Raw strings (ignorano gli escape)
percorso = r"C:\nuova\cartella"
print(f"Raw string: {percorso}")


# 12. Esempio pratico: validazione input utente
print("\n--- Esempio pratico ---")
email = input("Inserisci la tua email: ")

# Validazione semplice
if "@" in email and "." in email:
    print("Email valida!")
    # Estrai il nome utente (parte prima della @)
    nome_utente = email.split("@")[0]
    print(f"Nome utente: {nome_utente}")
else:
    print("Email non valida!")