lista_nazioni = ["Italia", "Francia", "Germania", "Spagna", "Regno Unito", "Olanda"]
lista_capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Londra", "Amsterdam"]
dom = input("Di che nazione vorresti sapere la capitale? ")
if dom in lista_nazioni:
    ris = lista_nazioni.index(dom)
    print("La capitale della nazione che hai scelto è:", (lista_capitali[ris]))
else:
    print("La nazione che hai scritto non è presente nella lista!")