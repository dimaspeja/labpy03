modal = 100000000
total_laba = 0

for bulan in range(1, 9):
    if bulan in [1, 2]:
        laba = 0
    elif bulan in [3, 4]:
        laba = modal * 0.01
    elif bulan in [5, 6, 7]:
        laba = modal * 0.05
    elif bulan == 8:
        laba = modal * 0.03
    
    total_laba += laba
    print(f"Laba bulan ke-{bulan} sebesar:Rp.{laba:,.2f}")

print(f"Total laba adalah:Rp.{total_laba:,.2f}")