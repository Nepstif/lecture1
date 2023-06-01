import math

primesL = [2, 5, 7]
limit = 700


def count_find_num(primesL, limit):
    list_of_numbers = list()
    sum = math.prod(primesL)


    if sum <= limit:
        list_of_numbers.append(math.prod(primesL))
        length_primesL = len(primesL)
        index = 0
        count = 1


        while True:
            temp = primesL.copy()
            temp.insert(index, primesL[index] ** count)

            if math.prod(temp) <= limit:
                list_of_numbers.append(math.prod(temp))
                count += 1
            elif math.prod(temp) >= limit:
                temp.clear()
                count = 1
                index += 1

            if index >= length_primesL:
                break
        return [len(list_of_numbers), max(list_of_numbers)]
    else:
        return []


print(count_find_num(primesL, limit))









