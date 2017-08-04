def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

# print (get_length('ATCGAT'))
# print (get_length('ATCG'))

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return dna1 > dna2

# print (is_longer('ATCG', 'AT'))
# print (is_longer('ATCG', 'ATCGGA'))

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    nucleotide_count = 0
    for nucl in dna:
        if nucl in nucleotide:
            nucleotide_count += 1

    return nucleotide_count

# print (count_nucleotides('ATCGGC', 'G'))
# print (count_nucleotides('ATCTA', 'G'))

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

# print (contains_sequence('ATCGGC', 'GG'))
# print (contains_sequence('ATCGGC', 'GT'))

def is_valid_sequence(dna):
    """ (str) -> bool
    
    Return True if and only if the DNA sequence is valid. That is, it contains 
    no characters other than '𝙰', '𝚃', '𝙲' and '𝙶'.

    >>> is_valid_sequence('ATCGGC'):
    True
    >>> is_valid_sequence('ATFPQ'):
    False

    """
    for char in dna:
        if char not in "ATCG":
            return False
    return True

# print (is_valid_sequence('ATCGGC'))
# print (is_valid_sequence('ATFPQ'))

def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    
    Return the DNA sequence obtained by inserting the second DNA sequence into 
    the first DNA sequence at the given index.
    
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('GCGA', 'CT', 1)
    'GCTCGA'

    """
    return dna1[:index] + dna2 + dna1[index:]

#print (insert_sequence('CCGG', 'AT', 2))
#print ('CCATGG')
#print (insert_sequence('GCGA', 'CT', 1))
#print ('GCTCGA')

def get_complement(dna_nucleotide):
    """ (str) -> str
    
    Return the nucleotide's complement. 

    >>> get_complement('A')
    T
    >>> get_complement('T')
    A
    """

    if char == 'A':
        return 'T'
    elif char == 'T':
        return 'A'
    elif char == 'C':
        return 'G'
    elif char == 'G':
        return 'C'

def get_complementary_sequence(dna_sequence):
    """ (str) -> str
    
    Return the DNA sequence that is complementary to the given DNA sequence. 

    >>> get_complementary_sequence('ACGTACG')
    TGCATGC
    >>> get_complementary_sequence('TGCATGC')
    ACGTACG
    """
    complementary_sequence = ''

    for char in dna_sequence:
        if char == 'A':
            complementary_sequence += 'T'
        elif char == 'T':
            complementary_sequence += 'A'
        elif char == 'C':
            complementary_sequence += 'G'
        elif char == 'G':
            complementary_sequence += 'C'

    return complementary_sequence
        
# print (get_compiment_sequence('ACGTACG'))
# print ('TGCATGC')
# print (get_compiment_sequence('TGCATGC'))
# print ('ACGTACG')
