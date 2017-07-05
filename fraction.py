"""Class practice."""


class Fraction(object):

    def __init__(self, top, bottom):

        self.num = top
        self.dem = bottom

    def __repr__(self):
        return str(self.num) + "/" + str(self.dem)

    def show(self):
        print self.num, "/", self.dem

    @staticmethod
    def gcd(m, n):
        while m % n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n

    def __add__(self, other_fraction):
        newnum = self.num * other_fraction.dem + \
                    self.dem * other_fraction.num
        newdem = self.dem * other_fraction.dem

        common = self.gcd(newnum, newdem)

        return Fraction(newnum/common, newdem/common)
