import time, sys


def readtext(filepath):
    """"Lazy read each line """
    with open(filepath, 'r') as data:
        while True:
            line = data.readline().rstrip('\n').split(',')
            if len(line) > 1:
                yield line
            else:
                break

start_time = time.time()
filepath = sys.argv[1]
result_file = open(sys.argv[2], 'w')
top_cost_drug = dict()

try:
    for id, ln, fn, dr, p, *dummy in readtext(filepath):

            if id != 'id':
                if top_cost_drug.get(dr) is None:
                    top_cost_drug[dr] = [{fn+ln: 1}, float(p)]
                else:
                    top_cost_drug[dr][0][fn+ln] = 1
                    top_cost_drug[dr][1] = top_cost_drug.get(dr)[1] + float(p)
except ValueError as e:
    print(e)

print('drug_name', 'num_prescriber', 'total_cost', sep=',', file=result_file)

for x in top_cost_drug.items():
    print(x[0], len(x[1][0]), round(x[1][1], 2), sep=',', file=result_file)

print('Completed in {} seconds'.format(round(time.time()-start_time, 2), '.2f'))
