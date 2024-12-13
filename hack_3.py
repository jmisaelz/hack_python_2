"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX"
"""


def fn_hack_3(s):
    result = s
    vowels = ["a","e","i","o","u"]
    texto_final = []
    posicion = 0
    for valor in result:
        if (posicion == 0 or posicion == len(result)-1) and valor not in vowels:
            letra = valor.upper()
            texto_final.append(letra)
        else:
            if valor == "a":
                letra = "@"

            elif valor == "e":
                letra = "3"

            elif valor == "i":
                letra = "¡"

            elif valor == "o":
                letra = "0"

            elif valor == "u":
                letra = "v"
                
            else:
                letra = valor

            texto_final.append(letra)
        posicion = posicion + 1

    result = "".join(texto_final)
        
    return result

print(fn_hack_3("fooziman"))
print(fn_hack_3("barziman"))
print(fn_hack_3("3q"))
print(fn_hack_3("qu"))
print(fn_hack_3("qux"))
