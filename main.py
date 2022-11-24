class ExponentiationMethods:
    def __init__(self, base, power):
        self.base = base
        self.power = power
        self.multiplication_count = 0

    def binary_exponentiation(self):
        two_power_list = [int(d) for d in bin(self.power)[2:]][::-1]

        n_powers = [1, self.base]
        multiplications = len(two_power_list) - 1

        for m in range(multiplications):
            n_powers.append(n_powers[-1] ** 2)

        self.multiplication_count += multiplications

        first_non_zero_index = [0 != two_power_list[i] for i in range(len(two_power_list))].index(True) + 1

        result = n_powers[first_non_zero_index]

        for i, power in enumerate(two_power_list[first_non_zero_index:]):
            if power:
                result *= n_powers[i+1+first_non_zero_index]
                self.multiplication_count += 1

        return result, self.multiplication_count

    def efficient_exponentiation(self, n):
        pass


print(ExponentiationMethods(2, 10).binary_exponentiation())
