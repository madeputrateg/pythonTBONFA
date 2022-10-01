import L1
import L2
import L3


print("Program NFA machine")
intputan = input("1.L1 adalah himpunan semua string yang mengandung prefiks 101 dan panjang string adalah genap\n2.L2 adalah himpunan semua string yang mengandung prefix 101 dan suffiks 00\n3.L3 adalah himpunan semua string yang mengandung suffix 00 dan panjang string adalah kelipatan 3\npilihan:")
match intputan:
    case "1":
        L1.start(input("masukan input string:"))
    case "2":
        L2.start(input("masukan input string:"))
    case "3":
        L3.start(input("masukan input string:"))