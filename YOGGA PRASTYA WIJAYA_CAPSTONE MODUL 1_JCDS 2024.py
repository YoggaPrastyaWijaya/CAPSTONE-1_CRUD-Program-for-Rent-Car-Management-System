from tabulate import tabulate

#################################################
#       CAPSTONE MODULE 1 - CRUD APPLICATION    #
#             YOGGA PRASTYA WIJAYA              #
#            JCDS PURWADHIKA JAKARTA            #
#################################################

### DATABASE ### 
#Plat - Plat nomor mobil rental (datatype: string) max 9 char
#Jenis - Jenis mobil rental (datatype: string) max 30 char
#Tahun - Tahun produksi mobil rental (datatype: integer) 2000 - 2024
#Warna - Warna mobil rental (datatype: string) max 30 char
#Mesin - Jenis mesin mobil rental (datatype: string) max 30 char

daftarmobil =[{"plat" : "B3661UJO", "jenis" : "Toyota Fortuner", "tahun" : 2020, "warna" : "Hitam", "mesin" : "Diesel"},
                {"plat" : "B4023BJK", "jenis" : "Mitsubishi Pajero", "tahun" : 2015, "warna" : "Silver", "mesin" : "Diesel"},
                {"plat" : "A9204NJR", "jenis" : "Toyota Avanza", "tahun" : 2022, "warna" : "Hitam", "mesin" : "Bensin"},
                {"plat" : "A9092EAR", "jenis" : "Honda Brio", "tahun" : 2023, "warna" : "Silver", "mesin" : "Bensin"},
                {"plat" : "DK5823GAJ", "jenis" : "Toyota Fortuner", "tahun" : 2022, "warna" : "Silver", "mesin" : "Diesel"},
                {"plat" : "A9092EAR", "jenis" : "Honda Brio", "tahun" : 2022, "warna" : "Merah", "mesin" : "Bensin"},
                {"plat" : "B2840SJ", "jenis" : "Daihatsu Xenia", "tahun" : 2021, "warna" : "Silver", "mesin" : "Bensin"},
                {"plat" : "B920RO", "jenis" : "Daihatsu Xenia", "tahun" : 2022, "warna" : "Hitam", "mesin" : "Bensin"},
                {"plat" : "DK379UCO", "jenis" : "Honda Brio", "tahun" : 2023, "warna" : "Merah", "mesin" : "Bensin"},
                ]
################################################ 

### MENCETAK DAFTAR MOBIL ###
def datamobil():
    print("### DAFTAR MOBIL ###")
    empty_list  = []
    for i in daftarmobil:
        empty_list.append(i.values())
    print(tabulate(empty_list,["Plat","Jenis","Tahun","Warna","Mesin"],tablefmt="pretty"))

### CETAK DAFTAR MOBIL DENGAN INDEX (Untuk edit dan hapus)### 
def datamobil_withindex():
    print("### DAFTAR MOBIL ###")
    empty_list  = []
    for i in range(len(daftarmobil)):
        empty_list_2 = list(daftarmobil[i].values())
        empty_list_2.insert(0,i)
        empty_list.append(empty_list_2)
    print(tabulate(empty_list,["Index","Plat","Jenis","Tahun","Warna","Mesin"],tablefmt="pretty"))

### !!!! SPECIAL MENU 1- SORT TAHUN MOBIL !!!! ###
def sort(x,y): #Default - Ascending
    empty_list =[] #placeholder data olahan
    sort_daftarmobil = daftarmobil.copy() #copy data dari database utama agar tidak merubah database utama ketika sorting
    #x adalah key dari dictionary yang ingin disort (plat, jenis, tahun, warna, dan mesin)
    #y adalah asc atau desc
    for j in range(len(sort_daftarmobil)-1): #melakukan algoritma bubble sort
        for index in range(0,len(sort_daftarmobil)-j-1): 
            if sort_daftarmobil[index][x] > sort_daftarmobil[index+1][x]: #swap
                sort_daftarmobil[index],sort_daftarmobil[index+1] = sort_daftarmobil[index+1],sort_daftarmobil[index]
            else: #no swap
                continue
    for i in sort_daftarmobil: #memindahkan hasil sort ke placeholder data olahan untuk ditampilkan
        empty_list.append(i.values())
    if y == "desc": #descending sort
        empty_list.reverse()
    print("### DAFTAR MOBIL ###")
    print(tabulate(empty_list,["Plat","Jenis","Tahun","Warna","Mesin"],tablefmt="pretty"))

