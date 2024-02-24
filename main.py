import os

class ManajemenKeyboard():

    def __init__(self):
        self.keyboard = {"121212": {
            "PCB": "Hotswap",
            "Case":"Aluminium",
            "Switch": "Blue",
            "Keycaps":"Asuka",
            "Stabilizer": "Durock"
        }}
    
    def tambahKeyboard(self, idKeyboard, pcb, case, switch, keyCaps, stabilizer):
        self.keyboard[idKeyboard] = {"PCB": pcb, "Case": case, "Switch": switch, "Keycaps": keyCaps, "Stabilizer": stabilizer}
        print(f"Keyboard dengan ID {idKeyboard} Berhasil di Tambahkan.")

    def cekIdKeyboard(self, idKeyboard):
        return idKeyboard in self.keyboard
    
    def perbaruiKeyboard(self, idKeyboard, pcb, case, switch, keyCaps, stabilizer):
        keyboard = self.keyboard[idKeyboard]
        keyboard["PCB"] = pcb
        keyboard["Case"] = case
        keyboard["Switch"] = switch
        keyboard["Keycaps"] = keyCaps
        keyboard["Stabilizer"] = stabilizer
        print(f"Keyboard dengan ID {idKeyboard} Berhasil di Ubah.")

    def tampilkanKeyboard(self):
        print("Daftar Keyboard")
        print("")
        for i, (idKeyboard, data) in enumerate(self.keyboard.items(), 1):
            print(f"Keyboard ke-{i}")
            print(f"ID Keyboard: {idKeyboard}")
            print(f"PCB: {data['PCB']}")
            print(f"Case: {data['Case']}")
            print(f"Switch: {data['Switch']}")
            print(f"Keycaps: {data['Keycaps']}")
            print(f"Stabilizer: {data['Stabilizer']}")
            print("")

    def hapusKeyboard(self, idKeyboard):
        if idKeyboard in self.keyboard:
            self.keyboard.pop(idKeyboard)
            print(f"Keyboard dengan ID {idKeyboard} Berhasil di Hapus.")
        else:
            print(f"Keyboard dengan ID {idKeyboard} Tidak Ada di Database.")



def menu():
    manajemenKeyboardobj = ManajemenKeyboard()
    while True:
        os.system("cls")
        print("+=========================+")
        print("| [1]. Tambah Keyboard    |")
        print("| [2]. Perbarui Keyboard  |")
        print("| [3]. Tampilkan Keyboard |")
        print("| [4]. Hapus Keyboard     |")
        print("| [5]. Keluar             |")
        print("+=========================+")
        pilihan = int(input("Masukkan Pilihan [1/2/3/4/5]: "))
        if pilihan == 1:
            idKeyboard = input("Masukkan ID Keyboard 6 Digit: ")
            if idKeyboard.isnumeric() and len(idKeyboard) == 6:
                if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                    print(f"Keyboard dengan ID {idKeyboard} Sudah Ada.")
                    input("Tekan enter untuk melanjutkan...")
                else:
                    pcb = str(input("Masukkan Nama PCB: "))
                    case = str(input("Masukkan Nama Case: "))
                    switch = str(input("Masukkan Nama Switch: "))
                    keyCaps = str(input("Masukkan Nama Keycaps: "))
                    stabilizer = str(input("Masukkan Nama Stabilizer: "))
                    manajemenKeyboardobj.tambahKeyboard(idKeyboard, pcb, case, switch, keyCaps, stabilizer)
                    input("Tekan enter untuk melanjutkan...")
            else:
                print("Pastikan ID hanya angka dan 6 digit.")
                input("Tekan enter untuk melanjutkan...")
        
        elif pilihan == 2:
            os.system('cls')
            idKeyboard = input("Masukkan ID Keyboard: ")
            if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                pcb = str(input("Masukkan Nama PCB: "))
                case = str(input("Masukkan Nama Case: "))
                switch = str(input("Masukkan Nama Switch: "))
                keyCaps = str(input("Masukkan Nama Keycaps: "))
                stabilizer = str(input("Masukkan Nama Stabilizer: "))
                manajemenKeyboardobj.perbaruiKeyboard(idKeyboard, pcb, case, switch, keyCaps, stabilizer)
                input("Tekan enter untuk melajutkan...")
            else:
                print(f"Keyboard dengan ID {idKeyboard} Tidak Ada di Database.")
                input("Tekan enter untuk melajutkan...")
        
        elif pilihan == 3:
            os.system('cls')
            manajemenKeyboardobj.tampilkanKeyboard()
            input("Tekan enter untuk melanjutkan...")
        
        elif pilihan == 4:
            idKeyboard = input("Masukkan ID Keyboard: ")
            manajemenKeyboardobj.hapusKeyboard(idKeyboard)
            input("Tekan enter untuk melanjutkan...")
        
        elif pilihan == 5:
            break

menu()