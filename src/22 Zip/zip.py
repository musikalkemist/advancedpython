compositions = ["the firebird", "another brick in the wall", "fur elise"]
composers = ["igor stravinsky", "pink floyd", "l. v. beethoven"]

combined_structures = zip(compositions, composers)
# print(list(combined_structures))

for c in zip(compositions, composers):
    print(c[0])
    print(c[1])
    print("_______")
