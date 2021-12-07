traductor = {
    "love": ["amor", "cariño"],
    "house": ["casa", "refugio", "hogar"],
    "thing": "cosa",
    "moon": "luna"}

x = input("Ingrese palabra en Inglés: ")

for i in traductor:
    if i == x:
        print(i+":",traductor[i])
        