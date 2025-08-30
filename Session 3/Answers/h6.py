# horofe seda daro toye ye reshte mizarim va age on harf
# toye in reshte bod mishorimesh
text = "this is a simple text and we want to count vowels."
vowels = "aioueAIOUE"
total = 0

for i in text:
    if i in vowels:
        total += 1
print(total)