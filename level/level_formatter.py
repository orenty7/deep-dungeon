def format_level(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    lines = list(filter(lambda s: s != '', map(str.strip, lines)))
    width, height = map(int, lines[0].split())
    player_pos = map(int, lines[1].split())

    lines = list(map(str.split, lines[2::]))

    max_ = 0
    for row in lines:
        for tile in row:
            max_ = max(len(tile), max_)

    fstr = '{:' + str(max_) + 's}'


    out = open(filepath, 'w')
    print(width, height, file=out)
    print(*player_pos, file=out)
    for row in lines:
        for tile in row:
            print(fstr.format(tile), end=' ', file=out)
        print(file=out)


format_level('levels/level01.txt')
format_level('levels/level02.txt')
format_level('levels/level03.txt')
format_level('levels/level04.txt')
format_level('levels/level05.txt')
format_level('levels/level06.txt')
format_level('levels/level07.txt')
format_level('levels/level08.txt')
format_level('levels/level09.txt')