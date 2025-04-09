# polynomial hash
# take a look at the implementation of the polynomial hash


class Polynomial:
    def __init__(self, string, base, mod):
        self.string = string
        self.base = base
        self.mod = mod
        self.length = len(string)
        self.prefix_hash, self.base_power = self.get_hash()

    def get_hash(self):
        prefix_hash = [0] * (self.length + 1)
        base_power = [1] * (self.length + 1)

        for x in range(1, self.length + 1):
            base_power[x] = (base_power[x - 1] * self.base) % self.mod

        for i in range(self.length):
            prefix_hash[i + 1] = (
                prefix_hash[i] + ord(self.string[i]) * base_power[i]
            ) % self.mod
        return prefix_hash, base_power

    # take a look at this function
    def substring_hash(self, left, right):
        substingHash = (
            self.prefix_hash[right + 1] - self.prefix_hash[left] + self.mod
        ) % self.mod
        return substingHash


string = "faate"
poly = Polynomial(string, 31, 10**9 + 7)
print(poly.get_hash())
print(poly.substring_hash(1, 3))
