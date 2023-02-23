""""Прикольное задание от codewars:
перевести число в Римский формат, а затем вернуть назад"""

def to_roman(val):

    thousands=['','M','MM','MMM']
    hundreds=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    tens=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    number=['','I','II','III','IV','V','VI','VII','VIII','IX']


    a=thousands[val//1000]
    b=hundreds[val//100%10]
    c=tens[val//10%10]
    d=number[val%10]
    return (a+b+c+d)

chislo=int(input('enter the number from 1 to 3999:  '))

while chislo>3999 or chislo<=0:
    chislo=int(input('enter the number from 1 to 3999:  '))

a=to_roman(int(chislo))
print(a)


def from_roman(roman_num):
    out = 0
    past_number = 0
    for num in map(lambda x: {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}[x], roman_num[::-1]):
        if num >= past_number:
            out += num
            past_number = num
        else:
            out -= num

    return out

out=from_roman(a)
print(out)