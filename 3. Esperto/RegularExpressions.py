# Le espressioni regolari (regex) sono pattern usati per cercare e manipolare testo.
# In Python, il modulo 're' fornisce supporto completo per le regex.

import re

# 1. Introduzione alle espressioni regolari

print("--- Introduzione ---")
print("""
Le regex sono pattern di ricerca per testo:
- Trovare pattern specifici in stringhe
- Validare formati (email, telefono, ecc.)
- Estrarre informazioni da testo
- Sostituire parti di testo
""")


# 2. Funzioni base del modulo re

# 2.1 re.search() - Cerca il pattern nella stringa
testo = "Python è fantastico! Python è potente!"
risultato = re.search(r"Python", testo)

print("\n--- re.search() ---")
if risultato:
    print(f"Pattern trovato: '{risultato.group()}'")
    print(f"Posizione: {risultato.start()}-{risultato.end()}")


# 2.2 re.match() - Cerca il pattern solo all'inizio della stringa
print("\n--- re.match() ---")
match1 = re.match(r"Python", "Python è fantastico")
match2 = re.match(r"Python", "Io amo Python")

print(f"Match all'inizio: {match1 is not None}")  # True
print(f"Match non all'inizio: {match2 is not None}")  # False


# 2.3 re.findall() - Trova tutte le occorrenze
print("\n--- re.findall() ---")
testo = "Python 3.9, Python 3.10, Python 3.11"
versioni = re.findall(r"Python \d+\.\d+", testo)
print(f"Versioni trovate: {versioni}")


# 2.4 re.finditer() - Restituisce un iteratore di match
print("\n--- re.finditer() ---")
for match in re.finditer(r"Python", "Python è fantastico! Python è potente!"):
    print(f"Trovato '{match.group()}' alla posizione {match.start()}")


# 2.5 re.sub() - Sostituisce pattern
print("\n--- re.sub() ---")
testo = "Ciao mondo! Ciao Python!"
nuovo_testo = re.sub(r"Ciao", "Hello", testo)
print(f"Originale: {testo}")
print(f"Modificato: {nuovo_testo}")


# 3. Caratteri speciali e metacaratteri

print("\n--- Metacaratteri ---")

# . (punto) - Qualsiasi carattere tranne newline
pattern = re.findall(r"P.thon", "Python Pithon P@thon")
print(f". (qualsiasi carattere): {pattern}")

# ^ - Inizio della stringa
match = re.search(r"^Python", "Python è fantastico")
print(f"^ (inizio stringa): {match is not None}")

# $ - Fine della stringa
match = re.search(r"fantastico$", "Python è fantastico")
print(f"$ (fine stringa): {match is not None}")

# * - 0 o più ripetizioni
pattern = re.findall(r"Py*thon", "Pthon Python Pyython Pyyython")
print(f"* (0 o più): {pattern}")

# + - 1 o più ripetizioni
pattern = re.findall(r"Py+thon", "Pthon Python Pyython")
print(f"+ (1 o più): {pattern}")

# ? - 0 o 1 ripetizione (opzionale)
pattern = re.findall(r"colou?r", "color colour")
print(f"? (opzionale): {pattern}")

# {n} - Esattamente n ripetizioni
pattern = re.findall(r"\d{3}", "123 45 6789 12")
print(f"{{3}} (esattamente 3): {pattern}")

# {n,m} - Da n a m ripetizioni
pattern = re.findall(r"\d{2,4}", "1 12 123 1234 12345")
print(f"{{2,4}} (da 2 a 4): {pattern}")


# 4. Classi di caratteri

print("\n--- Classi di caratteri ---")

# [abc] - Uno qualsiasi dei caratteri a, b, c
pattern = re.findall(r"[aeiou]", "Python")
print(f"[aeiou] (vocali): {pattern}")

# [a-z] - Qualsiasi carattere da a a z
pattern = re.findall(r"[a-z]+", "Python 123 Test")
print(f"[a-z]+ (lettere minuscole): {pattern}")

# [^abc] - Qualsiasi carattere TRANNE a, b, c
pattern = re.findall(r"[^aeiou]", "Python")
print(f"[^aeiou] (non vocali): {pattern}")

# \d - Qualsiasi cifra (equivalente a [0-9])
pattern = re.findall(r"\d+", "Python 3.11 è uscito nel 2022")
print(f"\\d+ (cifre): {pattern}")

# \D - Qualsiasi NON cifra
pattern = re.findall(r"\D+", "Python3")
print(f"\\D+ (non cifre): {pattern}")

# \w - Qualsiasi carattere alfanumerico (lettere, cifre, underscore)
pattern = re.findall(r"\w+", "Python_3 è fantastico!")
print(f"\\w+ (alfanumerici): {pattern}")

# \W - Qualsiasi NON alfanumerico
pattern = re.findall(r"\W+", "Python 3!")
print(f"\\W+ (non alfanumerici): {pattern}")

