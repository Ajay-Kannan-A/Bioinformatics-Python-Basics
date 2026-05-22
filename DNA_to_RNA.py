bp_rule = {
"A":"T",
"T":"A",
"C":"G",
"G":"C"
}
template = input("Enter DNA template:").upper()
t = template.maketrans(bp_rule)
complement = template.translate(t)
transcript = complement.replace("T","U")
print("RNA:", transcript)
