### Mistakes
1. I assumed the problem to be a DP problem without carefully thinking about the problem.
2. Due to some reason I thought that I have to write `sum` and `difference` functions for string on my own.

## Takesways
1. The problem became so easy when I realized I could solve it from reverse.
2. If m >> f, then no need to subtract f again and again from m. We can directly do `m-f*(int(m/f))`.
3. As java also have BigInteger, so its OK to take advantage of arbitrary length of int in python.
