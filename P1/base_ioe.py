#base_ioe.py
import sys
'''
print("Hello, World")
sys.stdout.write("Hello, World\n")
print("Hello")

print("Ini error")
sys.stderr.write("yang ini baru error")

username = input("masukkan nama")
print("username")

'''

print("Masukkan alamat:")
alamat = sys.stdin.readline()
print(alamat)

print("Deskripsi: ")
deskripsi = sys.stdin.read(30)
#deskripsi = sys.stdin.readlines()
print(deskripsi)
