nyelvek = []
with open('feladat/Timeline_of_programming_languages.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)  # fejléc átugrása
    next(forrasfajl)  # fejléc átugrása
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nyelv_ev = int(adatok[0])
        nyelv_nev = adatok[1]
        nyelv_fejleszto_keresztnev = adatok[2]
        nyelv_fejleszto_vezeteknev = adatok[3]
        nyelvek.append([nyelv_ev, nyelv_nev, nyelv_fejleszto_keresztnev, nyelv_fejleszto_vezeteknev])

# print(f'{nyelvek=}')
legfiatalabb_nyelv = nyelvek[0]
# print(legfiatalabb_nyelv)
for nyelv in nyelvek:
    if nyelv[0] > legfiatalabb_nyelv[0]:
        legfiatalabb_nyelv = nyelv
print(f"{legfiatalabb_nyelv=}")
print(f"Legfiatalabb nyelv: {legfiatalabb_nyelv[0]}, {legfiatalabb_nyelv[1]}, , {legfiatalabb_nyelv[2]}")