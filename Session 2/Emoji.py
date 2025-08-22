# Uni codes
real_codes = ["\U0001F600", "\U0001F603", "\U0001F604", "\U0001F601", "\U0001F606", "\U0001F605", "\U0001F923", "\U0001F602", "\U0001F642",
         "\U0001F643", "\U0001F609", "\U0001F60A", "\U0001F607", "\U0001F970", "\U0001F60D", "\U0001F929", "\U0001F618", "\U0001F617",
         "\U0001F61A", "\U0001F619", "\U0001F60B", "\U0001F61B", "\U0001F61C", "\U0001F92A", "\U0001F61D", "\U0001F911", "\U0001F917",
         "\U0001F92D", "\U0001F92B", "\U0001F914", "\U0001F910", "\U0001F928", "\U0001F610", "\U0001F611", "\U0001F636", "\U0001F60F",
         "\U0001F612", "\U0001F644", "\U0001F62C", "\U0001F925", "\U0001F60C", "\U0001F614", "\U0001F62A", "\U0001F924", "\U0001F634",
         "\U0001F634", "\U0001F637", "\U0001F912", "\U0001F915", "\U0001F922"]
# Remove same parts
code_names = ["F600", "F603", "F604", "F601", "F606", "F605", "F923", "F602", "F642",
         "F643", "F609", "F60A", "F607", "F970", "F60D", "F929", "F618", "F617",
         "F61A", "F619", "F60B", "F61B", "F61C", "F92A", "F61D", "F911", "F917",
         "F92D", "F92B", "F914", "F910", "F928", "F610", "F611", "F636", "F60F",
         "F612", "F644", "F62C", "F925", "F60C", "F614", "F62A", "F924", "F634",
         "F634", "F637", "F912", "F915", "F922"]

# Combine them into one variable
combine = list(zip(real_codes, code_names))
# Information's
print(r"All codes satart with --> \U0001")
# Loop through them all
for i in combine:
    print(i)
# Heart emoji
print("\u2764\uFE0F", r"Code is --> \u2764\uFE0F")