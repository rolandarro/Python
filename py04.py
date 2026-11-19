# 19.11.2026 Roland Arro

# Ringi pindala ja turtle
#Kirjuta programm, mis kasutab Turtle graafikat joonistamaks ringi ning arvutab ja kuvab konsoolis ringi pindala ja ümbermõõdu.
import turtle
try:
    r = int(input("Sisesta raadius: "))
    s = 3.14  * r ** 2
    p = 2 * 3.14 * r
    turtle.circle(r)
    print(s, p)
    turtle.done()
except ValueError:
    print("urror")




# Faili allalaadimine
# Kirjuta programm, mis aitab arvutada, mis on allalaadimis kiirus

try:

    kiirus = int(input("Sisesta kiirus MB/s: "))
    suurus = int(input("Sisesta suurus MB: "))
    if kiirus == 0:
        print("Nulliga ei saa jagada")
    else:
            vastus = suurus / kiirus
    
    print(int(vastus))
except ValueError:
    print ("Mingi jama")




# Aia pikkus
# Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
x = int(input("sisesta külg 1: "))
y = int(input("sisesta külg 2: "))
pikkus = (x + y) * 2

print(f"Aia kogupikkus on {pikkus} meetrit.")