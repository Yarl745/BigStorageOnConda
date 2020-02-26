def unique_in_order(iterable):
    if not iterable: return []
    out = [iterable[0]]
    for i in range(1, len(iterable)):
        if out[len(out)-1] != iterable[i]: out.append(iterable[i])
    return out


print(unique_in_order('AAAABBBCCDAABBB'))