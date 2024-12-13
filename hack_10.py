"""
text: [{"a":"b"},{"c":"d"},{"e":"f"}] output => [{"1":"2"},{"3":"4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    lista_final = []
    contador = 1
    for valor in result:
        lista_final.append({str(contador):str(contador + 1)})
        contador = contador + 2         

    result = lista_final
    return result

print(fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}]))
