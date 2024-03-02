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
        nodeBaru = NodeKeyboard(idKeyboard, pcb, case, switch, keyCaps, stabilizer)
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
            print("Tidak Ada Data Keyboard")
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
        if self.head == None:
            return
        else:
            current = self.head
            while current is not None:
                if current.idKeyboard == idKeyboard:
                    if current.next is None:
                        current = None
                        return
                    else:
                        current.idKeyboard = current.next.idKeyboard
                        current.pcb = current.next.pcb
                        current.case = current.next.case
                        current.switch = current.next.switch
                        current.keyCaps = current.next.keyCaps
                        current.stabilizer = current.next.stabilizer
                        current.next = current.next.next
                        return
                current = current.next

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
            if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                manajemenKeyboardobj.hapusKeyboard(idKeyboard)
                print(f"Keyboard dengan ID {idKeyboard} berhasil dihapus.")
                input("Tekan enter untuk melanjutkan...")
            else:
                print(f"Keyboard dengan ID {idKeyboard} Tidak Ada di Database.")
                input("Tekan enter untuk melanjutkan...")
        
        elif pilihan == 5:
            break

menu()