def ana_to_square_feet(ana):
    # 1 Ana = 342.25 square feet
    return ana * 342.25

def bigga_to_square_feet(bigga):
    # 1 Bigga = 13.69 square feet
    return bigga * 13.69

def pisa_to_square_feet(pisa):
    # 1 Pisa = 507.33 square feet
    return pisa * 507.33

def ropani_to_square_feet(ropani):
    # 1 Ropani = 5476 square feet
    return ropani * 5476

# Conversion examples
ana = 5
bigga = 10
pisa = 2
ropani = 1

ana_sq_feet = ana_to_square_feet(ana)
bigga_sq_feet = bigga_to_square_feet(bigga)
pisa_sq_feet = pisa_to_square_feet(pisa)
ropani_sq_feet = ropani_to_square_feet(ropani)

print(f"{ana} Ana is equal to {ana_sq_feet:.2f} square feet.")
print(f"{bigga} Bigga is equal to {bigga_sq_feet:.2f} square feet.")
print(f"{pisa} Pisa is equal to {pisa_sq_feet:.2f} square feet.")
print(f"{ropani} Ropani is equal to {ropani_sq_feet:.2f} square feet.")
