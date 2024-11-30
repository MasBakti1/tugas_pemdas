print("tugas 7")
print("===========")

data_panen = {
    'lokasi1': {
        'nama_lokasi' : 'Kebun A',
        'hasil_panen' : {
            'padi' : 1200,
            'jagung' : 800,
            'kedelai' : 500
        }
    },
    'lokasi2': {
        'nama_lokasi' : 'Kebun B',
        'hasil_panen' : {
            'padi' : 1500,
            'jagung' : 900,
            'kedelai' : 450
        }
    },
    'lokasi3': {
        'nama_lokasi' : 'Kebun C',
        'hasil_panen' : {
            'padi' : 1100,
            'jagung' : 750,
            'kedelai' : 600
        }
    },
    'lokasi4': {
        'nama_lokasi' : 'Kebun D',
        'hasil_panen' : {
            'padi' : 1300,
            'jagung' : 850,
            'kedelai' : 550
        }
    },
    'lokasi5': {
        'nama_lokasi' : 'Kebun E',
        'hasil_panen' : {
            'padi' : 1400,
            'jagung' : 950,
            'kedelai' : 480
        }
    }
}

# menampilkan semua data_panen
for i in data_panen:
    print(data_panen[i]['nama_lokasi'])
    print(data_panen[i]['hasil_panen'])

# menampilkan hasil panen jagung di lokasi B
print(f"hasil panen jagung di {data_panen['lokasi2']['nama_lokasi']} adalah {data_panen['lokasi2']['hasil_panen']['jagung']}")

# menampilkan lokasi dari lokasi3
print(f"lokasi 3 adalah {data_panen['lokasi3']['nama_lokasi']}")

# memasukan jumlah panen padi dan kedelai pada variabel berbeda
padi = 0
kedelai = 0
for i in data_panen:
    padi = padi + data_panen[i]['hasil_panen']['padi']
    kedelai = kedelai + data_panen[i]['hasil_panen']['kedelai']

print (f"jumlah panen padi adalah {padi}")
print (f"jumlah panen kedelai adalah {kedelai}")

# percabangan
for i in data_panen:
    if data_panen[i]['hasil_panen']['padi'] > 1300 or data_panen[i]['hasil_panen']['jagung'] > 800:
        print(f"{data_panen[i]['nama_lokasi']} memerlukan perhatian khusus")
    else:
        print(f"{data_panen[i]['nama_lokasi']} ini dalam keadaan baik")





