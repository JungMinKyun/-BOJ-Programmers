# 백준 1672 DNA 해독

table = {    
    "AA": "A",
    "AG": "C",
    "AC": "A",
    "AT": "G",
    "GA": "C",
    "GG": "G",
    "GC": "T",
    "GT": "A",
    "CA": "A",
    "CG": "T",
    "CC": "C",
    "CT": "G",
    "TA": "G",
    "TG": "A",
    "TC": "G",
    "TT": "T",
    }

n = int(input())
dna = list(input())

for i in range(n-2, -1, -1):
    dna[i] = table[dna[i] + dna[i+1]]
    dna[i+1] = ""

print(dna[0])