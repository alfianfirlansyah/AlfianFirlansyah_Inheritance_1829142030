class rumah(object):
   def __init__(self, p, l):
      self.panjang = p
      self.lebar = l

   def hitungluas(self):
      return self.panjang * self.lebar

   def cetakdata(self):
      print("Panjang Rumah\t= ", self.panjang)
      print("Lebar Rumah\t= ", self.lebar)

   def cetakluas(self):
      print("Luas Rumah\t= ", self.hitungluas())

# mendefinisikan kelas turunan (subclass)
class jumlahkamar(rumah):
   def __init__(self, p, l, jk1, jk2):
      # memanggil Kotak.__init__()
      super(jumlahkamar, self).__init__(p, l)
      # menambah atribut baru
      self.jkamar = jk1 + jk2

   def cetakdata(self):
      # memanggil Kotak.cetakData()
      super(jumlahkamar, self).cetakdata()
      print("jumlahkamar\t= ", self.jkamar)

def main():
   # membuat objek KotakWarna
   jumlahkamar1 = jumlahkamar(5, 4, 2, 4)

   # menggunakan objek
   jumlahkamar1.cetakdata()
   jumlahkamar1.cetakluas()

if __name__ == "__main__":
   main()
