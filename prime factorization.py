# this program show how to prim factorize a given number and from that how to find the total
# number of divisor of that given number
# if a number N = (a^p)*(b^q)*(c^r).....
# then total number of divisor of N is (p+1)*(q+1)*(r+1)*.....


def factorization(n):
    for i in range(2, n + 1):
        if n / i == 1:
            return {i: 1}
        else:
            if n % i == 0:
                get_dicti = factorization(int(n / i))
                if i not in get_dicti:
                    get_dicti[i] = 1
                else:
                    get_dicti[i] += 1

                return get_dicti


print(factorization(42))
total_divisor = 1
for ele in factorization(42).values():
    total_divisor *= (ele + 1)

print(total_divisor)
