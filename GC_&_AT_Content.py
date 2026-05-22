# GC and AT content
seq = input("Enter DNA sequence:").upper()
g = seq.count("G")
c = seq.count("C")
gc_content = ((g+c)*100)/len(seq)
at_content = 100-gc_content
print(f"GC content: {gc_content:.2f}%")
print(f"AT content: {at_content:.2f}%")
