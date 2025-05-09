# Input rule 1, kondisi bibit ikan
def determine_kondisi_bibit(bentuk_kepala, kelincahan, warna_kulit, kecacatan,
                             cf_bentuk_kepala, cf_kelincahan, cf_warna_kulit, cf_kecacatan):
    # Kecacatan:
    #    1 = Sirip Merah
    #    2 = Moncong Putih
    #    3 = Tidak Ada
    if kecacatan in [1, 2]:
        return "Tidak Sehat", 0.9 * cf_kecacatan
    
    # Warna Kulit:
    #    1 = Mengkilap
    #    2 = Buram
    if warna_kulit == 2:
        return "Tidak Sehat", 0.8 * cf_warna_kulit
    
    # Bentuk Kepala:
    #    1 = Runcing
    #    2 = Gemuk
    if bentuk_kepala == 2 and warna_kulit == 1 and kecacatan == 3:
        return "Sehat", 0.85 * min(cf_bentuk_kepala, cf_warna_kulit, cf_kecacatan)
    
    # Kelincahan:
    #    1 = Lincah
    #    2 = Lambat
    if bentuk_kepala == 1 and kelincahan == 1 and warna_kulit == 1 and kecacatan == 3:
        return "Sehat", 0.9 * min(cf_bentuk_kepala, cf_kelincahan, cf_warna_kulit, cf_kecacatan)
    
    if bentuk_kepala == 1 and kelincahan == 2 and warna_kulit == 1 and kecacatan == 3:
        return "Tidak Sehat", 0.75 * min(cf_bentuk_kepala, cf_kelincahan, cf_warna_kulit, cf_kecacatan)

    return "Tidak Valid", 0.0

# Input rule 2, kondisi kolam ikan
def determine_kondisi_kolam(ph_air, suhu):
    # pH Air:
    #    1 = Tinggi
    #    2 = Netral
    #    3 = Rendah
    if ph_air in [1, 3]:  # 1: Tinggi, 2: Netral, 3: Rendah
        if 27 <= suhu <= 30:
            return "Cukup Baik", 0.9
        else:
            return "Buruk", 0.6

    # Suhu Air:
    #    Int, contoh: 27.5, 28, 30
    if ph_air == 2:  # Netral
        if 27 <= suhu <= 30:
            return "Baik", 1.0
        else:
            return "Cukup Baik", 0.8
    return "Tidak Valid", 0.0

# Input rule 3, kondisi pertumbuhan ikan
def determine_hasil_keputusan(kondisi_bibit, kondisi_kolam, jenis_pakan, cf_bibit, cf_kolam):
    cf_hasil = cf_bibit * cf_kolam
    
    if kondisi_bibit == "Sehat" and kondisi_kolam == "Baik":
        return "Sangat Baik", cf_hasil
    
    # Jenis Pakan:
    #    1 = Pelet
    #    2 = Telur
    #    3 = Usus
    #    4 = Cacing
    if kondisi_bibit == "Sehat" and kondisi_kolam == "Cukup Baik":
        if jenis_pakan == 1:
            return "Sangat Baik", cf_hasil
        elif jenis_pakan in [2, 3, 4]:
            return "Baik", cf_hasil
        
    if kondisi_bibit == "Sehat" and kondisi_kolam == "Buruk":
        return "Baik", cf_hasil
    
    if kondisi_bibit == "Tidak Sehat" and kondisi_kolam == "Baik":
        if jenis_pakan == 1:
            return "Netral", cf_hasil
        elif jenis_pakan in [2, 3, 4]:
            return "Tidak Baik", cf_hasil
        
    if kondisi_bibit == "Tidak Sehat" and kondisi_kolam == "Cukup Baik":
        if jenis_pakan in [1, 2]:
            return "Tidak Baik", cf_hasil
        elif jenis_pakan in [3, 4]:
            return "Sangat Tidak Baik", cf_hasil
        
    if kondisi_bibit == "Tidak Sehat" and kondisi_kolam == "Buruk":
        return "Sangat Tidak Baik", cf_hasil
    return "Tidak Diketahui", 0.0

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

# faktor keyakinan user
def input_confidence():
    print("Masukkan tingkat keyakinan:")
    print(" 1: Yakin (1.0)")
    print(" 2: Kurang Yakin (0.8)")
    print(" 3: Tidak Yakin (0.5)")
    while True:
        try:
            c = int(input(" Pilihan keyakinan Anda: "))
            if c == 1:
                return 1.0
            elif c == 2:
                return 0.8
            elif c == 3:
                return 0.5
            else:
                print("Pilihan tidak valid. Masukkan 1, 2, atau 3.")
        except ValueError:
            print("Input harus berupa angka.")

# Input
print("=== Sistem Pakar Bibit Ikan ===")

bentuk_kepala = input_with_validation("Masukkan bentuk kepala\n 1: Runcing\n 2: Gemuk\n Your input: ", [1, 2])
cf_bentuk_kepala = input_confidence()
kelincahan = input_with_validation("Masukkan kelincahan\n 1: Lincah\n 2: Lambat\n Your input: ", [1, 2])
cf_kelincahan = input_confidence()
warna_kulit = input_with_validation("Masukkan warna kulit\n 1: Mengkilap\n 2: Buram\n Your input: ", [1, 2])
cf_warna_kulit = input_confidence()
kecacatan = input_with_validation("Masukkan kecacatan\n 1: Sirip Merah\n 2: Moncong Putih\n 3: Tidak Ada\n Your input: ", [1, 2, 3])
cf_kecacatan = input_confidence()

ph_air = input_with_validation("Masukkan pH air\n 1: Tinggi\n 2: Netral\n 3: Rendah\n Your input: ", [1, 2, 3])
suhu = float(input("\nSuhu Air dalam derajat celcius (contoh: 28): "))

jenis_pakan = input_with_validation("Masukkan jenis pakan\n 1: Pelet\n 2: Telur\n 3: Usus\n 4: Cacing\n Your input: ", [1, 2, 3, 4])

# Inference
kondisi_bibit, cf_bibit = determine_kondisi_bibit(
    bentuk_kepala, kelincahan, warna_kulit, kecacatan,
    cf_bentuk_kepala, cf_kelincahan, cf_warna_kulit, cf_kecacatan
)
kondisi_kolam, cf_kolam = determine_kondisi_kolam(ph_air, suhu)
hasil_keputusan, cf_hasil = determine_hasil_keputusan(kondisi_bibit, kondisi_kolam, jenis_pakan, cf_bibit, cf_kolam)

# Output
print("\n=== Hasil Analisis ===")
print("Kondisi Bibit:", kondisi_bibit, f"(Kepastian: {cf_bibit * 100:.1f}%)")
print("Kondisi Kolam:", kondisi_kolam, f"(Kepastian: {cf_kolam * 100:.1f}%)")
print("Hasil Keputusan:", hasil_keputusan, f"(Kepastian: {cf_hasil * 100:.1f}%)")