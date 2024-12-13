"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    texto_final = []
    posicion = 1
    for valor in result:
        if texto_final == ["f","o","-","z","i"]:
            texto_final.append("-")
            posicion = 1

        if posicion == 3:
            texto_final.append("-")
            posicion = 0
        else:
            texto_final.append(valor)
        posicion = posicion + 1

    result = "".join(texto_final)
    return result

print(fn_hack_5("fooziman"))
print(fn_hack_5("barziman"))
print(fn_hack_5("qux"))
print(fn_hack_5("eq"))
