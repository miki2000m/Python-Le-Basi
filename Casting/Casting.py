# trasformare una variabile in una altro tipo di variabile

#x = String
x="5"

#y = int
y=5

#obbiettivo --------------------
#print(x+y) = vogliamo che restituisca un valore intero cosa che se noi scriviamo direttamente il print così ci dà errore
#perché ci sono 2 tipi di variabili che non possono essere sommate tra loro

#Output to try:
#errore che ci viene fuori con print(x+y) = TypeError: can only concatenate str (not "int") to str (y non è un intero quindi non può essere sommato con x)
#errore che ci viene fuori con print(y+x) = TypeError: unsupported operand type(s) for +: 'int' and 'str' (x non è una stringa quindi non piò essere concatenata)


#Come risolvere???:
#facendo il casting
#formula generica: nome = tipo(valore)

#per concatenare e rendere entrambi i valori STRING
#castring to string
y=str(5)

#Output -> 55
#Perché CONCATENA cioè: unisce i 2 valori delle stringhe.
#NON LI SOMMA perché sono 2 valori String cioè testo non lì prende come valori numerici
print("x+y con casting di y in String: "+x+y)


#N.B. {all'interno delle parentesi tonde bisogna assolutamente mettere un valore numerico se vogliamo passare da String a int}
#per far si che in Output abbiamo la somma dobbiamo rendere x un valore int
#castring to int
x=int("5")

#Devo fare il recasting di y perché adesso è una Sting
y=int("5")

#Output -> 10
#Perché in questo caso fa la somma come volevamo
print("\nx+y con casting di x in int: ")
print(x+y)



#STESSI PASSAGGI PER IL FLOAT
#fomula: nome=float("x")
