import sys
from pathlib import Path

inp_file = Path("_ab.inp")
out_file = Path("_ab.out")

if inp_file.is_file():
    sys.stdin = open(inp_file, "r")

if out_file.is_file():
    sys.stdout = open(out_file, "w")

# --- Code chính ở đây ---
n = int(input())

res = 1;

if (n & 1):
    for i in range(1, n+1, 2):
        res *= i
        i += 2
    print(n, "!! = ", res, sep = "")
else: 
    for i in range(2, n+1, 2):
        res *= i
        i += 2
    print(n, "!! = ", res, sep = "")