import math

def solver(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("VSN")  # vô số nghiệm
            else:
                print("VN")   # vô nghiệm
        else:
            print(-c / b)     # nghiệm bậc 1
        return
    
    delta = b**2 - 4*a*c
    
    if delta == 0:
        print(-b / (2 * a))
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        x1, x2 = sorted([x1, x2])   # đảm bảo x1 <= x2
        print(x1, x2, sep=" ")
    else:
        print("VN")
