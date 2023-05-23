def main():
    input_path = "/home/shared_folder/2_0516/train/data"
    paired_1 = open(f"{input_path}/5_paired_end_1.fq", 'r')
    paired_2 = open(f"{input_path}/6_paired_end_2.fq", 'r')

    ############################################################
    seq_1 = ""
    seq_2 = ""

    count = 0
    for line in paired_1.readlines():
        count += 1 
        if count == 2:
            seq_1 = line.strip()

    count = 0
    for line in paired_2.readlines():
        count += 1 
        if count == 2:
            seq_2 = line.strip()
    
    ###########################################################

    dictionary = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
    
    new_seq_2 = ""
    for alpha in seq_2[::-1]:
        new_seq_2 += dictionary[alpha]
    
    single_end_read = seq_1 + new_seq_2
    print(single_end_read)

    ###########################################################

    single = open(f"{input_path}/single_end.fastq", 'w')
    single.write("@Train single end fastq file format\n")
    single.write(f"{single_end_read}\n")
    single.write("+Quality\n")
    single.write("XXXXXXXXXXXXXXXXX\n")
    return 0

main()
