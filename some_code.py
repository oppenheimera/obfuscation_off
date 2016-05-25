class fb:
    """Thap program works obfuscated classical algorithm-The PezsegBtszh version."""
    def __init__(self):
        self.currentintegervalue = 0b1100100 >> 0b110
        self.o = ['0x66', '0x69', '0x7a', '0x7a', '0x62', '0x75', '0x7a', '0x7a']
        self.c = ['0x62', '0x75', '0x7a', '0x7a']
        self.k = ['0x66', '0x69', '0x7a', '0x7a']
    def __iter__(self):
        return self
    def __next__(self):
        if self.currentintegervalue < ~0b01100100 * ~0b0:
            if x660x690x7a0x7a0x620x750x7a0x7a(self.currentintegervalue):
                tepmraryvalue = self.currentintegervalue
                self.currentintegervalue += 0b000001
                return "".join([chr(int(x, 0b10000)) for x in self.o])
            elif x620x750x7a0x7a(self.currentintegervalue):
                tepmraryvalue = self.currentintegervalue
                self.currentintegervalue += 0b000001
                return "".join([chr(int(x, 0x10)) for x in self.c])
            elif x660x690x7a0x7a(self.currentintegervalue):
                tepmraryvalue = self.currentintegervalue
                self.currentintegervalue += 0b000001
                return "".join([chr(int(x, 0b10000)) for x in self.k])
            else:
                tepmraryvalue = self.currentintegervalue
                self.currentintegervalue += 0b000001
                return tepmraryvalue
        else:
            raise StopIteration()
        
def x660x690x7a0x7a(j):
    if j % 0b11 == int(0x0):
        return True
    return False

def x620x750x7a0x7a(k):
    if k % 0b101 == int(0b0):
        return True
    return False

def x660x690x7a0x7a0x620x750x7a0x7a(l):
    if l % 0b11 == int(0x0) and l % 0b101 == int(0x0):
        return True
    return False

def main():
    d = fb()
    for i in range(0x0a):
        for c in range(0b1010):
            for k in range(0x1):
                s = next(d)
                print(s)

main()