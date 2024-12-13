"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    lista_final = []
    if result[0] != 0:
        posicion = 0
        for valor in result:
            if(posicion + 1) % 2 == 0:
                lista_final.append(posicion+1)
            else:
                lista_final.append(str(posicion+1))
            posicion = posicion + 1
        result = lista_final    
    return result

print(fn_hack_7(["a","b","c","d","e"]))
print(fn_hack_7([0]))
