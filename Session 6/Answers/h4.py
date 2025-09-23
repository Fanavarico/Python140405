languages = ["Python", "Java", "JavaScript", "C", "Kotlin"]
longest = languages[0]
for lang in languages:
    if len(lang) > len(longest):
        longest = lang
print("Longest language name is:", longest)