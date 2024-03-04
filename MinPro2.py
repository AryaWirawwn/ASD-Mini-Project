import os

class NodeKeyboard():
    def __init__(self, idKeyboard, pcb, case, switch, keyCaps, stabilizer):
        self.idKeyboard = idKeyboard
        self.pcb = pcb
        self.case = case
        self.switch = switch
        self.keyCaps = keyCaps
        self.stabilizer = stabilizer
        self.next = None

class ManajemenKeyboard():
    def __init__(self):
        self.head = None
    
    def tambahKeyboard(self, idKeyboard, pcb, case, switch, keyCaps, stabilizer):
        if self.head == None:
            self.head = NodeKeyboard(idKeyboard, pcb, case, switch, keyCaps, stabilizer)
        else:
            new_node = NodeKeyboard(idKeyboard, pcb, case, switch, keyCaps, stabilizer)
            new_node.next = self.head
            self.head = new_node
    
    def tambahKeyboardDariTengah(self, prev_id, idKeyboard, pcb, case, switch, keyCaps, stabilizer):
        new_node = NodeKeyboard(idKeyboard, pcb, case, switch, keyCaps, stabilizer)
        if self.head is None:
            print("Daftar keyboard kosong, tidak bisa menambahkan ke tengah.")
            return
        else:
            current = self.head
            while current.next:
                if current.idKeyboard == prev_id:
                    new_node.next = current.next
                    current.next = new_node
                    return
                current = current.next
            print("ID keyboard sebelumnya tidak ditemukan.")
        
    def tambahKeyboardDariTail(self, idKeyboard, pcb, case, switch, keyCaps, stabilizer):
        new_node = NodeKeyboard(idKeyboard, pcb, case, switch, keyCaps, stabilizer)
        if self.head == None:
            self.head = NodeKeyboard(idKeyboard, pcb, case, switch, keyCaps, stabilizer)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = NodeKeyboard(idKeyboard, pcb, case, switch, keyCaps, stabilizer)

    def cekIdKeyboard(self, idKeyboard):
        current = self.head
        while current:
            if current.idKeyboard == idKeyboard:
                return True
            current = current.next
        return False
    
    def perbaruiKeyboard(self, idKeyboard, pcb, case, switch, keyCaps, stabilizer):
        current = self.head
        while current:
            if current.idKeyboard == idKeyboard:
                current.pcb = pcb
                current.case = case
                current.switch = switch
                current.keyCaps = keyCaps
                current.stabilizer = stabilizer
                return True
            current = current.next
        return False

    def tampilkanKeyboard(self):
        if self.head == None:
            print("Dafter Keyboard Kosong.")
        else:
            current = self.head
            print("Daftar Keyboard")
            print("")
            i = 1
            while current:
                print(f"Keyboard ke-{i}")
                print(f"ID Keyboard: {current.idKeyboard}")
                print(f"PCB Keyboard: {current.pcb}")
                print(f"Case Keyboard: {current.case}")
                print(f"Switch Keyboard: {current.switch}")
                print(f"Keycaps Keyboard: {current.keyCaps}")
                print(f"Stabilizer Keyboard: {current.stabilizer}")
                print("")
                current = current.next
                i += 1

    def hapusKeyboard(self, idKeyboard):
        if self.head is None:
            print("Daftar Keyboard Kosong.")
            return
        else:
            # Jika keyboard yang akan dihapus adalah keyboard pertama
            if self.head.idKeyboard == idKeyboard:
                self.head = self.head.next
                print(f"Keyboard dengan ID {idKeyboard} berhasil dihapus.")
                return

            # Mencari keyboard yang akan dihapus
            current = self.head
            while current.next is not None:
                if current.next.idKeyboard == idKeyboard:
                    current.next = current.next.next
                    print(f"Keyboard dengan ID {idKeyboard} berhasil dihapus.")
                    return
                current = current.next

            # Jika keyboard tidak ditemukan
            print(f"Keyboard dengan ID {idKeyboard} tidak ditemukan.")

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
            os.system("cls")
            print("+=========================+")
            print("| [1]. Tambah Di Awal     |")
            print("| [2]. Tambah Di Tengah   |")
            print("| [3]. Tambah Di Akhir    |")
            print("+=========================+")
            pilihanTambah = int(input("Masukkan Pilihan[1/2/3]: "))
            if pilihanTambah == 1:
                idKeyboard = input("Masukkan ID Keyboard 6 Digit: ")
                if idKeyboard.isnumeric() and len(idKeyboard) == 6:
                    if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                        print("ID Sudah Ada di Database")
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

            elif pilihanTambah == 2:
                idKeyboard = input("Masukkan ID Keyboard 6 Digit: ")
                if idKeyboard.isnumeric() and len(idKeyboard) == 6:
                    if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                        print("ID Sudah Ada di Database")
                        input("Tekan enter untuk melanjutkan...")
                    else:
                        pcb = str(input("Masukkan Nama PCB: "))
                        case = str(input("Masukkan Nama Case: "))
                        switch = str(input("Masukkan Nama Switch: "))
                        keyCaps = str(input("Masukkan Nama Keycaps: "))
                        stabilizer = str(input("Masukkan Nama Stabilizer: "))

                        prev_id = input("Masukkan ID Keyboard Sebelumnya: ")
                        manajemenKeyboardobj.tambahKeyboardDariTengah(prev_id, idKeyboard, pcb, case, switch, keyCaps, stabilizer)
                        input("Tekan enter untuk melanjutkan...")
                else:
                    print("Pastikan ID hanya angka dan 6 digit.")
                    input("Tekan enter untuk melanjutkan...")

            elif pilihanTambah == 3:
                idKeyboard = input("Masukkan ID Keyboard 6 Digit: ")
                if idKeyboard.isnumeric() and len(idKeyboard) == 6:
                    if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                        print("ID Sudah Ada di Database")
                        input("Tekan enter untuk melanjutkan...")
                    else:
                        pcb = str(input("Masukkan Nama PCB: "))
                        case = str(input("Masukkan Nama Case: "))
                        switch = str(input("Masukkan Nama Switch: "))
                        keyCaps = str(input("Masukkan Nama Keycaps: "))
                        stabilizer = str(input("Masukkan Nama Stabilizer: "))
                        manajemenKeyboardobj.tambahKeyboardDariTail(idKeyboard, pcb, case, switch, keyCaps, stabilizer)
                        input("Tekan enter untuk melanjutkan...")
                else:
                    print("Pastikan ID hanya angka dan 6 digit.")
                    input("Tekan enter untuk melanjutkan...")
            
            else:
                print("Pilihan Tidak Ada.")
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
            os.system('cls')
            idKeyboard = input("Masukkan ID Keyboard: ")
            if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                manajemenKeyboardobj.hapusKeyboard(idKeyboard)
                input("Tekan enter untuk melanjutkan...")
            else:
                print(f"Keyboard dengan ID {idKeyboard} Tidak Ada di Database.")
                input("Tekan enter untuk melanjutkan...")
        
        elif pilihan == 5:
            break

        else:
            print("Pilihan Tidak Ada.")
            input("Tekan enter untuk melanjutkan...")

menu()
