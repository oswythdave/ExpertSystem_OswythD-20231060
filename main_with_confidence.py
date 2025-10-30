from engine_with_confidence import analisa_metode_belajar_with_confidence

def tanya_pilihan(prompt, pilihan):
    print(f"\n{prompt}")
    for i, p in enumerate(pilihan, 1):
        print(f"{i}. {p.capitalize()}")
    while True:
        try:
            jawab = int(input("Pilih (1/2/3): ").strip())
            if 1 <= jawab <= len(pilihan):
                return pilihan[jawab - 1]
        except ValueError:
            pass
        print("Masukkan angka sesuai pilihan yang tersedia.")

def main():
    print("=== Sistem Pakar Rekomendasi Metode Belajar (Confidence Score) ===")

    tipe_kepribadian = tanya_pilihan("Pilih tipe kepribadian Anda:", ["visual", "auditori", "kinestetik"])
    waktu_belajar = tanya_pilihan("Pilih waktu belajar favorit Anda:", ["pagi", "siang", "malam"])
    kesulitan_belajar = tanya_pilihan("Tingkat kesulitan belajar Anda saat ini:", ["mudah", "sedang", "sulit"])

    data = {
        "tipe_kepribadian": tipe_kepribadian,
        "waktu_belajar": waktu_belajar,
        "kesulitan_belajar": kesulitan_belajar
    }

    print("\nInput Anda:")
    for k, v in data.items():
        print(f"- {k.replace('_', ' ').capitalize()}: {v.capitalize()}")

    print("\nMenganalisis metode belajar yang sesuai...\n")

    # proses analisis
    hasil = analisa_metode_belajar_with_confidence(data)

    # tampilkan hasil
    if hasil:
        print(">> Rekomendasi Metode Belajar:")
        for item in hasil:
            print(f"- {item}")
    else:
        print(">> Tidak ditemukan rekomendasi yang cocok.")

if __name__ == "__main__":
    main()
