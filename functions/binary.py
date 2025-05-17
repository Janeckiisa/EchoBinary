def numeroParaBinario(numero):
    binario = []

    if numero == 0:
        return '0'

    while numero != 0:
        quociente = numero // 2
        resto = numero % 2

        binario.insert(0, resto)
        numero = quociente

    count = len(binario)

    while count < 8:
        binario.insert(0, 0)
        count += 1

    return ''.join(str(bit) for bit in binario)

def binarioParaNumero(binario):
    temp = []
    result = 0
    i = 0

    for bit in binario:
        temp.insert(0, bit)

    for item in temp:
        calculo = int(item) * (2 ** i)
        result += calculo
        i += 1

    return result
