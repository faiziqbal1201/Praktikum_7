def tambah(nama, nilai):
    data_mahasiswa.append({"nama": nama, "nilai": nilai})

def tampilkan():
    for mahasiswa in data_mahasiswa:
        print(f"Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")

def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [mahasiswa for mahasiswa in data_mahasiswa if mahasiswa['nama'] != nama]

def ubah(nama, nilai):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = nilai

data_mahasiswa = []

tambah("Arlot", 100)
tambah("Brody", 95)
tambah("Estes", 60)

tampilkan()

hapus("Brody")

tampilkan()

ubah("Estes", 82)

tampilkan()