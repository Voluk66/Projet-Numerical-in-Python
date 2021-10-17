import sys
import 'Solution.py'

def getConns(lines, n):

    cost = []
    count = n



    for i in range(count):

        if len(lines[i]) != 27:
            break

        chaine = lines[i][15:27]
        cost.append(chaine)

    return cost


def getCost(lines, m):

    Conns = []

    for i in range(m):
        nb_conn = len(lines) - 306

        var = lines[i].split()




        Conns.append

if __name__ == '__main__':



    if len(sys.argv) != 2:
        print('Entrez deux arguments')

    filename = sys.argv[1]
    filewrite = sys.argv[2]

    instance = open(filename)

    lines = []

    for i in instance:
        lines.append(i)

    n = 2
    m = len(lines) - n

    cost = getCost(lines, m)

    Conns = getConns(lines, n)

    instance.close()

    C_solution S = C_Solution(m, n, cost, Conns)
    fin = S.AlgorithmeGlouton()
    print(fin)

    instance2 = open(filewrite, "w")
    instance2.write(fin)
    instance2.close()

    return 0





