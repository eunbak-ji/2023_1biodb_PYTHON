#card db다루기 
"""
sequence와 coomment를 따로 파일로 저장
단, 파일명은 gene name으로
"""
input_path='/home/shared_folder/2_0516/card_database_v3.2.5.fasta'
output_path='/home/u202114027/subject2/output'

def Card_to_single():
    #carddb에서 comment와 sequence따로 분리시키기
    comment=[]
    sequence=[]
    f=open(input_path,"r")
    for line in f.readlines():
        if ">"in line:
            comment.append(line.strip())
        else:
            sequence.append(line.strip())
    file_name_list = []
    #파일이름 파싱해서 설정하기
    for char in comment:
        file_name=char.split("|")[2][5:].replace("/","_")
        file_name_list.append(file_name)

    #파일을 각각 저장하기
    #zip을 이용할 시, 여러변수를 한번에 for문으로 돌릴 수 있다.
    for c,k,s in zip(comment,file_name_list,sequence):
        new_name = output_path + '/' + k + '.fa'
        f = open(new_name,'w')
        f.write(c+'\n')
        f.write(s)
        f.close()
    return 0


def main():
    Card_to_single()
    return 0 

main()
