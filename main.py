nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]


class FlatIterator:

    def __init__(self, list):
        self.list = self.unpacking_list(list)

    def unpacking_list(self, array):
        lst = []
        for i in array:
            if isinstance(i, list):
                lst.extend(self.unpacking_list(i))
            else:
                lst.append(i)
        return lst

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.list) == 0:
            raise StopIteration

        return self.list.pop(0)


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
       print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)