### !!!! SPECIAL MENU 1- FILTER GANJIL GENAP !!!! ###
def ganjil_genap(x):
    result = "" #placeholder plat
    genap = [] #placeholder genap
    ganjil =[] #placeholder ganjil
    for i in daftarmobil: #melakukan iterasi untuk mengecek tiap angka pada plat di database 
        for j in i["plat"]:
            if j.isnumeric():
                result += j
        if int(result) % 2 == 0:
            genap.append(i.values())
        else:
            ganjil.append(i.values())
    #x adalah pilihan tampilan genap atau ganjil
    if x == "genap":
        print("### DAFTAR MOBIL PLAT GENAP ###")
        print(tabulate(genap,["Plat","Jenis","Tahun","Warna","Mesin"],tablefmt="pretty"))
    if x == "ganjil":
        print("### DAFTAR MOBIL PLAT GANJIL ###")
        print(tabulate(ganjil,["Plat","Jenis","Tahun","Warna","Mesin"],tablefmt="pretty"))

### MENU 2 - Plat Input ###
def menu2_input_plat():
    m2_1_plat_input = input("Silahkan masukkan plat nomor: ").upper()
    if " " not in m2_1_plat_input and m2_1_plat_input.isalnum() and len(m2_1_plat_input) <= 9: #Memastikan jika plat nomor yang ditambahkan tidak mengandung spasi, karakter special, dan maksimal 9 karakter
        return m2_1_plat_input
    else:
        print("***Mohon masukkan plat TANPA spasi dan karakter special (Maskimal 9 karakter)!, silahkan coba kembali***")
        return menu2_input_plat()
    
### MENU 2 - Input Tahun ### 
def menu2_input_tahun():
    m2_1_tahun_input = input("Silahkan masukkan tahun produksi mobil: ") 
    if m2_1_tahun_input.isdecimal():#memastikan jika tahun yang dimasukan user berupa data angka dan ada dikisaran tahun 2000 - 2024
        integer_input = int(m2_1_tahun_input)
        if integer_input >= 2000 and integer_input <= 2024:
            return int(integer_input)
        else:
            print("*** Mobil tidak sesuai dengan standar, silahkan masukkan tahun mobil yang sesuai (2000 - 2024)! ***")
            return menu2_input_tahun()
    else:
        print("***Mohon masukkan angka!***")
        return menu2_input_tahun()

### MENU 2 - Save Data Options ###
def save_data_options():
    m2_1_save_input = input("Menyimpan data ini? (Y/N): ").upper()
    if m2_1_save_input == "Y" or m2_1_save_input == "N": #memastikan pilihan user jika yakin untuk menyimpan data yang baru ditambahkan
        return m2_1_save_input
    else:
        print("*** Mohon masukan kode menu yang tepat, silahkan masukan kembali *** ")
        return save_data_options()

### MENU 3 - Confirmation Edit ###
def menu3_confirmation_edit():
    m3_1_confirmation_input = input("Mengedit data ini? (Y/N): ").upper()
    if m3_1_confirmation_input == "Y" or m3_1_confirmation_input == "N": #memastikan pilihan user jika yakin untuk menyimpan data yang baru diedit
        return m3_1_confirmation_input
    else:
        print("*** Mohon masukan kode menu yang tepat, silahkan masukan kembali *** ")
        return menu3_confirmation_edit()

