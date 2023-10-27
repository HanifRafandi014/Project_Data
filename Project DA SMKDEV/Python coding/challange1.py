def checkCats(catsTuti, catsNining):
    # Salin array milik Tuti dan hapus usia kucing dari array yang disalin
    salinanCatsTuti = catsTuti.copy()
    del salinanCatsTuti[0]  # Hapus Kucing Pertama
    del salinanCatsTuti[-2:]  # Hapus dua Kucing Terakhir

    # Gabungkan data Tuti yang sudah dikoreksi dengan data Nining
    semuaCats = salinanCatsTuti + catsNining

    # Loop melalui semua kucing
    for i, usia in enumerate(semuaCats, start=1):
        if usia >= 3:
            print(f"Kucing Nomor {i} adalah Kucing Dewasa, dan berusia {usia} tahun.")
        else:
            print(f"Kucing Nomor {i} masih anak-anak.")

# Data uji 1
dataTuti1 = [3, 5, 2, 12, 7]
dataNining1 = [4, 1, 15, 8, 3]
checkCats(dataTuti1, dataNining1)

# Data uji 2
dataTuti2 = [9, 16, 6, 8, 3]
dataNining2 = [10, 5, 6, 1, 4]
checkCats(dataTuti2, dataNining2)
