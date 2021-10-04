import math
import myLibrary


def getE(phi):
    # tìm E t/m gcd(e,phi) = 1
    e = 65537  # một số nguyên tố Fermat 2^(2^4)+ 1
    while True:
        if math.gcd(e, phi) == 1:
            break
        e += 2
    return e


def getD(e, phi):
    d = myLibrary.GCD(e, phi)[0]  # tìm D t/m D*E = 1 mod phi
    if d < 0:
        d += phi
    return d


if __name__ == '__main__':
    bits = 2048
    # tạo 2 số nguyên tố ngẫu nhiên
    p, q = myLibrary.getPrime(bits), myLibrary.getPrime(bits)
    n = p*q
    phi = (p-1)*(q-1)
    e = getE(phi)
    d = getD(e, phi)

    with open('Data/publicKey.txt', "w") as f:
        print(n, file=f)
        print(e, file=f)

    with open('Data/privateKey.txt', "w") as f:
        print(n, file=f)
        print(d, file=f)

    print('Created RSA Key: ' + bits + 'bits')
