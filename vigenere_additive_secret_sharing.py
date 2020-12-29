import re
import random

# Support function
def print_return(x):
    print(x)
    return x

### Integer section

# Strech integers list
def stretch(K, l):
    assert(len(K) < l)
    streched_K = []
    for i in range(0,l):
        streched_K.append(K[i % len(K)])
    return streched_K

# Sum integers lists
def sum_int(A, B, is_B_negative = False):
    if len(B) < len(A):
        B = stretch(B, len(A))
    elif len(B) > len(A):
        A = stretch(A, len(B))
    return [(a + b) % 26 if not is_B_negative else (a - b) % 26 for a,b in zip(A,B)]

# Compute shares of an integer
def share_single_int(a, n):
    S = [random.randint(0,25) for i in range(0,n-1)]
    return S + [(a - sum(S)) % 26]
 
# Compute shares of an integers list   
def share_int(A, n):
    return [share_single_int(a, n) for a in A]

### String section

def char_to_int(c):
    return ord(c.lower()) - 97

def int_to_char(i):
    return chr(i + 97)

# Convert string to integers list
def string_to_int(S):
    return [char_to_int(s) for s in S]

# Convert integers list to string
def int_to_string(I):
    return [int_to_char(i) for i in I]

# Sum strings
def sum_string(A, B, is_B_negative = False):
    return "".join(int_to_string(sum_int(string_to_int(A),string_to_int(B), is_B_negative)))

# Compute shares of a string
def share_string(A, n):
    partial1 = [[int_to_char(s) for s in S] for S in share_int(string_to_int(A), n)]
    partial2 = [[S[i] for S in partial1] for i in range(0,n)]
    partial3 = ["".join(S) for S in partial2]    
    return " + ".join(partial3)
     
# Compute [A] + [B] - [C] + ... based on the parsed values 
def comp_exp(EXP):
    print("".join([str(e) if e != '+' and e != '-' else ' ' + e + ' ' for e in EXP]))
    if len(EXP) == 1:
        return EXP[0]
    else:
        ARG1 = EXP[0]
        ARG2 = EXP[2]
        if EXP[1] == '+':
            RES = sum_string(ARG1, ARG2)
        elif EXP[1] == '-':
            RES = sum_string(ARG1, ARG2, True)
        return comp_exp([RES] + EXP[3:])

while True:
    exp = input("Insert expression: ")
    # Syntax for sharing a secret:
    # share [A] [n]
    if exp.startswith("share"):
        print('Shares: ' + str(share_string(exp.split()[1],int(exp.split()[2]))))
    # Syntax for summing and subtracting strings (eventually shares) according to the scheme:
    # [A] + [B] - [C] + ... 
    else:
        EXP = re.split('([+|-])',exp.replace(' ',''))
        RES = comp_exp(EXP)
        print('Result: ' + str(RES))

