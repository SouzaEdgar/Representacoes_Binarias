def formarBinario(real):
    inteiro = int(real)
    decimal = real - inteiro
    binario = ""
    newBIN = ""

    while decimal > 0.0:
        restante = decimal * 2.0
        if restante >= 1.0:
            binario += "1"
            decimal = restante - 1
        else:
            binario += "0"
            decimal = restante

    newBIN = binario
    binario = ""
    for z in range(0, 12):
        binario += newBIN[z]

    return (binario)

def aproxMaior(binario):
    newBIN = ""
    editado = [".",".",".",".",".",".",".",".",".",".",".",".","."]
    casa = len(binario) - 1
    original = 0
    
    for x in range(casa, 0, -1):
        if binario[x] == "1":
            editado.insert(x, binario[x].replace("1","0"))
        else:
            editado.insert(x, binario[x].replace("0","1"))
            original = x
            break
        
    editado = str(editado).replace(".","").replace("[","").replace("'"
    ,"").replace("]","").replace(",","").replace("","").replace(" ","")
    
    for y in range(0, original):
        newBIN += binario[y]
        
    return (newBIN+editado)

def formarExato(binario):
    bina = binario
    exato = 0.0

    for x in range(0, len(bina)):
        if bina[x] == "1":
            exato += 2 ** -(x+1)

    return exato

def formarErro(real,exato):
    numDECIMAL = real
    numEXATO = exato
    erro = float(str(((numDECIMAL - numEXATO) / numDECIMAL)*100).replace("-",""))

    return erro

##############################################################################################33
while True:

    real = float(input("\n\nDigite um valor entre 0 e 1: "))
    bits = 0

    if real > 0.0 and real < 1.0:
        binario = formarBinario(real)
        maior = ""
        newMENOR = ""

        for _ in range(0, len(binario)):
            maior += binario[_]
            newMENOR += binario[_]
            newMAIOR = aproxMaior(maior)

            bits += 1

            if bits >= 5:
                print(f"\nCom {_+1} bits")
                print(f"Aproximação a menor: {newMENOR} -> {formarExato(newMENOR)} "
                f"com erro = {formarErro(real,formarExato(newMENOR)):.2f}%")
                print(f"Aproximação a maior: {newMAIOR} -> {formarExato(newMAIOR)} "
                f"com erro = {formarErro(real,formarExato(newMAIOR)):.2f}%\n")
            if bits >= 12:
                break
    else:
        print("\nO número deve ser maior que 0 e menor que 1\n")
    
    repetir = input("Repetir? [S/N]: ").lower()
    if repetir[0] != "s":
        break
