"""Logika CRUD run dan pemeringkatan."""

import data
import tampilan
import utils


def pilih_kategori():
    tampilan.tampilkan_kategori()
    pilihan = input("Pilih kategori: ").strip()
    try:
        nomor = int(pilihan)
        if 1 <= nomor <= len(data.kategori):
            return data.kategori[nomor - 1]
        utils.galat("Nomor kategori di luar jangkauan!")
    except ValueError:
        utils.galat("Kategori harus berupa angka!")
    return None


def run_milik(role, username):
    """Daftar ID run yang boleh diubah/dihapus oleh user."""
    bisa = []
    for id_run in data.runs:
        if role == "admin" or data.runs[id_run]["pengirim"] == username:
            bisa.append(id_run)
    return bisa


def urutkan_ranking(daftar_id):
    """Bubble sort berdasarkan total detik (terkecil = peringkat teratas)."""
    for i in range(len(daftar_id)):
        for j in range(len(daftar_id) - i - 1):
            a = data.runs[daftar_id[j]]
            b = data.runs[daftar_id[j + 1]]
            if utils.ke_detik(a["menit"], a["detik"]) > utils.ke_detik(b["menit"], b["detik"]):
                daftar_id[j], daftar_id[j + 1] = daftar_id[j + 1], daftar_id[j]
    return daftar_id


def tambah_run(username):
    utils.bersihkan_layar()
    utils.judul("TAMBAH RUN")
    pemain = input("Nama pemain: ").strip()
    if pemain == "":
        utils.galat("Nama pemain tidak boleh kosong!")
    else:
        nama_kat = pilih_kategori()
        if nama_kat is not None:
            try:
                menit = int(input("Waktu - menit: ").strip())
                detik = int(input("Waktu - detik: ").strip())
                if menit < 0 or detik < 0 or detik > 59:
                    utils.galat("Menit tidak boleh negatif, detik harus 0-59!")
                elif utils.ke_detik(menit, detik) == 0:
                    utils.galat("Waktu tidak boleh 00:00!")
                else:
                    id_run = data.buat_id_baru()
                    data.runs[id_run] = {
                        "pemain": pemain,
                        "kategori": nama_kat,
                        "menit": menit,
                        "detik": detik,
                        "pengirim": username
                    }
                    utils.sukses("Run berhasil ditambahkan!")
            except ValueError:
                utils.galat("Menit dan detik harus berupa angka bulat!")
    utils.tunggu()


def lihat_ranking():
    utils.bersihkan_layar()
    utils.judul("RANKING SPEEDRUN")
    nama_kat = pilih_kategori()
    if nama_kat is not None:
        tampil = [i for i in data.runs if data.runs[i]["kategori"] == nama_kat]
        urutkan_ranking(tampil)

        print()
        utils.peringatan(f"Ranking kategori: {nama_kat}")
        if len(tampil) == 0:
            utils.peringatan("Belum ada data run pada kategori ini.")
        else:
            tampilan.tampilkan_ranking(tampil)
    utils.tunggu()


def ubah_run(role, username):
    utils.bersihkan_layar()
    utils.judul("UBAH RUN")
    bisa = run_milik(role, username)

    if len(bisa) == 0:
        utils.peringatan("Tidak ada data yang dapat diubah.")
    else:
        tampilan.tampilkan_tabel_run(bisa)
        try:
            idx = int(input("ID run yang diubah: ").strip())
            if idx in bisa:
                menit_lama = data.runs[idx]["menit"]
                detik_lama = data.runs[idx]["detik"]
                print("Kosongkan input jika tidak ingin mengubah.")

                baru = input(f"Pemain [{data.runs[idx]['pemain']}]: ").strip()
                if baru != "":
                    data.runs[idx]["pemain"] = baru

                ubah_kat = input(f"Ubah kategori [{data.runs[idx]['kategori']}]? (y/n): ").strip().lower()
                if ubah_kat == "y":
                    kat_baru = pilih_kategori()
                    if kat_baru is not None:
                        data.runs[idx]["kategori"] = kat_baru
                    else:
                        utils.peringatan("Kategori tidak diubah.")

                menit_baru = input(f"Menit [{data.runs[idx]['menit']}]: ").strip()
                if menit_baru != "":
                    try:
                        if int(menit_baru) < 0:
                            utils.galat("Menit tidak boleh negatif, tidak diubah.")
                        else:
                            data.runs[idx]["menit"] = int(menit_baru)
                    except ValueError:
                        utils.galat("Menit harus angka, tidak diubah.")

                detik_baru = input(f"Detik [{data.runs[idx]['detik']}]: ").strip()
                if detik_baru != "":
                    try:
                        if 0 <= int(detik_baru) <= 59:
                            data.runs[idx]["detik"] = int(detik_baru)
                        else:
                            utils.galat("Detik harus 0-59, tidak diubah.")
                    except ValueError:
                        utils.galat("Detik harus angka, tidak diubah.")

                if utils.ke_detik(data.runs[idx]["menit"], data.runs[idx]["detik"]) == 0:
                    data.runs[idx]["menit"] = menit_lama
                    data.runs[idx]["detik"] = detik_lama
                    utils.galat("Waktu tidak boleh 00:00, waktu dikembalikan.")
                utils.sukses("Proses update selesai.")
            else:
                utils.galat("ID tidak valid atau bukan milik Anda!")
        except ValueError:
            utils.galat("ID harus berupa angka!")
    utils.tunggu()


def hapus_run(role, username):
    utils.bersihkan_layar()
    utils.judul("HAPUS RUN")
    bisa = run_milik(role, username)

    if len(bisa) == 0:
        utils.peringatan("Tidak ada data yang dapat dihapus.")
    else:
        tampilan.tampilkan_tabel_run(bisa)
        try:
            idx = int(input("ID run yang dihapus: ").strip())
            if idx in bisa:
                yakin = input(f"Hapus run {data.runs[idx]['pemain']}? (y/n): ").strip().lower()
                if yakin == "y":
                    data.runs.pop(idx)
                    utils.sukses("Run berhasil dihapus!")
                else:
                    utils.peringatan("Penghapusan dibatalkan.")
            else:
                utils.galat("ID tidak valid atau bukan milik Anda!")
        except ValueError:
            utils.galat("ID harus berupa angka!")
    utils.tunggu()
