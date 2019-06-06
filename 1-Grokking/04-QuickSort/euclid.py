def euclid_gcd(a, b):
    if b == 0:
        return a
    else:
        return euclid_gcd(b, a%b) 

a = 1221 
b = 1234567891011121314151617181920212223242526272829

print("GCD: " + str(euclid_gcd(a, b)))

c = 163231
d = 152057

print("GCD: " + str(euclid_gcd(c,d)))