def complementary_strand_find(dna_strand):
    complementary=""
    for base in dna_strand:
        if base=="A":
            complementary+="T"
        elif base=="T":
            complementary+="A"
        elif base=="C":
            complementary+="G"
        elif base=="G":
            complementary+="C"
        else:
            print("wrong input")
            complementary=None
            break
    return complementary

if __name__=="__main__":
    dna_strand="CGTATACGGT"
print("dna strand is",dna_strand)
print("complementary",complementary_strand_find(dna_strand))
