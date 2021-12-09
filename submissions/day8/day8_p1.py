from collections import Counter


with open('inputs/day8.txt') as file:
    txt = file.read()
    data = [ line.split('|') for line in txt.split('\n') ]


data = [
    [ digit.strip()
      for digit in output.split(' ')
      if digit.isalpha() ]
     for signal, output in data ]


len_to_digit = {
    2: '1',
    3: '7',
    4: '4',
    7: '8'
}

c = Counter()

for i in data:
    for digit in i:
        match len(digit):
            case 2 | 3 | 4 | 7:
                c.update([len_to_digit[len(digit)]])
            case _:
                pass

print(c.total())
breakpoint()