### MENU 3 - Plat Input ###
def menu3_plat_input():
    global daftarmobil
    m3_1_plat_input = input("Silahkan masukkan plat mobil: ").upper()
    if " " not in m3_1_plat_input and m3_1_plat_input.isalnum() and len(m3_1_plat_input) <= 9: #Memastikan jika plat nomor yang ditambahkan tidak mengandung spasi, karakter special, dan maksimal 9 karakter
        filter_value = []
        for i in daftarmobil:
            filter_value.append(i['plat']) ##Mengubah semua value menjadi list
        if m3_1_plat_input in filter_value:
            print("***Plat nomor ini sudah ada didatabase! Silahkan dicoba kembali*** ")
            return menu3_plat_input()
        else:
            return m3_1_plat_input
    else:
        print("***Mohon masukkan plat TANPA spasi dan karakter special (Maskimal 9 karakter)!, silahkan coba kembali***")
        return menu3_plat_input()
 
### MENU 4 - Confirmation Delete ###
def menu4_confirmation_delete():
    m3_1_confirmation_input = input("Menghapus data ini? (Y/N): ").upper()
    if m3_1_confirmation_input == "Y" or m3_1_confirmation_input == "N": #memastikan pilihan user jika yakin untuk menyimpan data yang baru dihapus
        return m3_1_confirmation_input
    else:
        print("*** Mohon masukan kode menu yang tepat, silahkan masukan kembali *** ")
        return menu3_confirmation_edit()

################################################ 

### MENU 1 ### - Tampilkan daftar mobil rental
def menu1():
    m1_input = input('''
    ### SELAMAT DATANG DI RENTAL SULTAN ###
    1. Tampilkan semua daftar mobil
    2. Tampilkan mobil berdasarkan plat mobil
    3. Urutkan daftar mobil
    4. Tampilkan mobil plat ganjil
    5. Tampilkan mobil plat genap
    6. Kembali ke Main Menu
    Silahkan untuk pilih menu yang dituju: ''')
    if (m1_input == "1"): ## Menampilkan semua daftar mobil
        if daftarmobil: #Jika ada data, tampilkan semua daftar mobil
            datamobil()
            menu1()
        else: #jika tidak ada data, munculkan peringatan dan kembali ke menu 1
            print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
            menu1()
    elif (m1_input == "2"): ## Menampilkan mobil berdasarkan plat mobil
        if daftarmobil: # Jika ada data mobil pada sistem, maka tampilkan menu user input memasukkan plat mobil
            plat_input = input('silahkan untuk tulis plat mobil yang dicari:').upper()
            empty_list = []
            for i in daftarmobil:
                if plat_input in i.values(): 
                    empty_list.append(i.values())
                else:
                    continue
            if empty_list:
                print(tabulate(empty_list,["Plat","Jenis","Tahun","Warna","Mesin"],tablefmt="pretty"))
                menu1()
            else: # Jika plat nomor yang di input user tidak ada di sistem, maka tampilkan peringatan
                print("***Data tidak ditemukan, silahkan coba kembali***")
                menu1()
        else: # Jika di sistem tidak berisi data apapun, berikan peringatan
            print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
            menu1()
    elif (m1_input == "3"): ## Menu Sort
        while True:
            sort_input = input('''
    Mengurutkan mobil berdasarkan:
    1. Jenis mobil (ascending)
    2. Jenis mobil (descending)
    3. Tahun produksi (ascending)
    4. Tahun produksi (descending)
    5. Warna mobil (ascending)
    6. Warna mobil (descending)
    7. Mesin mobil (ascending)
    8. Mesin mobil (descending)
    9. Kembali ke Menu 1
    Silahkan untuk pilih menu yang dituju: ''')   
            if sort_input == "1": #Jenis mobil (ascending)
                if daftarmobil:
                    sort("jenis","asc")
                    continue
                else:
                    print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
                    continue
            elif sort_input == "2": #Jenis mobil (descending)
                if daftarmobil:
                    sort("jenis","desc")
                    continue
                else:
                    print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
                    continue
            elif sort_input == "3": #Tahun produksi (ascending)
                if daftarmobil:
                    sort("tahun","asc")
                    continue
                else:
                    print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
                    continue
            elif sort_input == "4": #Tahun produksi (descending)
                if daftarmobil:
                    sort("tahun","desc")
                    continue
                else:
                    print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
                    continue
            elif sort_input == "5": #Warna mobil (ascending)
                if daftarmobil:
                    sort("warna","asc")
                    continue
                else:
                    print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
                    continue
            elif sort_input == "6": #Warna mobil (descending)
                if daftarmobil:
                    sort("warna","desc")
                    continue
                else:
                    print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
                    continue
            elif sort_input == "7": #Mesin mobil (ascending)
                if daftarmobil:
                    sort("mesin","asc")
                    continue
                else:
                    print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
                    continue
            elif sort_input == "8": #Mesin mobil (descending)
                if daftarmobil:
                    sort("mesin","desc")
                    continue
                else:
                    print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
                    continue
            elif sort_input == "9": #Kembali ke Menu 1
                break
            else: #User input tidak sesuai, berikan peringatan
                print("*** Mohon masukan kode menu yang tepat, silahkan masukan kembali *** ")
                continue
        menu1() #Setelah memilih, kembali ke menu 1
    elif (m1_input == "4"): ## Menampilkan mobil plat ganjil  
        if daftarmobil:
            ganjil_genap("ganjil")
            menu1()        
        else:
            print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
            menu1()
    elif (m1_input == "5"): ## Menampilkan mobil plat genap  
        if daftarmobil:
            ganjil_genap("genap")
            menu1()
        else:
            print("*** Data tidak tersedia di sitem! mohon untuk tambahkan***")
            menu1()
    elif (m1_input == "6"): ## Kembali ke Main Menu
        mainmenu()
    else: ## WARNING - Kode input tidak sesuai
        print("*** Mohon masukan kode menu yang tepat, silahkan masukan kembali *** ")
        menu1()
    
