
# coding: utf-8

# In[3]:


EcoRI = 'TTAACCTATAAAAATAGGCGTATCACGAGGCAGAATTTCAGATAAAAAAAATCCTTAGCTTTCGCTAAGG' +'ATGATTTCTGGAATTCGCGGCCGCTTCTAGAGTTGACGGCTAGCTCAGTCCTAGGTACAGTGCTAGCTAC' +'TAGAGAAAGAGGAGAAATACTAGATGGCCGGCGCACGCAACGCGACCAATAAGCTCCTGCACAAAGCGAA' +'AAAAAGCAAAAGCGATGAGTTTTATACCCAGTATTGCGACATTGAAAACGAATTACAATACTACCGCGAA' +'CATTTCAGCGATAAGGTTGTGTACTGCAACTGTGATGACCCGCGTGTGAGCAATTTTTTTAAATATTTCG' +'CGGTGAACTTTGACAACCTCGGACTGAAGAAGCTGATTGCAAGCTGTTATGTAGAAAACAAGGAGGGCTT' +'TAGCTCCAGCGAAGCAGCAAAAAATGGCTTTTACTATGAATACCATAAAGAAAACGGCAAAAAACTGGTC' +'TTCGATGATATTTCGGTGAGTAGCTTCTGTGGCGACGGAGATTTTCGGAGCAGTGAAAGCATTGATCTGC' +'TCAAAAAAAGTGATATCGTGGTCACGAACCCGCCTTTTTCACTCTTTCGTGAATACTTAGATCAACTTAT' +'TAAATACGATAAAAAGTTCCTTATCATCGCCAATGTAAACAGCATTACTTATAAAGAAGTGTTTAATCTG' +'ATCAAAGAAAACAAGATCTGGCTGGGAGTACATTTAGGCCGGGGTGTGAGTGGCTTCATCGTTCCAGAAC' +'ATTACGAACTGTACGGCACCGAGGCCCGCATTGATTCAAATGGAAACCGTATTATCAGCCCGAATAACTG' +'TCTGTGGCTGACGAACCTTGACGTCTTCATTCGCCACAAAGACCTGCCGTTAACACGTAAATACTTTGGA' +'AACGAAAGCTCGTAC'

def comp(vector):  #상보적 염기서열
    comp_dict={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    vector_comp=""
    for char in vector:
        if char in comp_dict:
            vector_comp = vector_comp + comp_dict[char]
    return vector_comp
 
def rev(vector): #역순 염기서열
    comp_dict={'A':'A', 'T':'T', 'C':'C', 'G':'G'}
    rev_str = "".join(reversed(vector))
    vector_rev = ""
    for char in rev_str:
        if char in comp_dict:
            vector_rev = vector_rev + comp_dict[char]
    return vector_rev

def cke(vector, pattern): #제한효소자리 검사
    pattern_list = []
    for i in range(0, len(vector) - len(pattern)) :
        if vector[i:i+len(pattern)] == pattern : 
            pattern_list.append((i+1, vector[i:i+len(pattern)]))
    for i in range(0, len(vector) - len(pattern)) :
        if vector[i:i+len(pattern)] == pattern : 
            pattern_list.append((i+1, vector[i:i+len(pattern)]))
    return pattern_list

vector = str(input('enter sequence of your vector').upper())
pattern = comp(input('사용할 제한효소의 염기서열을입력해주세요.').upper())
i = cke(vector, pattern)
print(i)

