import sys
import 'Solution.py'

def getConns(lines, n):


    count = n
    chaine = []



    for i in range(count):

        if len(lines[i+2]) == 0:
            break

        var = lines[i+2]

        for j in var:
            numero = []
            if j == 'x':
                for k in range(len(var)):

                    while var[i][k] != " ":
                        numero.append(var[i][k])

                    if numero not in chaine:
                        chaine.extend([numero,1])

                    if numero in chaine:
                        chaine[chaine.index(numero)][1] = chaine[chaine.index(numero)][1] + 1

    return chaine





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

    m = 2
    n = len(lines) - m

    cost = getCost(lines, m)

    Conns = getConns(lines, n)

    instance.close()

    C_solution S = C_Solution(n, m, cost, Conns)
    fin = S.AlgorithmeGlouton()
    print(fin)

    instance2 = open(filewrite, "w")
    instance2.write(fin)
    instance2.close()

    return 0





