def birinchi_harf_katta(qolgan_kichik(satrlar)):
    yangi_satrlar = []
    for satr in satrlar:
        birinchi_harf = satr[0].upper()
        qolgan = satr[1:].lower()
        yangi_satr = birinchi_harf + qolgan
        yangi_satrlar.append(yangi_satr)
    return yangi_satrlar

satrlar = ["ASSALOMU", "aleykum", "DUNYO", "JAHONIMIZ"]
print(birinchi_harf_katta(qolgan_kichik(satrlar)))
