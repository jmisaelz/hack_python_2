"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    lista_final = []
    posicion = 0
    if len(result) == 0:        
        lista_final.append("0")
    else:
        for valor in result:
            if(posicion + 1) % 2 == 0:
                lista_final.append("-")
            else:
                lista_final.append(str(posicion+1))
            posicion = posicion + 1

    result = lista_final        
    return result

print(fn_hack_6(["a","b","c","d","e"]))
print(fn_hack_6([]))
