# python 2.6
#Program on The Football Fest from HACKER EARTH
kases = int(raw_input())
for k in range(kases):
    b = map(int, raw_input().split())
    n = int(b[0])
    count = 0
    passes = [b[1]]
    for i in range(n):
        inp = map(str, raw_input().split())
        pass_type = inp[0]
        if pass_type == 'P':
            if count % 2 == 1:
                passes.pop()
                count -= 1
            player_ID = int(inp[1])
            passes.append(player_ID)
        if pass_type == 'B' and i != n:
            count += 1
        if pass_type == 'B' and i == n-1 and count % 2 == 1:
            passes.pop()





    print 'Player %d' % passes[-1]

