
def execute(dna):
    conversion = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    str = ""
    for c in list(dna):
        str += conversion[c]
    return str
    
