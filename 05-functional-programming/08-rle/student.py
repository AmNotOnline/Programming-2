def rle_encode(data):
    prev_elem = None
    out = []

    for entry in data:
        if entry != prev_elem:
            out.append((entry, 1))
            prev_elem = entry
        else:
            out[-1] = (entry, out[-1][1] + 1)

    
    return out

def rle_decode(data):
    return [p[0] for p in data for _ in range(p[1])]