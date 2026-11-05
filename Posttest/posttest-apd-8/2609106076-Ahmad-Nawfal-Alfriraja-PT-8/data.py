users = {
    "admin": {"password": "admin76", "role": "admin"},
    "steve": {"password": "steve123", "role": "user"}
}

kategori = ("Any% Random Seed", "Any% Set Seed", "All Achievements", "Glitchless")

runs = {
    1: {"pemain": "Steve", "kategori": "Any% Set Seed", "menit": 9, "detik": 58, "pengirim": "steve"},
    2: {"pemain": "Clementdav", "kategori": "Any% Random Seed", "menit": 9, "detik": 22, "pengirim": "Clementdav"},
    3: {"pemain": "Dream", "kategori": "Any% Random Seed", "menit": 19, "detik": 24, "pengirim": "Dream"},
    4: {"pemain": "Herobrine", "kategori": "Any% Random Seed", "menit": 1, "detik": 11, "pengirim": "admin"}
}

id_berikut = 5


def buat_id_baru():
    global id_berikut
    id_baru = id_berikut
    id_berikut += 1
    return id_baru
