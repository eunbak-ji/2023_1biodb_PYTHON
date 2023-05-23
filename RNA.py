#rna끝에서 3개 슬라이싱 하기
#UGGC서열이 존재하는 지 확인
#RNA길이와 길이 평균 출력
RNA1="AAUGGCAUAGCGUAG"
RNA2="AUGGCGCCCUAG"
RNA3="AUGGCGUAA"

def slicing():
    for i in range(1,4):
        print(f"{RNA(i)}[-1,-3]")
    return 0

def check():
    for i in range(1,4):
        if UGGC in RNA(i):
            print("True")
        else:
            print("False")
    return 0

def length():
    for i in range(1,4):
        print(f"len{RNA(i)}")
    return 0

def main():
    slicing()
    check()
    length()
    mean=(len(RNA1)+len(RNA2)+len(RNA3))/3
    print(mean)


main()
