def to_roman(num):
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanNum = ""
    firstVal = None
    index = 0
    while num>0:
        div = num//value[index]
        num = num%value[index]
        while div>0:
            romanNum = romanNum+symbol[index]
            div -= div
        index+=1    

    return romanNum

