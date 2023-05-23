#paried_end_read프로그램 만들기
"""
파일1 3'-5'을 가져온다. 2번째 줄이 서열줄
파일2 5'-3'을 가져온다. 2번째 줄이 서열줄
파일2를 reverse시킨다.
파일2의 sequence를 상보적 서열로 바꾼다. 
파일1과 파일2를 이어붙인다.
"""

#파일 읽기
file1=open("/home/shared_folder/2_0516/train/data/5_paired_end_1.fq","r")
file2=open("/home/shared_folder/2_0516/train/data/6_paired_end_2.fq","r")

cnt1=0
cnt2=0
sequence1=""
sequence2=""
#파일sequence가져오기
for line in file1.readlines():
    cnt1+=1
    if cnt1%2==0:
        sequence1=line.strip()

for line in flie2.readlines():
    cnt2+=1
    if cnt2%2==0:
        sequence2=line.strip()

#sequence2거꾸로 읽기
read2=sequence2[::-1]

#sequence2 상보염기서열 읽기
n={'A':'T','T':'A','C':'G','G':'C'}
n_sequence2=""
for char in read2:
    n_sequence2+=n[char]


single_end=sequence1+n_sequence2
print(single_end)





