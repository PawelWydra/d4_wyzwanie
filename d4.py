#
# * Mikołaj postanowił w tym roku skorzytać z pomocy nowoczesnych technologii
# * i zamiast rozwozić wszystkie prezenty, niektóre przesłać przez Internet.
# * Do tego celu musi zamienić nazwy prezentów w strumienie bitów!
# * Pomoż Mikołajowi! Przygotuj kod, który zamieni nazwy prezentów na ciąg zer i jedynek.
# * Dla każdej litery nazwy prezentu znajdz kod UTF-8, a później zamień go na system binarny.
# * Dla każdego prezentu wypisz na ekran ciąg zer i jedynek. Każdy prezent w oddzielnej linijce.
# * Możesz napisać funkcję zamieniającą numer znaku na system binarny samodzielnie,
# * albo znaleźć odpowiednią funkcję w bibliotece Twojego języka.
# */
def gift(gift_name):
    string_to_utf = bytearray(gift_name, "utf8")
    utf_to_binary = [(bin(letter))[2:] for letter in string_to_utf]
    gift_in_binary = " ".join(utf_to_binary)
    return print(f"{gift_in_binary}")


list_of_presents = ["Parfum", "Socks", "Sweather", "Cup",
         "Hat", "Tea", "Coffee", "Clock", "Bag",
         "Book", "Wallet", "Cream", "Earrings"]

for _ in list_of_presents:
    gift(_)