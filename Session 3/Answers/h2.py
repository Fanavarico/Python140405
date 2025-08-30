# adadi avale ke be qeyre khodesh va 1 be chizi bakhsh
# pazir nabashe.
# inja man migam beyne bazeh 2 ta yeki kamtar az khode adad
# age be hichi bakhsh pazir nabod avale, yani 1 va khodesh
# ro hesab nemikonam.

adad = int(input("Adad bego : "))
maqsom_elaih = 0

for i in range(2, adad):
    if adad % i == 0:
        maqsom_elaih += 1

if maqsom_elaih != 0:
    print("Adad = ", adad, "Aval Nist !")
else:
    print("Adad = ", adad, "Aval Hast !!!")