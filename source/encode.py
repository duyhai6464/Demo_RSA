import myLibrary


def get_data(file):
    with open(file, "r") as f:
        return f.read()


def convertStringToInt(P, base):
    R = []
    for i in P:
        c = str(ord(i))
        while len(c) != base:
            # 0000 ex for base = 4
            c = '0' + c
        R.append(c)
    return R


def createBigInt(R, size_n):
    A = []
    x = ""
    for i in R:
        # Tối ưu mã hóa nhiều kí tự nhất có thể
        if len(x) + len(i) >= size_n - 1:
            A.append(int(x))
            x = ""
        x += i
    A.append(int(x))
    return A


def encode(n, e, P, fileout):
    with open(fileout, "w") as f:
        C = ""
        R = convertStringToInt(P, 4)
        A = createBigInt(R, len(str(n)))
        for i in A:
            M = pow(i, e, n)
            M = myLibrary.toBase(M, 64)
            C += M + ' '
        print(C, file=f, end='')
    return C


if __name__ == '__main__':
    n, e = myLibrary.getKey("Data/PublicKey.txt")
    P = get_data("Data/data.txt")
    # data --> encryption_data
    C = encode(n, e, P, "Data/encryption_data.txt")
