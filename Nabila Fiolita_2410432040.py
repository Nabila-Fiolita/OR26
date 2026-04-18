import random

print("\n" + "="*30)     
print(f"{'SIMULASI DIMULAI':^30}")

n = int(input("Masukkan Jumlah Elemen: "))
if n < 2:
    print("Minimal 2 elemen untuk melakukan simulasi")
else:
    array = []
    while len(array) < n:
        elemen = int(random.random() * 50) + 1
        if elemen not in array:
            array.append(elemen)

    print("Baris Awal :", array)
    m = int(input("Masukkan Maksimal iterasi: "))
    
    history = [] # Memulai history kosong untuk pengecekan yang tepat
    iterasi = 1
    
    while iterasi <= m:
        # 1. Simpan kondisi SEBELUM perubahan ke dalam history
        history.append(list(array))
        
        hasil = list(array)
        
        # 2. Logika Perubahan (Tengah)
        for i in range(1, n - 1):
            if array[i] < array[i-1] and array[i] < array[i+1]:
                hasil[i] = array[i] + 2
            elif array[i] > array[i-1] and array[i] > array[i+1]:
                hasil[i] = array[i] - 2   
        
        # 3. Logika Perubahan (Ujung)
        if array[0] < array[1]:
            hasil[0] = array[0] + 2
        elif array[0] > array[1]:
            hasil[0] = array[0] - 2
            
        if array[n-1] < array[n-2]:
            hasil[n-1] = array[n-1] + 2
        elif array[n-1] > array[n-2]:
            hasil[n-1] = array[n-1] - 2

        print(f"Baris Iterasi {iterasi}\n", hasil)

        # 4. Pengecekan Kondisi Berhenti
        if hasil == array:
            print("Iterasi dihentikan karena kondisi sudah stabil")
            break
        elif hasil in history:
            print("Iterasi dihentikan karena siklus terdeteksi")
            break
        
        # Update array untuk iterasi berikutnya
        array = list(hasil)
        
        if iterasi == m:
            print("Simulasi dihentikan karena sudah mencapai batas iterasi")
        
        iterasi += 1

print("\n" + "="*30)     
print(f"{'SIMULASI SELESAI':^30}")
