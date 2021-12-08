import math
import itertools
import random

# job = [1,2,3,4]
# pj = [13,9,13,10]
# dj = [12,37,21,22]
# wj = [2,4,2,5]

job = [1,2,3,4]
pj = [8,12,6,10]
dj = [11,15,9,12]
wj = [2,4,7,6]
Beta = 0.8
k=3
def hammuctieu(congviec):
    C = 0
    T =[]
    MucTieu =0 
    for i in congviec:
        i= i -1
        C += pj[i]
        if C-dj[i]>0:
            T= (C-dj[i])
        else:
            T= 0
        MucTieu += T*wj[i]
    return MucTieu
a = 3
b=1
c=4
d=2
G_s0 = hammuctieu([a,b,c,d])
print("Hàm mục tiêu lời giải ban đầu:",G_s0)

for i in range(k):
    print('\n ---------------------')
    print('Lần thứ',i+1)
    thutu = [[b,a,c,d],[a,c,b,d],[a,b,d,c]]
    print("Hoán vị ",thutu)
    LanCan = []
    for j in thutu:
        LanCan.append(hammuctieu(j))
    G_Sc = min(LanCan)


    print("LanCan",LanCan)
    thamso = LanCan.index(G_Sc)
    # Nếu bộ số mới tốt hơn thì đổi sang bộ số mới
    if G_Sc <= G_s0:
        G_s0=G_Sc
        print(G_s0)
        a = (thutu[thamso])[0]
        b = (thutu[thamso])[1]
        c = (thutu[thamso])[2]
        d = (thutu[thamso])[3]
    else:
        # Nếu bộ số mới không tốt bằng thì có xác xuất chuyển đổi là U
        U = random.uniform(0, 1)
        # 0.8 là hệ số của B, mũ k, k lúc này là i
        P = math.exp((G_s0-G_Sc/(Beta**(i+1))))

        if U>=P:
            # Nếu U>= P (P là xác suất cực kì nhỏ) nên là cực kì khó xảy ra, thì giữ nguyên bộ số cũ, và tiếp tục hoán vij
            # Ở đây hoán bị không có gì thay đổi nên là, vẫn như thế
            # Xác suất ngày càng nhỏ, khả năng kẹt ở đây cực kì lớn
            print("Giá trị G_s0 là:",G_s0)
        else:
            # Nếu may mắn thoát được thì giá trị mới sẽ gán vào S0
            G_s0=G_Sc
            a = (thutu[thamso])[0]
            b = (thutu[thamso])[1]
            c = (thutu[thamso])[2]
            d = (thutu[thamso])[3]
            print("Chuyển đổi vị trí")
            print("Giá trị G_s0 là:",G_s0)
    print("Bộ số S là: ",[a,b,c,d])
else:
    pass


    
