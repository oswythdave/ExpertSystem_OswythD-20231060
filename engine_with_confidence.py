def analisa_metode_belajar_with_confidence(data):
    tipe = data.get('tipe_kepribadian')
    waktu = data.get('waktu_belajar')
    kesulitan = data.get('kesulitan_belajar')

    hasil = []
    confidence = 0

    # --- Logika sederhana berbasis aturan ---
    if tipe == 'visual':
        hasil.append("Belajar lewat video interaktif atau mind map")
        confidence += 40
    elif tipe == 'auditori':
        hasil.append("Belajar melalui diskusi kelompok atau mendengarkan rekaman")
        confidence += 40
    elif tipe == 'kinestetik':
        hasil.append("Belajar melalui praktik langsung dan simulasi")
        confidence += 40

    if waktu == 'pagi':
        hasil.append("Gunakan waktu pagi untuk materi yang membutuhkan fokus tinggi")
        confidence += 30
    elif waktu == 'malam':
        hasil.append("Gunakan malam untuk review dan latihan ringan")
        confidence += 25
    elif waktu == 'siang':
        hasil.append("Gunakan siang untuk belajar kolaboratif atau diskusi online")
        confidence += 20

    if kesulitan == 'mudah':
        hasil.append("Coba tingkatkan level materi agar tetap menantang")
        confidence += 10
    elif kesulitan == 'sedang':
        hasil.append("Gunakan metode campuran: video + latihan soal")
        confidence += 15
    elif kesulitan == 'sulit':
        hasil.append("Gunakan bantuan tutor, belajar kelompok, dan latihan soal rutin")
        confidence += 25

    # Batasi confidence maksimum 100%
    confidence = min(confidence, 100)

    hasil.append(f"Tingkat keyakinan rekomendasi: {confidence}%")

    return hasil
