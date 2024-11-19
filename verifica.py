#esercizio 1
voto1= float(input("inserisci primo voto "))
voto2= float(input("inserisci secondo voto "))
voto3= float(input("inserisci terzo voto "))

somma = (voto1 + voto2 + voto3)
scelta= int(input("inserisci 1 se vuoi la media in centesimi o 2 se la vuoi in trentesimi"))
media = (somma/3) 
if(scelta==1):
    print("questa è la media ", media)
elif(scelta==2):
    mediatrenta = (media*100)/30
    print("questa è la media in trentesimi ", mediatrenta)



#esercizio 2
media= float(input("inserisci la media della pagella "))
anno=int(input("inserisci anno scolastico "))

if (anno==3):
    if(media ==6 ):
        print("i crediti vanno da 7 a 8")
    elif(media>6 and media<=7):
        print("i crediti vanno da 8 a 9")
    elif(media>7 and media<=8):
        print("i crediti vanno da 9 a 10")
    elif(media>8 and media<=9):
        print("i crediti vanno da 10 a 11")
    elif(media>9 and media<=10):
        print("i crediti vanno da 11 a 12")
    else:
        print("voto non valido")
elif (anno==4):
    if(media ==6 ):
        print("i crediti vanno da 8 a 9")
    elif(media>6 and media<=7):
        print("i crediti vanno da 9 a 10")
    elif(media>7 and media<=8):
        print("i crediti vanno da 10 a 11")
    elif(media>8 and media<=9):
        print("i crediti vanno da 11 a 12")
    elif(media>9 and media<=10):
        print("i crediti vanno da 12 a 13")
    else:
        print("voto non valido")
elif (anno==5):
    if(media ==6 ):
        print("i crediti vanno da 9 a 10")
    elif(media>6 and media<=7):
        print("i crediti vanno da 10 a 11")
    elif(media>7 and media<=8):
        print("i crediti vanno da 11 a 12")
    elif(media>8 and media<=9):
        print("i crediti vanno da 12 a 13")
    elif(media>9 and media<=10):
        print("i crediti vanno da 13 a 14")
    else:
        print("voto non valido")
else:
        print("anno non valido")
    


#esercizio 3
somma=0
i=0
lancio1=int(input("inserisci valore del lancio"))
lancio2=int(input("inserisci valore del lancio"))
lancio3=int(input("inserisci valore del lancio"))
lancio4=int(input("inserisci valore del lancio"))
lancio5=int(input("inserisci valore del lancio"))
if(lancio1>0):
    somma =somma+ lancio1
    i = i+1
else:
    print("lancio1 nullo riprova")

if(lancio2>0):
    somma =somma+ lancio2
    i = i+1
else:
    print("lancio2 nullo riprova")

if(lancio3>0):
    somma =somma+ lancio3
    i = i+1
else:
    print("lancio3 nullo riprova")

if(lancio4>0):
    somma =somma+ lancio4
    i = i+1
else:
    print("lancio4 nullo riprova")

if(lancio5>0):
    somma =somma + lancio5
    i = i+1
else:
    print("lancio5 nullo riprova")


media = somma/i
print("la media lunghezza è",media)