### MENU 2 ### - #Menambah mobil rental
def menu2():
    global daftarmobil
    m2_input = input('''
    ### SELAMAT DATANG DI RENTAL SULTAN ###
    1. Menambahkan data mobil baru
    2. Kembali ke Main Menu
    Silahkan untuk pilih menu yang dituju: ''')
    if (m2_input == "1"): #Menambahkan data mobil baru berdasarkan user input
        while True:
            plat = menu2_input_plat() #User memasukan plat mobil baru dan kemudian diperiksa menghindari data duplikat
            dict_value = [] 
            for i in daftarmobil: # Mengubah dictionary menjadi list berisi semua plat mobil yang ada di data
                dict_value.append(i['plat'])
            if plat in dict_value:
                print("***Plat nomor ini sudah ada didatabase!***")
                break
            else: # Jika plat nomor yang diinput tidak duplikat, lanjutkan memasuki data jenis mobil, tahun produksi, warna mobil, dan jenis mesin
                while True:
                    m2_1_jenismobil_input = input("Silahkan masukkan Jenis mobil: ").title()
                    if len(m2_1_jenismobil_input) <= 30:
                        break
                    else:
                        print("***Mohon masukkan nama mobil maksimal 30 karakter***")
                        continue
                tahun = menu2_input_tahun()
                while True:
                    m2_1_warna_input = input("Silahkan masukkan warna mobil: ").title()
                    if len(m2_1_warna_input) <= 30:
                        break
                    else:
                        print("***Mohon masukkan warna mobil maksimal 30 karakter***")
                        continue
                while True:
                    m2_1_mesin_input = input("Silahkan masukkan jenis mesin: ").title()
                    if len(m2_1_mesin_input) <= 30:
                        break
                    else:
                        print("***Mohon masukkan jenis mesin maksimal 30 karakter***")
                        continue
            empty_list = [[plat, m2_1_jenismobil_input, tahun, m2_1_warna_input, m2_1_mesin_input]]
            print("### Data Tambahan Mobil ###")
            print(tabulate(empty_list,["Plat","Jenis","Tahun","Warna","Mesin"],tablefmt="pretty"))
            result = save_data_options() # Meminta konfirmasi user untuk menyimpan data yang telah di input
            if (result == "Y"): # Jika Y, menyimpan data ke database
                daftarmobil.append({"plat" : plat, "jenis" : m2_1_jenismobil_input, "tahun" : tahun, "warna" : m2_1_warna_input, "mesin" : m2_1_mesin_input})
                print("***Data berhasil ditambahkan!***")
                break
            if (result == "N"): # Jika N, kembali ke menu 2
                break
        menu2()
    elif (m2_input == "2"): # Kembali ke main menu
        mainmenu()
    else:## WARNING - Kode input tidak sesuai
        print("*** Mohon masukan kode menu yang tepat, silahkan masukan kembali *** ")
        menu2()

