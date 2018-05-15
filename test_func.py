def get_vat(price, vat_rate):
    vat = price / 100 * vat_rate
    price_no_vat = price - vat
    #print(vat)
    #print(price_no_vat)
    return round(price_no_vat, 2)

price = 100
vat_rate = 18

print("Цена без НДС: {}".format(get_vat(price, vat_rate)))