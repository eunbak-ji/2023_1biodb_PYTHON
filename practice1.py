"""
작성자 : 박은지
작성일자 :2023년  05월 15일
기능 : open reading frame 프로그램 만들기
작동방법:
    1.dna서열이 주어지면 모두 대문자로 바꾼다.
    2.대문자로 바뀐 서열을 rna서열로 바꾼다.
    3.서열의 0번째, 1번째,2번째 시작되는 순으로 코돈을 읽는다.
"""

#코돈 테이블
codon_table={'UUU':'Phe','UUC':'Phe','UUA':'Leu','UUG':'Leu',
             'UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser',
             'UAU':'Tyr','UAC':'Tyr','UAA':'Stop','UAG':'Stop',
             'UGU':'Cys','UGC':'Cys','UGA':'Stop','UGG':'Trp',
             'CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu',
             'CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
             'CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln',
             'CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg',
             'AUU':'Ile','AUC':'Ile','AUA':'Ile','AUG':'Met',
             'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
             'AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys',
             'AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg',
             'GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val',
             'GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala',
             'GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',
             'GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}

#코돈을 읽을 함수 만들기
def orf_codon1(list_rna):
    orf_result=''
    for i in range(0,len(list_rna),3):
        codon1=RNA[i:i+3]
        if codon1 in codon_table:
            orf1=codon_table.get(codon1)
            orf_result += orf1
    return orf_result


def orf_codon2(list_rna):
    orf_result=''
    for i in range(1,len(list_rna),3):
        codon2=RNA[i:i+3]
        if codon2 in codon_table:
            orf2=codon_table.get(codon2)
            orf_result += orf2
    return orf_result


def orf_codon3(list_rna):
    orf_result=''
    for i in range(2,len(list_rna),3):
        codon3=RNA[i:i+3]
        if codon3 in codon_table:
            orf3=codon_table.get(codon3)
            orf_result += orf3
    return orf_result



dna_seq=input("dna서열을 입력하시오:")
DNA=dna_seq.upper()
if 'T' in DNA:
    RNA=DNA.replace('T','U')

print("--------------------------------------")
print(f"DNA서열:{DNA}")
print(f"RNA서열:{RNA}")
list_rna=list(RNA)
print("-------------<ORF예측 결과>-----------")
print(f"첫번째 예측 결과: {orf_codon1(list_rna)}\n")
print(f"두번째 예측 결과: {orf_codon2(list_rna)}\n")
print(f"세번째 예측 결과: {orf_codon3(list_rna)}\n")


