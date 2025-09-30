import sys
import math
from pathlib import Path

inp_file = Path("_ab.inp")
out_file = Path("_ab.out")

if inp_file.is_file():
    sys.stdin = open(inp_file, "r")

if out_file.is_file():
    sys.stdout = open(out_file, "w")

# --- Code chính ở đây ---
a = float(input().strip())
b = float(input().strip())
c = float(input().strip())

if (a + b <= c or
    a + c <= b or
    b + c <= a):
    print("INVALID")
else:
    perimeter = a + b + c    
    p = perimeter / 2
    area = (p * (p - a) * (p - b) * (p - c))
    area = area ** 0.5
    print("S = ", area, "C = ", perimeter)
    
