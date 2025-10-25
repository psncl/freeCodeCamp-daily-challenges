# Complementary DNA

https://www.freecodecamp.org/learn/daily-coding-challenge/2025-10-25

Given a string representing a DNA sequence, return its complementary strand using the following rules:

- DNA consists of the letters `"A"`, `"C"`, `"G"`, and `"T"`.
- The letters `"A"` and `"T"` complement each other.
- The letters `"C"` and `"G"` complement each other.

For example, given `"ACGT"`, return `"TGCA"`.

## Tests

1. `complementary_dna("ACGT")` should return `"TGCA"`.
1. `complementary_dna("ATGCGTACGTTAGC")` should return `"TACGCATGCAATCG"`.
1. `complementary_dna("GGCTTACGATCGAAG")` should return `"CCGAATGCTAGCTTC"`.
1. `complementary_dna("GATCTAGCTAGGCTAGCTAG")` should return `"CTAGATCGATCCGATCGATC"`.
