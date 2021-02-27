print('hallo cat')
x = 3
x = 4
simba = "Kater"
print(x)
length_sim = len(simba)
print(f"de lengte van simba is {length_sim}")
print(f"Mijn kater is {x}"+"Simba")
for i in range(x):
    print(i)
    print(f"Mijn kater is {x+i} jaar")
for i in range(len(simba)):
    print(i)

anna_list = ["aap","noot","mies"]
print(anna_list)
for word in anna_list:
    print(word)
    for letter in word:
        print(letter)
for i in range(3):
    print(i)
print(f"de broer van mijn kat heet{simba}")
print(f"de broer van mijn kat is"+f" {simba}"+" hij is"+f" {i}")
cijfer_lijst = [1,2,3,4,4,3,2,1,7,"banaan", "banaan"]
for k in cijfer_lijst:
    print(f"het getal is {k}")
x = set(cijfer_lijst) 
print(x)
x.add(100)
print(x)
#kat = {"harry":"eten","brokjes","staart","kattebak"}
kat = {"harry":["eten","brokjes","staart"], 
       "simba":["staart","kussentje","rat"]}
print(f"{kat}")
print(kat.values())
print(kat.keys())
print(kat["simba"])
kat["harry"].append("muis")
print(f"De kat.values zijn: {kat.values()}")
print(f" de kat.keys zijn k {kat.keys()}")
kat ["dodo"] ="brokjes"
hond = {}
print("hond is een lege dictonary")
print (kat,hond)


print("hier")
for k in range(2):
    if "hallo" not in hond:
        hond["hallo"] = "blaf"
        print("check",k)
    else: 
        print("zit er al in")
        print(k)    
print(hond)

def plantagefunctie():
    """hij print iets"""
    kater = 5
    print(kater)

def nwefunction(plantagefunctie):
    print(kater)
    print(f"ken ik {kater}?") 
    
nwefunction()
