from typing import Iterable, Tuple, TypeVar

T = TypeVar("T")

def grouped(iterable: Iterable[T], n=2) -> Iterable[Tuple[T, ...]]:
    """s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), ..."""
    return zip(*[iter(iterable)] * n)

def count_words(filepath):
    with open(filepath) as f:
        data = f.read()
        data.replace(",", " ")
        return data.split("\n")

input_file = input('input file path: ')
data = count_words(input_file)[:-1]

test_case = data[0]
print('')
if int(test_case) > 1000:
    pass
else:
    result = []
    for i, j in grouped(data[1:]):
        res = [int(x) for x in j.split() if int(x) > 0]
        result.append(sum(res))
        print('')

    for item, number in zip(result, range(1, len(result)+1)):
        print(f'Case #{number}: {item}')