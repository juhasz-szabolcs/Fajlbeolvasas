nyelvek = []
with open('feladat/Timeline_of_programming_languages.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)  # fejléc átugrása
    next(forrasfajl)  # fejléc átugrása
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nyelv = {'year': int(adatok[0]), 'programming language': adatok[1], 'first name': adatok[2], 'last name': adatok[3]}
        nyelvek.append(nyelv)

# print(f'{nyelvek=}')
legfiatalabb_nyelv = nyelvek[0]
legidosebb_nyelv = nyelvek[0]
for sor in nyelvek:
    if sor['year'] > legfiatalabb_nyelv['year']:
        legfiatalabb_nyelv = sor
    if sor['year'] < legidosebb_nyelv['year']:
        legidosebb_nyelv = sor

print(f'A legfiatalabb programozási nyelv: {legfiatalabb_nyelv["programming language"]}, amelyet {legfiatalabb_nyelv["year"]}-ben hoztak létre {legfiatalabb_nyelv["first name"]} {legfiatalabb_nyelv["last name"]} vezető fejlesztő által.')
print(f'A legidősebb programozási nyelv: {legidosebb_nyelv["programming language"]}, amelyet {legidosebb_nyelv["year"]}-ben hoztak létre {legidosebb_nyelv["first name"]} {legidosebb_nyelv["last name"]} vezető fejlesztő által.')