#fastq파일을 fast파일로 바꾸기

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


re_fast=open("/home/u202114027/re_fast.py","w")
for i in range(len(comment)):
    re_fast.write(f"{comment[i].replace('@','>')}\n")
    re_fast.write(f"{sequence[i]}\n")


