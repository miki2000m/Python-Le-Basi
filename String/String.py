# DICHIARAZIONE STRINGHE
# In Java: String x = "Ciao";  (solo doppi apici)
# In Python: si possono usare sia "..." che '...'
#es:
#x = ""
#y = ''
print("Adesso sto per dichiarare x e y:")
x="Ciao"
y='Ciao'

#i "..." e i '...' non ci permettono di mettere stringhe multi linea
#z= "Ciao
#   sono
#   Gianluca"

# STRINGHE MULTI-LINEA
# In Java: String x = "Ciao\n" + "     sono\n" + "     Gianluca";
#          oppure StringBuilder sb = new StringBuilder();
# In Python: si usano TRIPLICI apici (doppi o singoli) - molto più semplice!
#es:
#Lindentazione così la ho decisa io
print("\nAdesso sto per creare stringhe multi-linea:")
x="""Ciao
     sono
     Gianlucad"""
y='''Ciao
     sono
     Gianluca'''

print("x: "+x+"\n")
print("y: "+y)


# stampa di un singolo carattere di una stringa perché possiamo vedere le stringhe come "array" di caratteri
print("\nAdesso sto per stampare un singolo carattere di una stringa: "+x[0])# -> stampa C cioè il primo carattere della stringa x

#stampa la lunghezza di una stringa
print("\nAdesso sto per stampare la lunghezza della stringa x: "+str(len(x)))# -> stampa 28 cioè il numero di caratteri della stringa x