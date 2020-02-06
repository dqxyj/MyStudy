# python3
# encoding:utf-8
import random

class Utils:
    @classmethod
    def gaussRand(self, u, s, bound=None, allowMinus=False):
        if bound is None:
            bound = 4 * s
        while True:
            rand = random.gauss(u, s)
            if (rand > u - bound and rand < u + bound):
                if allowMinus:
                    return rand
                elif rand >= 0:
                    return rand

    @classmethod
    def gaussRandInt(self, u, s, bound=None, allowMinus=False):
        rand = self.gaussRand(u, s, bound=bound, allowMinus=allowMinus)
        return int(rand)