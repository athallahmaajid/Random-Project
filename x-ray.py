from typing import Iterable, Tuple, TypeVar
import time
start = time.time()

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

def main():
    global data, f
    test_case = data[0]
    result = []

    for i, j in grouped(data[1:]):
        items = [int(x) for x in j.split()]
        ans = [[] for e in range(max(items))]
        for j in range(len(items)):
            for k in range(items[j]):
                ans[k].insert(j, 1)
            l = items[j]
            while l < max(items):
                ans[l].insert(j, 0)
                l += 1

        penanda, akhir, xkali = 0, 0, 0
        for i in range(max(items)):
            xkali = 0
            for j in range(len(items)-1):
                if ans[i][j] == 1 and ans[i][j+1] == 1:
                    penanda = 1
                elif ans[i][j] == 0 and ans[i][j+1] == 1:
                    penanda = 1
                elif ans[i][j] == 1 and ans[i][j+1] == 0:
                    xkali += 1
                    penanda = 0
                else:
                    penanda = 0
            if penanda == 1:
                akhir += 1
            akhir += xkali
        result.append(akhir)
    for o, i in zip(range(1, len(result)+1), result):
        print(f'Case #{o}: {i}')
main()
print(time.time()-start)
