# Fungsi print dapat digunakan untuk menampilkan string atau teks secara langsung
# Ada 3 metode ketika bekerja dengan string
# - menggunakan ' atau dengan "
# - bekerja dengan Raw String
# - menggunakan tanda kutip 3 '''

print('-Bekerja dengan String dengan menggunakan tanda petik (1)')
print("-Bekerja dengan String dengan menggunakan tanda kutip (2)")
print("-Bekerja dengan String bila diperlukan tanda petik \'")
print("-Bekerja dengan String bila diperlukan tanda kutip ganda \"")
print("-Bekerja dengan String bila diperlukan \t tab")
print("-Bekerja dengan String bila diperlukan \\ garis miring")
print("-Bekerja dengan String dengan tipe font dan warna tertentu")
print("\033[6;31;46m -Text biasa dengan warna font merah dan background warna cyan")
# Kode \033 adalah kode ANSI untuk style text
# Kode 1 adalah style
# Warna Text | Kode    | Style Text | Kode  | BG    | Kode |
# Black      | 30      | No Effect  | 0     | Black | 40   |
# Red        | 31      | Bold       | 1     | Red   | 41   |
# Green      | 32      | Underline  | 4     | Green | 42   |
# Yellow     | 33      | Negative-1 | 5     | Yellow| 43   |
# Blue       | 34      | Negative-4 | 7     | Blue  | 44   |
# Purple     | 35      |                    | Purple| 45   |
# Cyan       | 36      |                    | Cyan  | 46   |
# White      | 37      |                    | White | 47   |

# Raw string akan ditampilkan apa adanya
print(r'Teks dengan raw string \n, apapun apakan ditampilkan\\')

# Menggunakan tanda kutip 3
# Tanda kutip digunakan apabila ingin menulis berbaris teks sesuai dengan cara anda menulis kode kode program
print('''\033[0;37;4omHalo
Nama Saya Dheni
Soeryantho''')