"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    texto_final = []
    posicion = 0
    for valor in result:
        if (posicion != 0 and posicion != len(result)-1) or len(result) == 3:    
            texto_final.append(valor)
        posicion = posicion + 1

    result = "".join(texto_final)
    return result

print(fn_hack_4("fooziman"))
print(fn_hack_4("barziman"))
print(fn_hack_4("qux"))
