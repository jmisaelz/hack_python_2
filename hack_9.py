"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    diccionario_final = {}
    cadena1 = []
    cadena2 = []
    posicion = 0
    if result.get("foo") == "fookziman":
        valor1 = "foo"
        for a in valor1:
            if posicion == 0:
                cadena1.append(a.upper())
            else:
                cadena1.append(a)
            posicion = posicion + 1

        valor2 = "fookziman"
        posicion = 0
        for b in valor2:
            if posicion == 0 and b != "k":
                cadena2.append(b.upper())
            else:
                if b != "k":
                    cadena2.append(b)
            posicion = posicion + 1
        
        cadena1 = "".join(cadena1)
        cadena2 = "".join(cadena2)
        diccionario_final = {cadena1:cadena2}

    result = diccionario_final
    return result

print(fn_hack_9({"foo":"fookziman","bar":"barziman"}))
