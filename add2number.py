import sys
from pathlib import Path

inp_file = Path("_ab.inp")
out_file = Path("_ab.out")

if inp_file.is_file():
    sys.stdin = open(inp_file, "r")

if out_file.is_file():
    sys.stdout = open(out_file, "w")

# --- Code chính ở đây ---
a = int(input())
b = int(input())
print(a + b)
