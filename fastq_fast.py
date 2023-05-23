#fastQ 파일을 fast파일로 바꾸기
#주석은 항상 첫번째
#염기서열은 두번째
f=open("/home/shared_folder/2_0516/train/data/3_sample.fq","r")

cnt=0
comment=[]
sequence=[]

for line in f.readlines():
    cnt+=1
    if cnt%4==1:
        comment.append(line.strip())
    elif cnt%4==2:
        sequence.append(line.strip())

#print(comment)
#print(sequence)

fast=open("/home/u202114027/fast.py","w")
for i in range(len(comment)):
    fast.write(f"{comment[i].replace('@','>')}\n")
    fast.write(f"{sequence[i]}\n")





