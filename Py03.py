#19.11.2026 Roland Arro

#Ülesanne 3.7 Python Turtle kolmnurk

import turtle

kylg =100
nurk = 120
varv = "red"

turtle.color(varv)
for i in range(3):
    turtle.fd(kylg)
    turtle.lt(nurk)
turtle.done()




#Ülesanne 3.3 Reisiplaan
sihtkoht = "Haapsalu"
paevade_arv = 10
oobimise_hind = 15.6
print(sihtkoht ,"reis kestab",paevade_arv," päeva ja üks öö maksab",oobimise_hind," eurot.")


#Ülesanne 3.2 Ostunimekiri
toode = "šampoon"
kogus = 5
hind = 5.65
print("Soovin " + toode + " " + str (kogus) +", mille tüki hind on "+str(hind)+" eurot.")


#Ülesanne 3.1 Tervitus
nimi = "Roland"
vanus = 16
keskmine_hinne = 5.0
print(nimi,vanus,keskmine_hinne)