### MENU 3 ###  - Mengubah data mobil rental
def menu3():
    global daftarmobil
    m3_input = input('''
    ### SELAMAT DATANG DI RENTAL SULTAN ###
    1. Mengubah data mobil
    2. Kembali ke Main Menu
    Silahkan untuk pilih menu yang dituju: ''')
    if (m3_input == "1"): ##Mengubah data mobil berdasarkan index dan kolom yang ingin dipilih oleh user
        datamobil_withindex()
        m3_1_index_input = input("Silahkan masukkan nomor index yang ingin di edit: ")  #User memasukan index yang ingin diedit
        if m3_1_index_input.isdecimal():#Jika user memasukan index berupa angka, lanjutkan proses
            if int(m3_1_index_input) <= len(daftarmobil)-1 and int(m3_1_index_input) >= 0:
                index = int(m3_1_index_input)
                print(tabulate([daftarmobil[index].values()],["Plat","Jenis","Tahun","Warna","Mesin"],tablefmt="pretty")) #Menampilkan kolom index dan meminta konfirmasi user
                result = menu3_confirmation_edit()
                if result == "Y":   
                    while True:
                        m3_edit_input = input("Kolom data apa yang ingin diedit?").lower()
                        if m3_edit_input == "plat": #Mengubah kolom plat
                            m3_1_plat_input = str(menu3_plat_input())
                            result = save_data_options()
                            if result == "Y":
                                daftarmobil[index]["plat"] =  m3_1_plat_input
                                print("Data Berhasil Diedit!")
                                break
                            else:
                                break
                        elif m3_edit_input == "jenis": #Mengubah kolom jenis
                            while True:
                                m3_1_mobil_input = input("Silahkan masukkan jenis mobil:")
                                if len(m3_1_mobil_input) <= 30:
                                    break
                                else:
                                    print("***Mohon masukkan jenis mobil maksimal 30 karakter***")
                                    continue
                            result = save_data_options()
                            if result == "Y":
                                daftarmobil[index]["jenis"] = m3_1_mobil_input
                                print("Data Berhasil Diedit!")
                                break
                            else:
                                break
                        elif m3_edit_input == "tahun": #Mengubah kolom tahun
                            tahun = menu2_input_tahun()
                            result = save_data_options()
                            if result == "Y":
                                daftarmobil[index]["tahun"] = int(tahun)
                                print("Data Berhasil Diedit!")
                                break
                            else:
                                break
                        elif m3_edit_input == "warna": #Mengubah kolom warna
                            while True:
                                m3_1_warna_input = input("Silahkan masukkan warna mobil:")
                                if len(m3_1_warna_input) <= 30:
                                    break
                                else:
                                    print("***Mohon masukkan warna mobil maksimal 30 karakter***")
                                    continue
                            result = save_data_options()
                            if result == "Y":
                                daftarmobil[index]["warna"] = m3_1_warna_input
                                print("Data Berhasil Diedit!")
                                break
                            else:
                                break
                        elif m3_edit_input == "mesin": #Mengubah kolom mesin
                            while True:
                                m3_1_mesin_input = input("Silahkan masukkan mesin mobil:")
                                if len(m3_1_mesin_input) <= 30:
                                    break
                                else:
                                    print("***Mohon masukkan jenis mesin maksimal 30 karakter***")
                                    continue
                            result = save_data_options()
                            if result == "Y":
                                daftarmobil[index]["mesin"] = m3_1_mesin_input
                                print("Data Berhasil Diedit!")
                                break
                            else:
                                break
                        else:
                            print("*** Kolom tidak ditemukan, silahkan dicoba kembali! ***")
                            continue
                    menu3()     
                else: #Jika user tidak mengonfirmasi, kembali ke menu 3
                    menu3()
            else: #Jika index yang user tidak ditemukan, kembali ke menu 3
                print("*** index tidak ditemukan, silahkan masukkan kembali ***")
                menu3()
        else: #Jika user memasukan index selain data numeric, akan ada peringatan
            print("*** Mohon masukan nomor index yang tepat, silahkan masukkan kembali *** ")
            menu3()
    elif (m3_input == "2"):#Kembali ke menu utama
        mainmenu()
    else:## WARNING - Kode input tidak sesuai
        print("*** Mohon masukan kode menu yang tepat, silahkan masukan kembali *** ")
        menu3()

