def complementary_dna(strand: str) -> str:

    complements: dict[str, str] = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    return "".join([complements[ch] for ch in strand])

## Tests

assert complementary_dna("ACGT") == "TGCA"
assert complementary_dna("ATGCGTACGTTAGC") == "TACGCATGCAATCG"
assert complementary_dna("GGCTTACGATCGAAG") == "CCGAATGCTAGCTTC"
assert complementary_dna("GATCTAGCTAGGCTAGCTAG") == "CTAGATCGATCCGATCGATC"