list_A = [1,2,21,4,5,6,7,8,9,10]
print("2 phan tu dau tien la {}".format(list_A[:2]))
print("2 phan tu cuoi cung la {}".format(list_A[-2:]))
print("So luong phan tu cua A:",len(list_A))
print("Tong cac phan tu cua A:",sum(list_A))
print("Gia tri lon nhat cua A:",max(list_A))
print("Gia tri nho nhat cua A:",min(list_A))
print("Trung binh cong cua A:",sum(list_A)/len(list_A))
list_A.sort()
print("List thu tu tang dan:",list_A)
list_A.reverse()
print("List thu tu giam dan:",list_A)