import myLibrary


def get_encryption_data(file):  # file encryption txt
    with open(file, 'r') as f:
        C = f.readline().split()
    return C


def decode(n, d, C, base, fileOut):  # file PlanintextDecode
    with open(fileOut, 'w') as f:
        P = ''
        for i in C:
            m = int(i)
            m = pow(m, d, n)
            c = str(m)
            while len(c) % base != 0:
                c = '0' + c
            x = 0
            while x != len(c):
                a = c[x:x+base]
                x += base
                P += chr(int(a))
        print(P, file=f, end='')
    return P


if __name__ == '__main__':
    n, d = myLibrary.getKey('Data/privateKey.txt')
    C = get_encryption_data('Data/encryption_data.txt')
    # encryption_data.txt --> decryption_data.txt
    P = decode(n, d, C, 5, 'Data/decryption_data.txt')
    print('encryption_data.txt ==> decryption_data.txt')
