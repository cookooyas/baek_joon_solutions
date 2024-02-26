import sys
angle_l=[]
for _ in range(3):
    angle_l.append(int(sys.stdin.readline()))
angle_l.sort()
if sum(angle_l)!=180:
    print("Error")
elif angle_l[1]==angle_l[0] and angle_l[1]==angle_l[2]:
    print("Equilateral")
elif angle_l[1]==angle_l[0] or angle_l[1]==angle_l[2]:
    print("Isosceles")
else:
    print("Scalene")