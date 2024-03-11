import os

class NodeKeyboard():
    def __init__(self, idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer):
        self.idKeyboard = idKeyboard
        self.namaKeyboard = namaKeyboard
        self.pcb = pcb
        self.case = case
        self.switch = switch
        self.keyCaps = keyCaps
        self.stabilizer = stabilizer
        self.next = None

class ManajemenKeyboard():
    def __init__(self):
        self.head = None
    
    def tambahKeyboard(self, idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer):
        if self.head == None:
            self.head = NodeKeyboard(idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)
        else:
            new_node = NodeKeyboard(idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)
            new_node.next = self.head
            self.head = new_node
    
    def tambahKeyboardDariTengah(self, prev_id, idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer):
        new_node = NodeKeyboard(idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)
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
        
    def tambahKeyboardDariTail(self, idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer):
        new_node = NodeKeyboard(idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)
        if self.head == None:
            self.head = NodeKeyboard(idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = NodeKeyboard(idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)

    def cekIdKeyboard(self, idKeyboard):
        current = self.head
        while current:
            if current.idKeyboard == idKeyboard:
                return True
            current = current.next
        return False
    
    def perbaruiKeyboard(self, idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer):
        current = self.head
        while current:
            if current.idKeyboard == idKeyboard:
                current.namaKeyboard = namaKeyboard
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
                print(f"Nama Keyboard: {current.namaKeyboard}")
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
            if self.head.idKeyboard == idKeyboard:
                self.head = self.head.next
                print(f"Keyboard dengan ID {idKeyboard} berhasil dihapus.")
                return
            current = self.head
            while current.next is not None:
                if current.next.idKeyboard == idKeyboard:
                    current.next = current.next.next
                    print(f"Keyboard dengan ID {idKeyboard} berhasil dihapus.")
                    return
                current = current.next
            print(f"Keyboard dengan ID {idKeyboard} tidak ditemukan.")
    
    def quickSortId(self, descending = False):
        if self.head is None:
            print("Daftar Keyboard Kosong.")
            return
        else:
            daftarIdKeyboard = []
            current = self.head
            while current:
                daftarIdKeyboard.append(current.idKeyboard)
                current = current.next
            daftarIdKeyboardSorted = self.quickSort(daftarIdKeyboard, descending)
            print("")
            print("ID Keyboard setelah diurutkan:")
            print("")
            for idKeyboard in daftarIdKeyboardSorted:
                current = self.head
                while current:
                    if current.idKeyboard == idKeyboard:
                        print(f"ID Keyboard: {current.idKeyboard}")
                        print(f"Nama Keyboard: {current.namaKeyboard}")
                        print(f"PCB Keyboard: {current.pcb}")
                        print(f"Case Keyboard: {current.case}")
                        print(f"Switch Keyboard: {current.switch}")
                        print(f"Keycaps Keyboard: {current.keyCaps}")
                        print(f"Stabilizer Keyboard: {current.stabilizer}")
                        print("")
                        break
                    current = current.next
            return daftarIdKeyboardSorted

    def quickSortNama(self, descending = False):
        if self.head is None:
            print("Daftar Keyboard Kosong.")
            return
        else:
            daftarNamaKeyboard = []
            current = self.head
            while current:
                daftarNamaKeyboard.append(current.namaKeyboard)
                current = current.next
            daftarNamaKeyboardSorted = self.quickSort(daftarNamaKeyboard, descending)
            print("")
            print("ID Keyboard setelah diurutkan:")
            print("")
            for namaKeyboard in daftarNamaKeyboardSorted:
                current = self.head
                while current:
                    if current.namaKeyboard == namaKeyboard:
                        print(f"Nama Keyboard: {current.namaKeyboard}")
                        print(f"ID Keyboard: {current.idKeyboard}")
                        print(f"PCB Keyboard: {current.pcb}")
                        print(f"Case Keyboard: {current.case}")
                        print(f"Switch Keyboard: {current.switch}")
                        print(f"Keycaps Keyboard: {current.keyCaps}")
                        print(f"Stabilizer Keyboard: {current.stabilizer}")
                        print("")
                        break
                    current = current.next
            return daftarNamaKeyboardSorted
        
    def quickSort(self, daftar, descending = False):
        if len(daftar) <= 1:
            return daftar
        pivot = daftar[len(daftar) // 2]
        if descending:  # Memperbaiki logika untuk descending
            left = [x for x in daftar if x > pivot]
            right = [x for x in daftar if x < pivot]
        else:  # Memperbaiki logika untuk ascending
            left = [x for x in daftar if x < pivot]
            right = [x for x in daftar if x > pivot]
        middle = [x for x in daftar if x == pivot]
        return self.quickSort(left, descending) + middle + self.quickSort(right, descending)


global manajemenKeyboardobj
manajemenKeyboardobj = ManajemenKeyboard()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def menu():
    while True:
        clear()
        print("+=========================+")
        print("| [1]. Tambah Keyboard    |")
        print("| [2]. Perbarui Keyboard  |")
        print("| [3]. Tampilkan Keyboard |")
        print("| [4]. Hapus Keyboard     |")
        print("| [5]. Urutkan            |")
        print("| [6]. Keluar             |")
        print("+=========================+")
        try:
            pilihan = int(input("Masukkan Pilihan [1/2/3/4/5]: "))
            if pilihan == 1:
                tambahKeyboard()
            elif pilihan == 2:
                perbaruiKeyboard()
            elif pilihan == 3:
                tampilkanKeyboard()
            elif pilihan == 4:
                hapusKeyboard()
            elif pilihan == 5:
                urutkanKeyboard()      
            elif pilihan == 6:
                clear()
                print("Terima Kasih Telah Menggunakan Program Ini")
                break
            else:
                print("Pilihan tidak ada.")
                input("Tekan enter untuk melanjutkan...")
        except ValueError:
            clear()
            print("Inputan salah.")
            input("Tekan enter untuk melanjutkan...")

def tambahKeyboard():
    clear()
    print("+=========================+")
    print("| [1]. Tambah Di Awal     |")
    print("| [2]. Tambah Di Tengah   |")
    print("| [3]. Tambah Di Akhir    |")
    print("+=========================+")
    try:
        pilihan = int(input("Masukkan Pilihan [1/2/3]: "))
        if pilihan == 1:
            idKeyboard = input("Masukkan ID Keyboard 6 Digit: ")
            if idKeyboard.isnumeric() and len(idKeyboard) == 6:
                if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                    print("ID sudah ada di database")
                    input("Tekan enter untuk melanjutkan...")
                else:
                    namaKeyboard = str(input("Masukkan Nama Keyboard: "))
                    if namaKeyboard != "":
                        pcb = str(input("Masukkan Nama PCB: "))
                        if pcb != "":
                            case = str(input("Masukkan Nama Case: "))
                            if case != "":
                                switch = str(input("Masukkan Nama Switch: "))
                                if switch != "":
                                    keyCaps = str(input("Masukkan Nama Keycaps: "))
                                    if keyCaps != "":
                                        stabilizer = str(input("Masukkan Nama Stabilizer: "))
                                        if stabilizer != "":
                                            manajemenKeyboardobj.tambahKeyboard(idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)
                                            print(f"Keyboard dengan ID {idKeyboard} berhasil ditambahkan.")
                                            input("Tekan enter untuk melanjutkan...")
                                        else:
                                            print("Nama Stabilizer tidak boleh kosong.")
                                            input("Tekan enter untuk melanjutkan...")
                                    else:
                                        print("Nama Keycaps tidak boleh kosong.")
                                        input("Tekan enter untuk melanjutkan...")
                                else:
                                    print("Nama Switch tidak boleh kosong.")
                                    input("Tekan enter untuk melanjutkan...")
                            else:
                                print("Nama Case tidak boleh kosong.")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            print("Nama PCB tidak boleh kosong.")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        print("Nama keyboard tidak boleh kosong.")
                        input("Tekan enter untuk melanjutkan...")
            else:
                print("Pastikan ID hanya angka dan 6 digit.")
                input("Tekan enter untuk melanjutkan...")

        elif pilihan == 2:
            idKeyboard = input("Masukkan ID Keyboard 6 Digit: ")
            if idKeyboard.isnumeric() and len(idKeyboard) == 6:
                if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                    print("ID sudah ada di database")
                    input("Tekan enter untuk melanjutkan...")
                else:
                    namaKeyboard = str(input("Masukkan Nama Keyboard: "))
                    if namaKeyboard != "":
                        pcb = str(input("Masukkan Nama PCB: "))
                        if pcb != "":
                            case = str(input("Masukkan Nama Case: "))
                            if case != "":
                                switch = str(input("Masukkan Nama Switch: "))
                                if switch != "":
                                    keyCaps = str(input("Masukkan Nama Keycaps: "))
                                    if keyCaps != "":
                                        stabilizer = str(input("Masukkan Nama Stabilizer: "))
                                        if stabilizer != "":
                                            prev_id = input("Masukkan ID Keyboard Sebelumnya: ")
                                            manajemenKeyboardobj.tambahKeyboardDariTengah(prev_id, idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)
                                            print(f"Keyboard dengan ID {idKeyboard} berhasil ditambahkan.")
                                            input("Tekan enter untuk melanjutkan...")
                                        else:
                                            print("Nama Stabilizer tidak boleh kosong.")
                                            input("Tekan enter untuk melanjutkan...")
                                    else:
                                        print("Nama Keycaps tidak boleh kosong.")
                                        input("Tekan enter untuk melanjutkan...")
                                else:
                                    print("Nama Switch tidak boleh kosong.")
                                    input("Tekan enter untuk melanjutkan...")
                            else:
                                print("Nama Case tidak boleh kosong.")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            print("Nama PCB tidak boleh kosong.")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        print("Nama keyboard tidak boleh kosong.")
                        input("Tekan enter untuk melanjutkan...")
            else:
                print("Pastikan ID hanya angka dan 6 digit.")
                input("Tekan enter untuk melanjutkan...")

        elif pilihan == 3:
            idKeyboard = input("Masukkan ID Keyboard 6 Digit: ")
            if idKeyboard.isnumeric() and len(idKeyboard) == 6:
                if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
                    print("ID sudah ada di database")
                    input("Tekan enter untuk melanjutkan...")
                else:
                    namaKeyboard = str(input("Masukkan Nama Keyboard: "))
                    if namaKeyboard != "":
                        pcb = str(input("Masukkan Nama PCB: "))
                        if pcb != "":
                            case = str(input("Masukkan Nama Case: "))
                            if case != "":
                                switch = str(input("Masukkan Nama Switch: "))
                                if switch != "":
                                    keyCaps = str(input("Masukkan Nama Keycaps: "))
                                    if keyCaps != "":
                                        stabilizer = str(input("Masukkan Nama Stabilizer: "))
                                        if stabilizer != "":
                                            manajemenKeyboardobj.tambahKeyboardDariTail(idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)
                                            print(f"Keyboard dengan ID {idKeyboard} berhasil ditambahkan.")
                                            input("Tekan enter untuk melanjutkan...")
                                        else:
                                            print("Nama Stabilizer tidak boleh kosong.")
                                            input("Tekan enter untuk melanjutkan...")
                                    else:
                                        print("Nama Keycaps tidak boleh kosong.")
                                        input("Tekan enter untuk melanjutkan...")
                                else:
                                    print("Nama Switch tidak boleh kosong.")
                                    input("Tekan enter untuk melanjutkan...")
                            else:
                                print("Nama Case tidak boleh kosong.")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            print("Nama PCB tidak boleh kosong.")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        print("Nama keyboard tidak boleh kosong.")
                        input("Tekan enter untuk melanjutkan...")
            else:
                print("Pastikan ID hanya angka dan 6 digit.")
                input("Tekan enter untuk melanjutkan...")
        
        else:
            print("Pilihan Tidak Ada.")
            input("Tekan enter untuk melanjutkan...")
    except ValueError:
        clear()
        print("Inputan salah.")
        input("Tekan enter untuk melanjutkan...")

def perbaruiKeyboard():
    clear()
    idKeyboard = input("Masukkan ID Keyboard: ")
    if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
        namaKeyboard = str(input("Masukkan Nama Keyboard: "))
        if namaKeyboard != "":
            pcb = str(input("Masukkan Nama PCB: "))
            if pcb != "":
                case = str(input("Masukkan Nama Case: "))
                if case != "":
                    switch = str(input("Masukkan Nama Switch: "))
                    if switch != "":
                        keyCaps = str(input("Masukkan Nama Keycaps: "))
                        if keyCaps != "":
                            stabilizer = str(input("Masukkan Nama Stabilizer: "))
                            if stabilizer != "":
                                manajemenKeyboardobj.perbaruiKeyboard(idKeyboard, namaKeyboard, pcb, case, switch, keyCaps, stabilizer)
                                print(f"Keyboard dengan ID {idKeyboard} berhasil diperbarui.")
                                input("Tekan enter untuk melanjutkan...")
                            else:
                                print("Nama Stabilizer tidak boleh kosong.")
                                input("Tekan enter untuk melanjutkan...")
                        else:
                            print("Nama Keycaps tidak boleh kosong.")
                            input("Tekan enter untuk melanjutkan...")
                    else:
                        print("Nama Switch tidak boleh kosong.")
                        input("Tekan enter untuk melanjutkan...")
                else:
                    print("Nama Case tidak boleh kosong.")
                    input("Tekan enter untuk melanjutkan...")
            else:
                print("Nama PCB tidak boleh kosong.")
                input("Tekan enter untuk melanjutkan...")
        else:
            print("Nama keyboard tidak boleh kosong.")
            input("Tekan enter untuk melanjutkan...")
    else:
        print(f"Keyboard dengan ID {idKeyboard} Tidak Ada di Database.")
        input("Tekan enter untuk melajutkan...")

def tampilkanKeyboard():
    clear()
    manajemenKeyboardobj.tampilkanKeyboard()
    input("Tekan enter untuk melanjutkan...")
    
def hapusKeyboard():
    clear()
    idKeyboard = input("Masukkan ID Keyboard: ")
    if manajemenKeyboardobj.cekIdKeyboard(idKeyboard):
        manajemenKeyboardobj.hapusKeyboard(idKeyboard)
        input("Tekan enter untuk melanjutkan...")
    else:
        print(f"Keyboard dengan ID {idKeyboard} Tidak Ada di Database.")
        input("Tekan enter untuk melanjutkan...")

def urutkanKeyboard():
    clear()
    print("+======================================+")
    print("| [1]. Berdasarkan ID [Ascending]      |")
    print("| [2]. Berdasarkan ID [Descending]     |")
    print("| [3]. Berdasarkan Nama [Ascending]    |")
    print("| [4]. Berdasarkan Nama [Descending]   |")
    print("+======================================+")
    try:
        pilihan = int(input("Masukkan Pilihan [1/2]: "))
        if pilihan == 1:
            manajemenKeyboardobj.quickSortId()
            input("Tekan enter untuk melanjutkan...")
        elif pilihan == 2:
            manajemenKeyboardobj.quickSortNama(descending = True)
            input("Tekan enter untuk melanjutkan...")
        elif pilihan == 3:
            manajemenKeyboardobj.quickSortNama()
            input("Tekan enter untuk melanjutkan...")
        elif pilihan == 4:
            manajemenKeyboardobj.quickSortNama(descending = True)
            input("Tekan enter untuk melanjutkan...")
        else:
            print("Pilihan Tidak Ada.")
            input("Tekan enter untuk melanjutkan...")
    except ValueError:
        clear()
        print("Inputan salah.")
        input("Tekan enter untuk melanjutkan...")

menu()
