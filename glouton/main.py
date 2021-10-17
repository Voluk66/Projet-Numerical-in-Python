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





            Conns.append

if __name__ == '__main__':



    if len(sys.argv) != 1:
        print('Entrez un unique argument')

    filename = sys.argv[1]

    instance = open(filename)

    lines = []

    for i in instance:
        lines.append(i)


    cost = getCost(lines, m)

    Conns = getConns(lines, n)

    instance.close()

    C_solution S = C_Solution(n, m, cost, Conns)
    fin = S.AlgorithmeGlouton()
    print(fin)



