author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
newlist = author.sort(key=lambda name: name.split(" ")[-1].lower())
print(newlist)