def reverse_digits(n: int) -> int:
    s = f"{n:02d}"
    return int(s[::-1])

def build_dob_wordlist(dob_chunks):
    dob_set = set(dob_chunks)    
    reversed_set = {reverse_digits(x) for x in dob_set if reverse_digits(x) != x}
    full_set = dob_set | reversed_set  
    wordlist = []
    for a in full_set:
        for b in full_set:
            pin = f"{a:02d}{b:02d}"     
            wordlist.append(pin)
    return wordlist, full_set

if __name__ == "__main__":
    dob_set = {22, 9, 19, 69, 28, 12, 76, 8, 11, 99}
    wordlist, full_set = build_dob_wordlist(dob_set)
    with open("dob_wordlist.txt", "w") as f:
        f.write("\n".join(wordlist))