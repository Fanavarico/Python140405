# iran -> 2
# usa -> 1
# iraq -> 2
# germany -> 2
country = ["irani", "usa", "iraq", "germany"]
vowels = "aeiouAEIOU"

for keshvar in country:
    # irani
    # usa
    seda = 0
    for harf in keshvar:
        # i r a n i
        # u s a
        if harf in vowels:
            seda += 1
    print(f"Keshvar {keshvar} | Vowels = {seda}")