def Primo(dado):
    i=1
    contador=0
    while i<dado:
        if dado % i == 0:
            contador+=1
            i+=1
    if contador>2:
        string = "Não é primo!"
        return string
    else:
        string2 = "É primo!"
        return string2