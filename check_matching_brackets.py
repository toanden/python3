""" def check_matchingBrackets(mystring):
    check_on = True
    brackets = "()[]{}<>"
    barckets_srting = "".join([x for x in mystring if x in brackets])
    while any(x in barckets_srting for x in ["()", "[]", "<>", "{}"] ):
        for brachet in ["()", "[]", "<>", "{}"]:
            barckets_srting = barckets_srting.replace(brachet, "")
    if not len(barckets_srting):
        return 1
    return 0 """

""" def check_matchingBrackets(mystring):
    matching = 1
    check_on = True
    brackets = "()[]{}<>"
    barckets_srting = "".join([x for x in mystring if x in brackets])

    while check_on:
        for brachet in ["()", "[]", "<>", "{}"]:
            if brachet in barckets_srting:

                barckets_srting = barckets_srting.replace(brachet, "")

        if not any(x in barckets_srting for x in ["()", "[]", "<>", "{}"] ):
            check_on = False
            if len(barckets_srting):

                matching = 0
    return matching """

""" def check_matchingBrackets(mystring):
    matching = 0
    check_on = True
    brackets = "()[]{}<>"
    barckets_srting = "".join([x for x in mystring if x in brackets])
    count = len(barckets_srting)
    while count:
        for brachet in ["()", "[]", "<>", "{}"]:
            if brachet in barckets_srting:
                barckets_srting = barckets_srting.replace(brachet, "")
        if count > len(barckets_srting):
            count = len(barckets_srting)
        else:
            break
    if not len(barckets_srting):
        matching = 1
    return matching 

print(check_matchingBrackets("(a+[b*c]-{d/3})"), end=" ")
print(check_matchingBrackets("(a + [b * c) - 17]"), end=" ")
print(check_matchingBrackets("(((a * x) + [b] * y) + c"), end=" ")
print(check_matchingBrackets("auf(zlo)men [gy<psy>] four{s}"), end=" ") """
brackets = "()[]{}<>"
mystring = "auf(zlo)men [gy<psy>] four{s}"
barckets_srting = "".join([x for x in mystring if x in brackets])
print([x in barckets_srting for x in ["()", "{}", "<>", "[]"]])