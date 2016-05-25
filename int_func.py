b = lambda x, y: int("".join(reversed([repr(~-0b1) for x in range(y)]+[0x1.__repr__()])), x)

