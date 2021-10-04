# Demo_RSA G-04 nhóm 3 create by Nguyễn Duy Hải - B19DCAT056

** Bản demo giải thuật RSA với 3 tính năng chính: tạo khóa, mã hóa và giải mã.

CreateKey.py   encode.py   decode.py

 *Tạo khóa RSA với độ dài bits
 
    p, q = myLibrary.getPrime(bits), myLibrary.getPrime(bits)
    n = p*q
    phi = (p-1)*(q-1)
    e = getE(phi)
    d = getD(e, phi)

    
PublicKey = (n, e)

PrivateKey = (n, d)

*Mã hóa RSA bằng PublicKey

    Data/data.txt ==> Data/encryption_data.txt
    
*Giải mã RSA bằng PrivateKey

    Data/encryption_data.txt ==> Data/decryption_data.txt
    

*** myLibrary chứa một số hàm phụ trợ
  * Kiểm tra tính nguyên tố BigInt
  * Sinh 1 số nguyên tố ngẫu nhiên
  * String to Integer (ascii)
  * Integer to String (base 64)
