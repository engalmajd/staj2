import numpy as np
import matplotlib.pyplot as plt
import heapq
import os
class UltrasonikSensör:
    def __init__(self, konum):
        self.konum = konum
    def engel_algila(self, mesafe):
        return mesafe < 1.0  # Engel algılama eşiği
class OtonomArac:
    def __init__(self, sensörler, ızgara):
        self.sensörler = sensörler
        self.ızgara = ızgara
    def engellerden_kacin(self, sensör_verisi):
        kaçınma_hareketi = False
        for i, sensör in enumerate(self.sensörler):
            if sensör.engel_algila(sensör_verisi[i]):
                print(f"Sensör {i} tarafından {sensör.konum} konumunda engel algılandı.")
                kaçınma_hareketi = True
                self.kaçınma_hareketi_al(sensör.konum)
        # Engel olup olmadığına bakılmaksızın kaçınma hareketi sonrası yol planlaması
        self.yol_planla((0, 0), (4, 4))
    def kaçınma_hareketi_al(self, konum):
        if konum == 'ön':
            print("Önde engel var. Sola dönülüyor.")
        elif konum == 'sol':
            print("Solda engel var. Sağa dönülüyor.")
        elif konum == 'sağ':
            print("Sağda engel var. Sola dönülüyor.")
        else:
            print(f"{konum} konumundaki sensöre göre kaçınma hareketi alınıyor")
    def yol_planla(self, başlangıç, bitiş):
        print(f"{başlangıç} konumundan {bitiş} konumuna yol planlanıyor...")
        yol = a_yildiz(başlangıç, bitiş, self.ızgara)
        print("Yol:", yol)
        if yol:
            self.yolu_gor(yol)
            self.yolu_izgarada_yazdir(yol)  # ASCII kullanarak ızgara gösterimi
        else:
            print("Yol bulunamadı.")
    def yolu_gor(self, yol):
        ızgara = np.array(self.ızgara)
        plt.figure(figsize=(8, 6))
        # Izgarayı çiz
        plt.imshow(ızgara, cmap='Greys', origin='upper')
        # Yolu çiz
        if yol:
            plt.plot([pos[1] for pos in yol], [pos[0] for pos in yol], marker='o', color='red', markersize=5)
            plt.title("Planlanan Yol")
            plt.xlabel("X-ekseni")
            plt.ylabel("Y-ekseni")
        else:
            plt.title("Yol Bulunamadı")

        plt.colorbar(label='Izgara Değeri')

        # Görüntüyü kaydet
        save_path = os.path.join(os.getcwd(), 'yol_cizimi.png')
        plt.savefig(save_path)  # Çizimi dosyaya kaydet
        plt.show()  # Grafiği göster
        print(f"Görsel '{save_path}' olarak kaydedildi")
    def yolu_izgarada_yazdir(self, yol):
        yol_ile_ızgara = [['.' for _ in range(len(self.ızgara[0]))] for _ in range(len(self.ızgara))]

        for pos in yol:
            yol_ile_ızgara[pos[0]][pos[1]] = 'P'

        for row in range(len(self.ızgara)):
            for col in range(len(self.ızgara[row])):
                if self.ızgara[row][col] == 1:
                    yol_ile_ızgara[row][col] = 'X'
        for row in yol_ile_ızgara:
            print(' '.join(row))
class Düğüm:
    def __init__(self, konum, ebeveyn=None):
        self.konum = konum
        self.ebeveyn = ebeveyn
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, diğer):
        return self.f < diğer.f
def a_yildiz(başlangıç, bitiş, ızgara):
    açık_liste = []
    kapalı_liste = set()
    başlangıç_düğümü = Düğüm(başlangıç)
    bitiş_düğümü = Düğüm(bitiş)
    heapq.heappush(açık_liste, başlangıç_düğümü)
    while açık_liste:
        mevcut_düğüm = heapq.heappop(açık_liste)
        kapalı_liste.add(mevcut_düğüm.konum)
        if mevcut_düğüm.konum == bitiş_düğümü.konum:
            yol = []
            while mevcut_düğüm:
                yol.append(mevcut_düğüm.konum)
                mevcut_düğüm = mevcut_düğüm.ebeveyn
            return yol[::-1]
        çocuklar = []
        for yeni_konum in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            düğüm_konumu = (mevcut_düğüm.konum[0] + yeni_konum[0], mevcut_düğüm.konum[1] + yeni_konum[1])

            if düğüm_konumu[0] > (len(ızgara) - 1) or düğüm_konumu[0] < 0 or düğüm_konumu[1] > (
                    len(ızgara[len(ızgara) - 1]) - 1) or düğüm_konumu[1] < 0:
                continue

            if ızgara[düğüm_konumu[0]][düğüm_konumu[1]] != 0:
                continue

            yeni_düğüm = Düğüm(düğüm_konumu, mevcut_düğüm)
            çocuklar.append(yeni_düğüm)
        for çocuk in çocuklar:
            if çocuk.konum in kapalı_liste:
                continue

            çocuk.g = mevcut_düğüm.g + 1
            çocuk.h = ((çocuk.konum[0] - bitiş_düğümü.konum[0]) ** 2) + (
                    (çocuk.konum[1] - bitiş_düğümü.konum[1]) ** 2)
            çocuk.f = çocuk.g + çocuk.h

            if len([i for i in açık_liste if çocuk.konum == i.konum and çocuk.g > i.g]) > 0:
                continue
            heapq.heappush(açık_liste, çocuk)
ızgara = [[0, 1, 0, 0, 0],
          [0, 1, 0, 1, 0],
          [0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0]]
sensörler = [UltrasonikSensör('ön'), UltrasonikSensör('sol'), UltrasonikSensör('sağ')]
arac = OtonomArac(sensörler, ızgara)

sensör_verisi = [0.5, 2.0, 1.5]  # Metre cinsinden
arac.engellerden_kacin(sensör_verisi)
