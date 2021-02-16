ujian_teori = float(input("Nilai ujian teori: "))
ujian_praktek = float(input("NIlai ujian praktek: "))
pass_grade = 70
a = ujian_teori
b = ujian_praktek
if a >= pass_grade and b >= pass_grade:
    txt = "Selamat, anda lulus!"
elif a >= pass_grade and b < pass_grade:
    txt = "Anda harus mengulang ujian praktek."
elif a < pass_grade and b >= pass_grade:
    txt = "Anda harus mengulang ujian teori."
else:
    txt = "Anda harus mengulang ujian teori dan praktek"

print(txt)

# done
