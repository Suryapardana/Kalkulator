import time

print("\033[93m\n" * 100)

def fazga():
    
    print("##    ##    ###    ##       ##    ## ##     ## ##          ###    ########  #######  ########     ########  ##    ##") 
    print("##   ##    ## ##   ##       ##   ##  ##     ## ##         ## ##      ##    ##     ## ##     ##    ##     ##  ##  ##") 
    print("##  ##    ##   ##  ##       ##  ##   ##     ## ##        ##   ##     ##    ##     ## ##     ##    ##     ##   ####")   
    print("#####    ##     ## ##       #####    ##     ## ##       ##     ##    ##    ##     ## ########     ########     ##")   
    print("##  ##   ######### ##       ##  ##   ##     ## ##       #########    ##    ##     ## ##   ##      ##           ##")    
    print("##   ##  ##     ## ##       ##   ##  ##     ## ##       ##     ##    ##    ##     ## ##    ##     ##           ##")    
    print("##    ## ##     ## ######## ##    ##  #######  ######## ##     ##    ##     #######  ##     ##    ##           ##")
    print("\n\t\t\tCoded by : Angga Surya Pardana (github.com/EvCf1703)")
    print("\033[91m\t\t\tHighly Perfection by : M.Fazri Nizar (github.com/Anon6372098)")
    print("\033[93m\t\t\tTeam : D4RK SYST3M F41LUR3 S33K3R (github.com/DSFS-org)")
    time.sleep(2)
    
    def tambah(fazri, angga):
        return fazri + angga

    def kurang(fazri, angga):
        return fazri - angga

    def kali(fazri, angga):
        return fazri * angga
   
    def bagi(fazri, angga):
        return fazri / angga
   
    def hasil_bagi(fazri, angga):
        return fazri % angga
        
    def pangkat(fazri, angga):
        return fazri ** angga
    
    def bulat(fazri, angga):
        return fazri // angga

    print("\nPilih ?\n")
    print("1. Pertambahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Sisa dari Pembagian")
    print("6. Pangkat")
    print("7. Pembagian Bulat")
    print("8. Keluar")

    xyz = raw_input("\nMasukkan pilihan (Angka) : ")

    if xyz == '1':
        faz = int(input("\nMasukkan angka pertama : "))
        rya = int(input("Masukkan angka kedua : "))
        print("\n",faz,"+",rya,"=", tambah(faz,rya))
        time.sleep(3)
        print ("\n" * 100)
        fazga()
        
    elif xyz == '2':
        faz = int(input("\nMasukkan angka pertama : "))
        rya = int(input("Masukkan angka kedua : "))
        print("\n",faz,"-",rya,"=", kurang(faz,rya))
        time.sleep(3)
        print ("\n" * 100)
        fazga()
        
    elif xyz == '3':
        faz = int(input("\nMasukkan angka pertama : "))
        rya = int(input("Masukkan angka kedua : "))
        print("\n",faz,"*",rya,"=", kali(faz,rya))
        time.sleep(3)
        print ("\n" * 100)
        fazga()
        
    elif xyz == '4':
        faz = int(input("\nMasukkan angka pertama : "))
        rya = int(input("Masukkan angka kedua : "))
        print("\n",faz,"/",rya,"=", bagi(faz,rya))
        time.sleep(3)
        print ("\n" * 100)
        fazga()
        
    elif xyz == '5':
        faz = int(input("\nMasukkan angka pertama : "))
        rya = int(input("Masukkan angka kedua : "))
        print("\n",faz,"%",rya,"=", hasil_bagi(faz,rya))
        time.sleep(3)
        print ("\n" * 100)
        fazga()
        
    elif xyz == '6':
        faz = int(input("\nMasukkan angka pertama : "))
        rya = int(input("Masukkan angka kedua : "))
        print("\n",faz,"**",rya,"=", pangkat(faz,rya))
        time.sleep(3)
        print ("\n" * 100)
        fazga()
        
    elif xyz == '7':
        faz = int(input("\nMasukkan angka pertama : "))
        rya = int(input("Masukkan angka kedua : "))
        print("\n",faz,"//",rya,"=", bulat(faz,rya))
        time.sleep(3)
        print ("\n" * 100)
        fazga()
        
    elif xyz == '8':
        print("\033[92m\nJumpa Lagi Gan :)")
        time.sleep(2)
        print ("\n" * 100)
        exit
        
    else:
        print("\033[91m\nSalah Pilihan !")
        time.sleep(2)
        print ("\n" * 100)
        fazga()
        
fazga()
