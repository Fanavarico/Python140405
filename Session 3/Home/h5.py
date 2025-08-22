# adad 4 raqami begir -> hasel jamesho bego
# 3211 -> 7

# 3211 -> 1  jam
# 321

# 321 -> 1 jam
# 32

# 32 -> 2 jam
# 3

# variable
# amaliat -> jam -> sefr
# A4 --> khali - jam tasir nazari
hasel = 0
adad = 3211

# % 10 --> adad akharo mide
# // 10 --> az adad yeki kam mikone

raqam_4 =  adad % 10  # 1
hasel = hasel + raqam_4 # 0 -> 1
adad = adad // 10 # 321

raqam_3 =  adad % 10  # 1
hasel = hasel + raqam_4 # 1 -> 2
adad = adad // 10 # 32

raqam_2 =  adad % 10  # 2
hasel = hasel + raqam_4 # 2 -> 4
adad = adad // 10 # 3

raqam_1 =  adad % 10  # 3
hasel = hasel + raqam_4 # 4 -> 7
adad = adad // 10 # 0
