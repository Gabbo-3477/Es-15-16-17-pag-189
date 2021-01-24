lista_nazioni = ["Giappone", "Stati Uniti", "Italia", "Belgio", "Olanda", "Svezia", "Finlandia", "Norvegia", "Germania"]
lista_capitali = ["Tokyo", "Washington", "Roma", "Bruxelles", "Amsterdam", "Stoccolma", "Helsinki", "Oslo", "Berlino"]
diz = {}
for i in range (len(lista_capitali)):
    diz[lista_capitali[i]] = lista_nazioni[i]
dom = input("Di che nazione vorresti sapere la capitale? ")
if dom in lista_capitali:
    print("La nazione della capitale che hai scelto è:", diz[dom])
else:
     print("La capitale che hai scritto non è presente nella lista!")