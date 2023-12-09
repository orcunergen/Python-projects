dictin= {
    "Türkiye":"ankara",
    "rusya":"moskova",
    "azerbaycan":"bakü"}
liste =[]
for tuples in dictin.items():
    for x in tuples:
        liste.append(x)
for a in liste:
    print(a)
