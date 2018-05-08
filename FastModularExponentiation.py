def FastModularExponentiation(b, e, m):
  c = b
  output = 1
  while e > 0:
      if e % 2 == 1:
          output = (c * output) % m
          e = e - 1
      e = e // 2
      c = (c * c) % m
  return output
