def answer(M, F):
    if M == '' or F == '':
        return 'impossible'
    mach = int(M)
    facula = int(F)
    result = solve(mach, facula)
    return result if result == 'impossible' else str(result)

def solve(m, f):
    if m <= 0 or f <= 0:
        return 'impossible'
    if m == 1 or f == 1:
        return f-1 if m == 1 else m-1
    if m > f:
        mul = int(m / f)
        val = m - (f * mul)
        result = solve(val, f)
    elif f > m:
        mul = int(f / m)
        val = f - (m * mul)
        result = solve(m, val)
    else:
        result = 'impossible'
    return result if result == 'impossible' else result + mul
