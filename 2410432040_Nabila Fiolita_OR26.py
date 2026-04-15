import random
print("\n"+"="*30)     
print(f"{'SIMULASI DIMULAI':^30}")
n= int(input("Masukkan Jumlah Elemen:"))
array=[]
while len(array) < n:
    elemen=int(random.random()*50)+1
    if elemen not in array:
         array.append(elemen)
history=[list(array)]
print("Baris Awal :", array)
m=int(input("Masukkan Maksimal iterasi:"))
iter=1
while iter<m+1:
       if n>1:
          hasil=list(array)
          for i in range (1,n-1):
               if array [i]<array[i-1] and array[i]<array[i+1] :
                    hasil[i]= array[i]+2
               elif array [i]>array[i-1] and array [i]>array[i+1] :
                    hasil[i]=array[i]-2   
          if array[0]<array [1]:
               hasil[0]=array[0]+2
          elif array[0]>array [1]:
               hasil[0]=array[0]-2
          if array[n-1]<array [n-2]:
               hasil[n-1]=array[n-1]+2
          elif array[n-1]>array [n-2]:
               hasil[n-1]=array[n-1]-2
          history.append(list(array))
          print(f"Baris Iterasi {iter}\n",hasil)
          if hasil==array:
               print("Iterasi dihentikan karena kondisi sudah stabil")   
               break                
          elif hasil in history:
               print("Iterasi dihentikan karena siklus terdeteksi")
               break
          elif iter>=m:
               print("Simulasi dihentikan karena sudah mencapai batas iterasi")
          array=list(hasil)
          iter+=1 
       else:
            print("Minimal 2 elemen untuk melakukan simulasi")
print("\n"+"="*30)     
print(f"{'SIMULASI SELESAI':^30}")


