def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return (len(dna))

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find(dna2) > 0:
        return True

    return False


def is_valid_sequence(dna):
    ''' (str) -> bool
    Return True if and only if the DNA squence is valid (contains only A T C G)
    >>>is_valid_sequence('ATCG')
    True
    >>>is_valid_sequence('QRACG')
    False
    '''
    
    for i in dna:
        if i in 'ATCG':
            return True
        else:
            return False


def insert_sequence(str1, str2, index):
    ''' (str, str, int) - str
    Return the DNA sequence 'str1' after inserting 'str2' at the 'index' given
    >>> insert_sequence ('CCGGAA', 'TT', 2)
    CCTTGGAA
    >>> insert_sequence ('ABCDEF', 'QQ', -2)
    ABCDQQEF
    '''
    return str1[:index] + str2 + str1[index:]


def get_complement(nucleotide):
    ''' (str) -> str
    Return the nucleotide's complement. 
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'
    else:
        return False
    

def get_complementary_sequence(seq):
    ''' (str) -> str
    Return the DNA sequence that is complimenatary to the DNA sequence.
    >>>get_complementary_sequence('TA')
    'AT'
    >>> get_complementary_sequence('GC')
    'CG'
    '''

    cs = ''
    for i in seq:
        
        cs = cs + get_complement(i)

    return cs

