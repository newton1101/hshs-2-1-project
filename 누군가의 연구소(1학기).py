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
    for i in range(0, len(EcoRI) - len(pattern)) :
        if EcoRI[i:i+len(pattern)] == pattern : 
            pattern_list.append((i+1, EcoRI[i:i+len(pattern)]))
    return pattern_list

def Limit_enzyme(EcoRI): #제한효소자리 길이를 구하기 위한 리스트 제작
    limit_enzyme_list = []
    for i in range(0, len(EcoRI) - len(pattern)) :
        if EcoRI[i:i+len(pattern)] == pattern : 
            limit_enzyme_list.append((i+1))
            
    base_pair_list = []
    for i in range (0, len(pattern)-2) :
        if len(limit_enzyme_list) == 0 or 1:
            base_pair_list.append(len(EcoRI))
        else :
            base_pair_list.append(limit_enzyme_list[i+1]-limit_enzyme_list[i]) #제한효소 부착자리 개수에 따른 절편의 길이 구하기
            base_pair_list.append(len(EcoRI) - (limit_enzyme_list[-1] - limit_enzyme_list[0])) #제한효소 절편들중 세어지지 않은 절편 1개 셈
    return base_pair_list

pattern = (input('사용할 제한효소의 염기서열을입력해주세요.').upper())

y = cke(EcoRI, pattern)
z = Limit_enzyme(EcoRI)
for s in range(len(y)):    
    print(y[s][0],'번째 염기서열에',y[s][1],'의 제한효소 부착자리가 존재')
    print(str(z)[s][0],'bp')
if len(y) == 0:
    print('그런거없다')
    
