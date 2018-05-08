from GreatestCommonDivisor import gcd

def diophantine(a, b, c):
  assert c % gcd(a, b) == 0
  d = gcd(a, b)
  p = int(a / d)
  q = int(b / d)

  for x in range(-abs(q),abs(q)+1):
    for y in range(-abs(p),abs(p)+1):
      if a * x + b * y == d:
        return x * c / d , y * c / d