# \s - Qualsiasi spazio bianco (spazio, tab, newline)
pattern = re.findall(r"\s+", "Python   è\tfantastico\n!")
print(f"\\s+ (spazi): {pattern}")

# \S - Qualsiasi NON spazio bianco
pattern = re.findall(r"\S+", "Python è fantastico")
print(f"\\S+ (non spazi): {pattern}")


# 5. Gruppi e cattura

print("\n--- Gruppi ---")

# Gruppi con parentesi ()
testo = "Nome: Mario, Cognome: Rossi"
match = re.search(r"Nome: (\w+), Cognome: (\w+)", testo)
if match:
    print(f"Nome completo: {match.group(0)}")  # Tutto il match
    print(f"Nome: {match.group(1)}")  # Primo gruppo
    print(f"Cognome: {match.group(2)}")  # Secondo gruppo

# Gruppi nominati
match = re.search(r"Nome: (?P<nome>\w+), Cognome: (?P<cognome>\w+)", testo)
if match:
    print(f"Nome (nominato): {match.group('nome')}")
    print(f"Cognome (nominato): {match.group('cognome')}")

# Gruppi non catturanti (?:...)
pattern = re.findall(r"(?:Mr|Mrs|Ms)\. (\w+)", "Mr. Smith, Mrs. Jones, Ms. Brown")
print(f"Gruppi non catturanti: {pattern}")


# 6. Lookahead e Lookbehind

print("\n--- Lookahead e Lookbehind ---")

# Positive lookahead (?=...)
# Trova "Python" solo se seguito da " 3"
pattern = re.findall(r"Python(?= 3)", "Python 3 è fantastico, Python 2 è vecchio")
print(f"Positive lookahead: {pattern}")

# Negative lookahead (?!...)
# Trova "Python" solo se NON seguito da " 2"
pattern = re.findall(r"Python(?! 2)", "Python 3 è fantastico, Python 2 è vecchio")
print(f"Negative lookahead: {pattern}")

# Positive lookbehind (?<=...)
# Trova numeri preceduti da "$"
pattern = re.findall(r"(?<=\$)\d+", "Prezzo: $100, Sconto: $20")
print(f"Positive lookbehind: {pattern}")

# Negative lookbehind (?<!...)
# Trova numeri NON preceduti da "$"
pattern = re.findall(r"(?<!\$)\d+", "Prezzo: $100, Quantità: 5")
print(f"Negative lookbehind: {pattern}")


# 7. Flag (modificatori)

print("\n--- Flag ---")

# re.IGNORECASE (re.I) - Ignora maiuscole/minuscole
pattern = re.findall(r"python", "Python PYTHON python", re.IGNORECASE)
print(f"IGNORECASE: {pattern}")

# re.MULTILINE (re.M) - ^ e $ matchano inizio/fine di ogni riga
testo_multiriga = "Python\nè\nfantastico"
pattern = re.findall(r"^.", testo_multiriga, re.MULTILINE)
print(f"MULTILINE: {pattern}")

# re.DOTALL (re.S) - . matcha anche newline
pattern = re.findall(r"Python.*fantastico", "Python\nè\nfantastico", re.DOTALL)
print(f"DOTALL: {pattern}")


# 8. Compilare espressioni regolari

print("\n--- Compilazione ---")

# Compilare un pattern per riutilizzarlo (più efficiente)
pattern_compilato = re.compile(r"\d+")
numeri1 = pattern_compilato.findall("Python 3.11")
numeri2 = pattern_compilato.findall("Versione 2.7")
print(f"Pattern compilato - risultato 1: {numeri1}")
print(f"Pattern compilato - risultato 2: {numeri2}")


# 9. Validazione email

print("\n--- Validazione Email ---")

def valida_email(email):
    """Valida un indirizzo email (versione semplificata)"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

emails = ["test@example.com", "invalid.email", "user@domain.co.uk", "@invalid.com"]
for email in emails:
    print(f"{email}: {'✓ Valida' if valida_email(email) else '✗ Non valida'}")


# 10. Validazione numero di telefono

print("\n--- Validazione Telefono ---")

def valida_telefono(telefono):
    """Valida un numero di telefono italiano"""
    # Formato: +39 123 4567890 o 123-4567890 o 1234567890
    pattern = r"^(\+39\s?)?(\d{3}[\s-]?)?\d{6,10}$"
    return re.match(pattern, telefono) is not None

telefoni = ["+39 123 4567890", "123-4567890", "1234567890", "12345"]
for tel in telefoni:
    print(f"{tel}: {'✓ Valido' if valida_telefono(tel) else '✗ Non valido'}")


# 11. Estrazione di URL

print("\n--- Estrazione URL ---")

testo = "Visita https://www.python.org e http://github.com per più info"
urls = re.findall(r"https?://[^\s]+", testo)
print(f"URL trovati: {urls}")


# 12. Estrazione di hashtag

print("\n--- Estrazione Hashtag ---")

tweet = "Amo #Python! È il miglior #linguaggio di #programmazione"
hashtags = re.findall(r"#\w+", tweet)
print(f"Hashtag: {hashtags}")


# 13. Sostituzioni avanzate con funzioni

print("\n--- Sostituzioni con funzioni ---")

def maiuscolo_match(match):
    """Converte il match in maiuscolo"""
    return match.group(0).upper()

testo = "python è fantastico"
risultato = re.sub(r"\b\w+\b", maiuscolo_match, testo)
print(f"Originale: {testo}")
print(f"Modificato: {risultato}")


# 14. Dividere stringhe con split()

print("\n--- Split con regex ---")

# Split su multipli delimitatori
testo = "Python,Java;C++;JavaScript|Ruby"
linguaggi = re.split(r"[,;|]+", testo)
print(f"Linguaggi: {linguaggi}")

# Split mantenendo i delimitatori
testo = "uno,due;tre"
parti = re.split(r"([,;])", testo)
print(f"Con delimitatori: {parti}")


# 15. Validazione password

print("\n--- Validazione Password ---")

def valida_password(password):
    """
    Valida una password:
    - Almeno 8 caratteri
    - Almeno una maiuscola
    - Almeno una minuscola
    - Almeno un numero
    - Almeno un carattere speciale
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

