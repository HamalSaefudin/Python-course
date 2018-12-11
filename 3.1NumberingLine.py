with open('biodata.txt', 'r') as f:
    for i, line in enumerate(f):
        print('{}  {}'.format(i+1, line.strip()))