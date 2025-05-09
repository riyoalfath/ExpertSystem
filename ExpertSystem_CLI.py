def tentukan_kondisi_bibit(bentuk_kepala, kelincahan, warna_kulit, kecacatan,
                           cf_bentuk, cf_kelincahan, cf_warna, cf_kecacatan):
    """
    Menilai kesehatan bibit ikan berdasarkan:
    - bentuk kepala (1:Runcing, 2:Gemuk)
    - kelincahan   (1:Lincah,   2:Lambat)
    - warna kulit  (1:Mengkilap,2:Buram)
    - kecacatan    (1:Sirip Merah, 2:Moncong Putih, 3:Tidak Ada)
    Mengembalikan tuple (status, cf_terkoreksi).
    """
    # Kalau ada kecacatan serius → langsung tidak sehat
    if kecacatan in (1, 2):
        return "Tidak Sehat", 0.9 * cf_kecacatan

    # Kulit buram juga menurunkan kesehatan
    if warna_kulit == 2:
        return "Tidak Sehat", 0.8 * cf_warna

    # Kondisi ideal: kepala gemuk, kulit mengkilap, tanpa cacat
    if bentuk_kepala == 2 and warna_kulit == 1 and kecacatan == 3:
        return "Sehat", 0.85 * min(cf_bentuk, cf_warna, cf_kecacatan)

    # Kondisi prima: kepala runcing + lincah + kulit bagus + tanpa cacat
    if bentuk_kepala == 1 and kelincahan == 1 and warna_kulit == 1 and kecacatan == 3:
        return "Sehat", 0.9 * min(cf_bentuk, cf_kelincahan, cf_warna, cf_kecacatan)

    # Kepala runcing tapi lambat → kurang sehat
    if bentuk_kepala == 1 and kelincahan == 2 and warna_kulit == 1 and kecacatan == 3:
        return "Tidak Sehat", 0.75 * min(cf_bentuk, cf_kelincahan, cf_warna, cf_kecacatan)

    return "Tidak Valid", 0.0


def tentukan_kondisi_kolam(ph_air, suhu):
    """
    Menilai kondisi kolam:
    - pH (1:Tinggi,2:Netral,3:Rendah)
    - suhu dalam °C
    """
    # pH ekstrem (terlalu tinggi/rendah)
    if ph_air in (1, 3):
        if 27 <= suhu <= 30:
            return "Cukup Baik", 0.9
        return "Buruk", 0.6

    # pH netral
    if ph_air == 2:
        if 27 <= suhu <= 30:
            return "Baik", 1.0
        return "Cukup Baik", 0.8

    return "Tidak Valid", 0.0


def tentukan_hasil_akhir(kondisi_bibit, kondisi_kolam, jenis_pakan, cf_bibit, cf_kolam):
    """
    Menentukan hasil pertumbuhan berdasarkan:
    - kondisi bibit ("Sehat"/"Tidak Sehat")
    - kondisi kolam ("Baik"/"Cukup Baik"/"Buruk")
    - jenis pakan (1:Pelet,2:Telur,3:Usus,4:Cacing)
    """
    cf_hasil = cf_bibit * cf_kolam

    # Kasus terbaik
    if kondisi_bibit == "Sehat" and kondisi_kolam == "Baik":
        return "Sangat Baik", cf_hasil

    # Bibit sehat + kolam cukup
    if kondisi_bibit == "Sehat" and kondisi_kolam == "Cukup Baik":
        if jenis_pakan == 1:
            return "Sangat Baik", cf_hasil
        return "Baik", cf_hasil

    # Bibit sehat + kolam buruk
    if kondisi_bibit == "Sehat" and kondisi_kolam == "Buruk":
        return "Baik", cf_hasil

    # Bibit tidak sehat + kolam baik
    if kondisi_bibit == "Tidak Sehat" and kondisi_kolam == "Baik":
        if jenis_pakan == 1:
            return "Netral", cf_hasil 
        else:
            "Tidak Baik", cf_hasil

    # Bibit tidak sehat + kolam cukup
    if kondisi_bibit == "Tidak Sehat" and kondisi_kolam == "Cukup Baik":
        if jenis_pakan in (1, 2):
            return "Tidak Baik", cf_hasil
        else:
            return "Sangat Tidak Baik", cf_hasil

    # Bibit tidak sehat + kolam buruk
    if kondisi_bibit == "Tidak Sehat" and kondisi_kolam == "Buruk":
        return "Sangat Tidak Baik", cf_hasil

    return "Tidak Diketahui", 0.0


def input_validasi(prompt, option):
    """Meminta input angka sampai valid sesuai opsi yang disediakan."""
    while True:
        try:
            value = int(input(prompt))
            if value in option:
                return value
            print(f"Pilihan tidak valid, masukkan salah satu: {option}")
        except ValueError:
            print("Input harus berupa angka.")


def input_confident():
    """Meminta tingkat keyakinan dan mengembalikan bobot CF."""
    pilihan = {
        1: 1.0,  # Yakin
        2: 0.8,  # Kurang Yakin
        3: 0.5   # Tidak Yakin
    }
    while True:
        print("Tingkat keyakinan: \n 1=Yakin (1.0)\n 2=Kurang Yakin(0.8)\n 3=Tidak Yakin(0.5)")
        try:
            x = int(input("Pilihan Anda: "))
            if x in pilihan:
                return pilihan[x]
            print("Masukkan 1, 2, atau 3.")
        except ValueError:
            print("Input harus berupa angka.")


def main():
    print("=== Sistem Pakar Bibit Ikan ===")
    bk = input_validasi("Bentuk kepala\n 1:Runcing\n 2:Gemuk\n Jawaban Anda: ", [1, 2])
    cf_bk = input_confident()

    lin = input_validasi("Kelincahan\n 1:Lincah\n 2:Lambat\n Jawaban Anda: ", [1, 2])
    cf_lin = input_confident()

    wk = input_validasi("Warna kulit\n 1:Mengkilap\n 2:Buram\n Jawaban Anda: ", [1, 2])
    cf_wk = input_confident()

    cacat = input_validasi("Kecacatan\n 1:Sirip Merah\n 2:Moncong Putih\n 3:Tidak Ada\n Jawaban Anda: ", [1, 2, 3])
    cf_cacat = input_confident()

    ph = input_validasi("pH air\n 1:Tinggi\n 2:Netral\n 3:Rendah\n Jawaban Anda: ", [1, 2, 3])
    suhu = float(input("Suhu air (°C): "))

    pakan = input_validasi("Jenis pakan\n 1:Pelet\n 2:Telur\n 3:Usus\n 4:Cacing\n Jawaban Anda: ", [1, 2, 3, 4])

    # Proses inferensi
    kondisi_bibit, cf_bibit = tentukan_kondisi_bibit(bk, lin, wk, cacat,
                                                   cf_bk, cf_lin, cf_wk, cf_cacat)
    kondisi_kolam, cf_kolam = tentukan_kondisi_kolam(ph, suhu)
    hasil, cf_hasil = tentukan_hasil_akhir(kondisi_bibit, kondisi_kolam, pakan, cf_bibit, cf_kolam)

    # Tampilkan hasil
    print("\n=== Hasil Analisis ===")
    print(f"Kondisi Bibit : {kondisi_bibit} (Kepastian {cf_bibit*100:.1f}%)")
    print(f"Kondisi Kolam : {kondisi_kolam} (Kepastian {cf_kolam*100:.1f}%)")
    print(f"Rekomendasi   : {hasil} (Kepastian {cf_hasil*100:.1f}%)")


if __name__ == "__main__":
    main()