### MENU 4 ### - Menghapus data mobil rental
def menu4():
    global daftarmobil
    m4_input = input('''
    ### SELAMAT DATANG DI RENTAL SULTAN ###
    1. Menghapus data mobil
    2. Kembali ke Main Menu
    Silahkan untuk pilih menu yang dituju: ''')
    if (m4_input == "1"): #Menghapus kolom menu berdasarkan index yang diinput user
        datamobil_withindex()
        m4_1_index_input = input("Silahkan masukkan nomor index yang ingin di hapus: ") 
        if m4_1_index_input.isdecimal(): #Jika index yang diinput user berupa angka, maka lanjutkan
            if int(m4_1_index_input) <= len(daftarmobil)-1 and int(m4_1_index_input) >= 0: 
                index = int(m4_1_index_input)
                print(tabulate([daftarmobil[index].values()],["Plat","Jenis","Tahun","Warna","Mesin"],tablefmt="pretty"))
                result = menu4_confirmation_delete()
                if result == "Y":   #Jika user confirm untuk hapus, lanjutkan
                    del daftarmobil[index]
                    print("Data berhasil dihapus!")
                    menu4()
                else:#jika tidak jadi menghapus, kembali ke menu 4
                    menu4()
            else:#jika index yang di input user tidak tersedia pada database, maka kembali ke menu 4
                print("*** index tidak ditemukan, silahkan masukkan kembali ***")
                menu4()
        else:#Jika user memasukan data selain angka, maka akan ada peringatan
            print("*** Mohon masukan nomor index yang tepat, silahkan masukkan kembali *** ")
            menu4()
    elif (m4_input == "2"):#Kembali ke menu utama
        mainmenu()
    else: ## WARNING - Kode input tidak sesuai
        print("*** Mohon masukan kode menu yang tepat, silahkan masukan kembali *** ")
        menu4()

### MENU 5 ### - Keluar dari program
def menu5():
    print("*** Anda Telah Keluar Dari Program ***")

### MAIN MENU  ## 
def mainmenu():
    mm_input = input('''
    ### SELAMAT DATANG DI RENTAL SULTAN ###
    1. Tampilkan daftar mobil rental
    2. Menambah mobil rental
    3. Mengubah data mobil rental
    4. Menghapus data mobil rental
    5. Keluar           
    Silahkan untuk pilih menu yang dituju: ''')
    if (mm_input == "1"): #Tampilkan daftar mobil rental
        menu1()
    elif (mm_input == "2"):#Menambah mobil rental
        menu2()
    elif (mm_input == "3"):#Mengubah data mobil rental
        menu3()
    elif (mm_input == "4"):#Menghapus data mobil rental
        menu4()
    elif (mm_input == "5"):#Keluar dari program
        menu5()
    else: #input yang dimasukkan user tidak sesuai, berikan peringatan
        print("*** Mohon masukan kode menu yang tepat, silahkan masukan kembali *** ")
        mainmenu()

################################################ 
        
##### START PROGRAM ####
mainmenu()