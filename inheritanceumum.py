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
      self.panjang = p
      self.lebar = l
      self.jkamarlt1 = jk1
      self.jkamarlt2 = jk2
   def jkamar(self):
      return self.jkamarlt1 + self.jkamarlt2
   def cetakdata(self):
      print("Panjang Rumah\t= ", self.panjang)
      print("Lebar Rumah\t= ", self.lebar)
      print("Jumlah Kamar\t= ", self.jkamar())

def main():
   # membuat objek jumlah kamar
   jumlahkamar1 = jumlahkamar( 5, 4, 2 ,4 )
   jumlahkamar1.cetakdata()
   jumlahkamar1.cetakluas()

if __name__ == "__main__":
   main()
