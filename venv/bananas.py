
from itertools import combinations

s = "bbananana"


def bananas(s) -> set:
    result = set()
    result_word = "banana"
    for index in combinations(range(len(s)), len(s) - len(result_word)):
        temp_list = list(s)
        for j in index:
            temp_list[j] = "-"
        temp_str = "".join(temp_list)
        if temp_str.replace("-", "") == result_word:
            result.add(temp_str)
    return result


print(bananas(s))


assert bananas("banann") == set()
assert bananas("banana") == {"banana"}
assert bananas("bbananana") == {"b-an--ana", "-banana--", "-b--anana",
                                "b-a--nana", "-banan--a", "b-ana--na",
                                "b---anana", "-bana--na", "-ba--nana",
                                "b-anan--a", "-ban--ana", "b-anana--"}
assert bananas("bananaaa") == {"banan-a-", "banana--", "banan--a"}
assert bananas("bananana") == {"ban--ana", "ba--nana", "bana--na",
                               "b--anana", "banana--", "banan--a"}