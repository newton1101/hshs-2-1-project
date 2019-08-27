
# coding: utf-8

# In[3]:


EcoRI = 'TTAACCTATAAAAATAGGCGTATCACGAGGCAGAATTTCAGATAAAAAAAATCCTTAGCTTTCGCTAAGG' +'ATGATTTCTGGAATTCGCGGCCGCTTCTAGAGTTGACGGCTAGCTCAGTCCTAGGTACAGTGCTAGCTAC' +'TAGAGAAAGAGGAGAAATACTAGATGGCCGGCGCACGCAACGCGACCAATAAGCTCCTGCACAAAGCGAA' +'AAAAAGCAAAAGCGATGAGTTTTATACCCAGTATTGCGACATTGAAAACGAATTACAATACTACCGCGAA' +'CATTTCAGCGATAAGGTTGTGTACTGCAACTGTGATGACCCGCGTGTGAGCAATTTTTTTAAATATTTCG' +'CGGTGAACTTTGACAACCTCGGACTGAAGAAGCTGATTGCAAGCTGTTATGTAGAAAACAAGGAGGGCTT' +'TAGCTCCAGCGAAGCAGCAAAAAATGGCTTTTACTATGAATACCATAAAGAAAACGGCAAAAAACTGGTC' +'TTCGATGATATTTCGGTGAGTAGCTTCTGTGGCGACGGAGATTTTCGGAGCAGTGAAAGCATTGATCTGC' +'TCAAAAAAAGTGATATCGTGGTCACGAACCCGCCTTTTTCACTCTTTCGTGAATACTTAGATCAACTTAT' +'TAAATACGATAAAAAGTTCCTTATCATCGCCAATGTAAACAGCATTACTTATAAAGAAGTGTTTAATCTG' +'ATCAAAGAAAACAAGATCTGGCTGGGAGTACATTTAGGCCGGGGTGTGAGTGGCTTCATCGTTCCAGAAC' +'ATTACGAACTGTACGGCACCGAGGCCCGCATTGATTCAAATGGAAACCGTATTATCAGCCCGAATAACTG' +'TCTGTGGCTGACGAACCTTGACGTCTTCATTCGCCACAAAGACCTGCCGTTAACACGTAAATACTTTGGA' +'AACGAAAGCTCGTAC'

def comp(EcoRI):  #상보적 염기서열
    comp_dict={'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    EcoRI_comp=""
    for char in EcoRI:
        if char in comp_dict:
            EcoRI_comp = EcoRI_comp + comp_dict[char]
    return EcoRI_comp
 
def rev(EcoRI): #역순 염기서열
    comp_dict={'A':'A', 'T':'T', 'C':'C', 'G':'G'}
    rev_str = "".join(reversed(EcoRI))
    EcoRI_rev = ""
    for char in rev_str:
        if char in comp_dict:
            EcoRI_rev = EcoRI_rev + comp_dict[char]
    return EcoRI_rev

def cke(EcoRI, pattern): #제한효소자리 검사
    pattern_list = []
    if len(pattern)!=len(comp(pattern)): #염기서열 오류 검사
        print('염기서열의 일부(전부)가 ATCG로 이루어지지 않았습니다.')
        return '찡긋' #?????????
    
    else:
        for i in range(0, len(EcoRI) - len(pattern)) :
            if EcoRI[i:i+len(comp(pattern))] == comp(pattern) :

                pattern_list.append((i+1, EcoRI[i:i+len(comp(pattern))]))    
        return pattern_list
pattern =(input('사용할 제한효소의 염기서열을입력해주세요.').upper())
i = cke(EcoRI, pattern)
print(i)

