def Info_From_FASTQ(fastq):
    read_count = 0
    comment, sequence = [], []
    result_info = []

    for line in fastq.readlines():
        read_count += 1
        if read_count % 4 == 1: # 1, 5
            comment.append(line.strip())
        elif read_count % 4 == 2: # 2, 6
            sequence.append(line.strip())
    
    for i in range(len(comment)):
        # [[comment1, sequence1], [comment2, sequence2]]
        result_info.append([comment[i], sequence[i]])

    print(result_info)
    return result_info


def FASTA_Write(info, output_path):
    f = open(output_path, 'w')
    for e in info:
        comment = e[0]
        sequence = e[1]
        f.write(f">{comment}\n")
        f.write(f"{sequence}\n")

    return 0


def main():
    input_path = "/home/shared_folder/2_0516/3_sample.fq"
    output_path = "/home/shared_folder/2_0516/example_code/1_output.fa"
    
    fastq = open(input_path, 'r')

    info = Info_From_FASTQ(fastq)

    FASTA_Write(info, output_path)

main()
