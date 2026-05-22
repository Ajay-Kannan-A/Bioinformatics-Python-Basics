# Reverse Complement
bp_rule = {
"A":"T",
"T":"A",
"C":"G",
"G":"C"
}
seq_ipt = input("Enter the sequence:")
std_seq_ipt = seq_ipt.upper()
t = std_seq_ipt.maketrans(bp_rule)
complement = std_seq_ipt.translate(t)
print("Complement:", complement)
r_complement = complement[::-1]
print("Reverse Complement:",r_complement)
