ds = []

def addsv(id ,name):
    id = input("nhap ma sinh vien: ")
    name = input("nhap ho va ten sinh vien: ")
    sv = (id, name)
    ds.append(sv)
    print("them sinh vien thanh cong!")

def remove():
    id  = input("nhap ma sinh vien can xoa: ")
    for sv in ds:
        if sv[0] == id:
            ds.remove(sv)
            print("Xoa sinh vien thanh cong")
            return
        print("Khong tim thay sinh vien can xoa.")

def inds():
    for sv in ds:
        print(f"Ma sinh vien: {sv[0]}, Ho va ten: {sv[1]}")

id = int
name = chr

while True:
    print ("---Trinh Quan ly Lop (alpha 0.1.1)---")
    print ("1. them sinh vien")
    print ("2. xoa sinh vien")
    print ("3. in danh sach lop")
    print ("4. thoat")

    choice = int(input("moi ban chon: "))

    if choice == 1:
        addsv(id, name)
    elif choice == 2:
        remove()
    elif choice == 3:
        inds()
    elif choice == 4:
        break
    else:
        print ("SYNTAX ERROR! - moi ban nhap tu 1-4.")