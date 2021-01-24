lista_nazioni = ["Italia", "Francia", "Germania", "Spagna", "Regno Unito", "Olanda"]
lista_capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Londra", "Amsterdam"]
diz = {}
for i in range (len(lista_nazioni)):
    diz[lista_nazioni[i]] = lista_capitali[i]
dom = input("Di che nazione vorresti sapere la capitale? ")
if dom in lista_nazioni:
    print("La capitale della nazione che hai scelto è:", diz[dom])
else:
     print("La nazione che hai scritto non è presente nella lista!")