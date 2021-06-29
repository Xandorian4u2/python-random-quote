f = open("quotes.txt")
quote = f.readlines()
f.close()
print(list(range(len(quote))))