passwords = ["Password123!", "weak", "NoSpecial123", "NoNumber!", "short1!"]
for pwd in passwords:
    print(f"{pwd}: {'✓ Valida' if valida_password(pwd) else '✗ Non valida'}")


# 16. Estrazione di date

print("\n--- Estrazione Date ---")

testo = "Eventi: 15/03/2024, 01-12-2023, 2024-06-30"
# Formato: DD/MM/YYYY o DD-MM-YYYY o YYYY-MM-DD
date = re.findall(r"\d{2}[/-]\d{2}[/-]\d{4}|\d{4}-\d{2}-\d{2}", testo)
print(f"Date trovate: {date}")


# 17. Rimozione di tag HTML

print("\n--- Rimozione tag HTML ---")

html = "<p>Questo è un <b>testo</b> con <i>tag</i> HTML</p>"
testo_pulito = re.sub(r"<[^>]+>", "", html)
print(f"HTML: {html}")
print(f"Testo pulito: {testo_pulito}")


# 18. Validazione codice fiscale italiano

print("\n--- Validazione Codice Fiscale ---")

def valida_codice_fiscale(cf):
    """Valida un codice fiscale italiano (solo formato)"""
    pattern = r"^[A-Z]{6}\d{2}[A-Z]\d{2}[A-Z]\d{3}[A-Z]$"
    return re.match(pattern, cf.upper()) is not None

codici = ["RSSMRA80A01H501U", "INVALID123", "ABCDEF12G34H567I"]
for cf in codici:
    print(f"{cf}: {'✓ Valido' if valida_codice_fiscale(cf) else '✗ Non valido'}")


# 19. Estrazione di numeri da testo

print("\n--- Estrazione Numeri ---")

testo = "Ho 25 anni, peso 70.5 kg e sono alto 1.75 m"
# Numeri interi
interi = re.findall(r"\b\d+\b", testo)
print(f"Numeri interi: {interi}")

# Numeri decimali
decimali = re.findall(r"\d+\.?\d*", testo)
print(f"Numeri (anche decimali): {decimali}")


# 20. Esempio pratico: Parser di log

print("\n--- Parser di Log ---")

log_line = "2024-01-15 14:30:45 [ERROR] Database connection failed: timeout"

# Pattern per estrarre componenti del log
pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)"
match = re.match(pattern, log_line)

if match:
    data, ora, livello, messaggio = match.groups()
    print(f"Data: {data}")
    print(f"Ora: {ora}")
    print(f"Livello: {livello}")
    print(f"Messaggio: {messaggio}")


# 21. Best practices

print("\n--- Best Practices ---")
print("""
✅ Usa raw strings (r"...") per evitare problemi con backslash
✅ Compila pattern riutilizzati per migliori performance
✅ Usa gruppi nominati per codice più leggibile
✅ Testa le regex su https://regex101.com
✅ Commenta regex complesse

❌ Non usare regex per parsing HTML/XML (usa parser dedicati)
❌ Non esagerare con la complessità (meglio codice chiaro)
❌ Non dimenticare di escapare caratteri speciali
""")


# 22. Cheat sheet

print("\n--- Cheat Sheet ---")
print("""
Metacaratteri:
  .   Qualsiasi carattere
  ^   Inizio stringa
  $   Fine stringa
  *   0 o più ripetizioni
  +   1 o più ripetizioni
  ?   0 o 1 ripetizione
  {n} Esattamente n ripetizioni

Classi:
  \\d  Cifra [0-9]
  \\D  Non cifra
  \\w  Alfanumerico [a-zA-Z0-9_]
  \\W  Non alfanumerico
  \\s  Spazio bianco
  \\S  Non spazio bianco

Funzioni:
  re.search()   Cerca pattern
  re.match()    Cerca all'inizio
  re.findall()  Trova tutte le occorrenze
  re.sub()      Sostituisce
  re.split()    Divide stringa
""")
