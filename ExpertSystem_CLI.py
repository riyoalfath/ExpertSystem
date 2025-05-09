# Input rule 1, kondisi bibit ikan
def determine_kondisi_bibit(bentuk_kepala, kelincahan, warna_kulit, kecacatan):
    # Kecacatan:
    #    1 = Sirip Merah
    #    2 = Moncong Putih
    #    3 = Tidak Ada
    if kecacatan in [1, 2]:
        return "Tidak Sehat"
    
    # Warna Kulit:
    #    1 = Mengkilap
    #    2 = Buram
    if warna_kulit == 2:
        return "Tidak Sehat"

    # Bentuk Kepala:
    #    1 = Runcing
    #    2 = Gemuk
    if bentuk_kepala == 2 and warna_kulit == 1 and kecacatan == 3:
        return "Sehat"
    
    # Kelincahan:
    #    1 = Lincah
    #    2 = Lambat
    if bentuk_kepala == 1 and kelincahan == 1 and warna_kulit == 1 and kecacatan == 3:
        return "Sehat"
    
    if bentuk_kepala == 1 and kelincahan == 2 and warna_kulit == 1 and kecacatan == 3:
        return "Tidak Sehat"
    return "Tidak Valid"

# Input rule 2, kondisi kolam ikan
def determine_kondisi_kolam(ph_air, suhu):
    # pH Air:
    #    1 = Tinggi
    #    2 = Netral
    #    3 = Rendah
    if ph_air in [1, 3]:  # 1: Tinggi, 2: Netral, 3: Rendah
        if 27 <= suhu <= 30:
            return "Cukup Baik"
        else:
            return "Buruk"

    # Suhu Air:
    #    Int, contoh: 27.5, 28, 30
    if ph_air == 2:  # Netral
        if 27 <= suhu <= 30:
            return "Baik"
        else:
            return "Cukup Baik"
    return "Tidak Valid"

# Input rule 3, kondisi pertumbuhan ikan
def determine_hasil_keputusan(kondisi_bibit, kondisi_kolam, jenis_pakan):
    # Jenis Pakan:
    #    1 = Pelet
    #    2 = Telur
    #    3 = Usus
    #    4 = Cacing
    if kondisi_bibit == "Sehat" and kondisi_kolam == "Baik":
        return "Sangat Baik"
    if kondisi_bibit == "Sehat" and kondisi_kolam == "Cukup Baik":
        if jenis_pakan == 1:
            return "Sangat Baik"
        elif jenis_pakan in [2, 3, 4]:
            return "Baik"
    if kondisi_bibit == "Sehat" and kondisi_kolam == "Buruk":
        return "Baik"
    if kondisi_bibit == "Tidak Sehat" and kondisi_kolam == "Baik":
        if jenis_pakan == 1:
            return "Netral"
        elif jenis_pakan in [2, 3, 4]:
            return "Tidak Baik"
    if kondisi_bibit == "Tidak Sehat" and kondisi_kolam == "Cukup Baik":
        if jenis_pakan in [1, 2]:
            return "Tidak Baik"
        elif jenis_pakan in [3, 4]:
            return "Sangat Tidak Baik"
    if kondisi_bibit == "Tidak Sehat" and kondisi_kolam == "Buruk":
        return "Sangat Tidak Baik"
    return "Tidak Diketahui"

# Exception untuk kesalahan input user
def input_with_validation(prompt, valid_options):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_options:
                return choice
            else:
                print(f"Pilihan tidak valid. Masukkan salah satu dari: {valid_options}")
        except ValueError:
            print("Input harus berupa angka.")

# User Input Menu
print("=== Sistem Pakar Bibit Ikan ===")

bentuk_kepala = input_with_validation("Masukkan bentuk kepala\n 1: Runcing\n 2: Gemuk\n Your input: ", [1, 2])
kelincahan = input_with_validation("Masukkan kelincahan\n 1: Lincah\n 2: Lambat\n Your input: ", [1, 2])
warna_kulit = input_with_validation("Masukkan warna kulit\n 1: Mengkilap\n 2: Buram\n Your input: ", [1, 2])
kecacatan = input_with_validation("Masukkan kecacatan\n 1: Sirip Merah\n 2: Moncong Putih\n 3: Tidak Ada\n Your input: ", [1, 2, 3])

ph_air = input_with_validation("Masukkan pH air\n 1: Tinggi\n 2: Netral\n 3: Rendah\n Your input: ", [1, 2, 3])
suhu = float(input("\nSuhu Air dalam derajat celcius (contoh: 28): "))

jenis_pakan = input_with_validation("Masukkan jenis pakan\n 1: Pelet\n 2: Telur\n 3: Usus\n 4: Cacing\n Your input: ", [1, 2, 3, 4])

# Inference
kondisi_bibit = determine_kondisi_bibit(bentuk_kepala, kelincahan, warna_kulit, kecacatan)
kondisi_kolam = determine_kondisi_kolam(ph_air, suhu)
hasil_keputusan = determine_hasil_keputusan(kondisi_bibit, kondisi_kolam, jenis_pakan)

# Output
print("\n=== Hasil Analisis ===")
print("Kondisi Bibit:", kondisi_bibit)
print("Kondisi Kolam:", kondisi_kolam)
print("Hasil Keputusan:", hasil_keputusan)