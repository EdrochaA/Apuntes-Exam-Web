frase = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
HKCZJOI OKEJSZCNHE."""

#*******************Subprogramas****************
#Pasar de frase a diccionario de letras
def contar_apariciones_letras(frase):
    dic_letras = {}

    # Iterar a través de cada carácter en la frase
    for caracter in frase:
      
        # Verificar si el carácter es una letra
        if caracter.isalpha():
            # Si existe, incrementar su contador
            if caracter in dic_letras:
                dic_letras[caracter] += 1
            # Si no existe, agregarlo con un contador inicial de 1
            else:
                dic_letras[caracter] = 1

    return dic_letras

# Ordenar el diccionario de mayor a menor según los valores
def ordenar_apariciones_letra(dic_sin_ord):
    diccionario_ordenado = dict(sorted(dic_sin_ord.items(), key=lambda item: item[1], reverse= True))
    return diccionario_ordenado


#Sustitui el diccionario de claves en la frase 
def sustituir_letras(texto, diccionario):
    for clave, valor in diccionario.items():
        texto = texto.replace(clave, valor)
    return texto


#Creamos un diccionrio con todas las claves posibles
diccionario = {
    "A" : "d" ,
    "B" : "" ,
    "C" : "i" ,
    "D" : "p" ,
    "E" : "a" ,
    "F" : "x" ,
    "G" : "j" ,
    "H" : "t" ,
    "I" : "o" ,
    "J" : "n" ,
    "K" : "r" ,
    "L" : "z" ,
    "M" : "h" ,
    "N" : "s" ,
    "Ñ" : "" ,
    "O" : "f" ,
    "P" : "m" ,
    "Q" : "b" ,
    "R" : "c" ,
    "S" : "q" ,
    "T" : "l" ,
    "U" : "g" ,
    "V" : "y" ,
    "W" : "" ,
    "X" : "e" ,
    "Y" : "" ,
    "Z" : "u" 
}


x = contar_apariciones_letras(frase)
x = ordenar_apariciones_letra(x)
print(x)


texto_sustituido = sustituir_letras(frase, diccionario)
print(texto_sustituido)