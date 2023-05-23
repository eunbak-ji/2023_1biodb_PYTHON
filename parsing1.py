#파싱하기

file=open("/home/shared_folder/2_0516/train/data/1_TolC.fa","r")

lines_list=[line for line in  file.readlines()]

#line 읽어내기
#for line in f.readlines():
#   print(line)


# '>'가 있는 것 뽑아 내기
print(lines_list[0],end="")


#기호로 파싱하기
#if ">" in line:
#   comment=line
#else:
#   sequence=line


#염기서열 뽑아 내기
nucleotide=""
cnt=0
for i in lines_list[1]:
    nucleotide += i
    cnt+=1
    if cnt==80:
        print(nucleotide)



        
