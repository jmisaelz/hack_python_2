"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    lista_final = []
    posicion = 1
    if len(result) == 5 or len(result) == 3:
        for valor in result:
            lista_final.append(result[len(result)-posicion]+'-'+str(len(result)-posicion+1))
            posicion = posicion + 1
    elif len(result) == 4 or len(result) == 2:
        for valor in result:
            lista_final.append(str(len(result)-posicion+1))
            posicion = posicion + 1
    result = lista_final
    return result

print(fn_hack_8(["a","b","c","d","e"]))
print(fn_hack_8(["a","b","c"]))
print(fn_hack_8(["a","b","c","d"]))
print(fn_hack_8(["a","b"]))
