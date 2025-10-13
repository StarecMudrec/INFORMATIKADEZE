def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx]); idx += 1
    M = int(data[idx]); idx += 1
    K = int(data[idx]); idx += 1
    
    first_occupied = [M + 1] * (K + 2)  # 1..K
    occupied_in_row = [set() for _ in range(M + 1)]
    
    for _ in range(N):
        r = int(data[idx]); idx += 1
        s = int(data[idx]); idx += 1
        if r < first_occupied[s]:
            first_occupied[s] = r
        occupied_in_row[r].add(s)
    
    for r in range(M, 0, -1):
        for s in range(K - 1, 0, -1):
            if first_occupied[s] >= r and first_occupied[s + 1] >= r:
                if s not in occupied_in_row[r] and (s + 1) not in occupied_in_row[r]:
                    print(r, s + 1)
                    return

if __name__ == "__main__":
    solve()