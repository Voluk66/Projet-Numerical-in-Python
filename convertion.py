import sys

N = 0
M = 0
Maximiser = True
cpt = 0
test = N * [[0]]
n = 0
Ci = []

# Ouverture de l'instance
File = open(sys.argv[1], 'r')
line = File.readlines()

# Configuration N et M
N = int(line[0].split()[0])
M = int(line[0].split()[1])

# Configuration des Ci
for k in range(0, N):
    Ci.append(line[k + 1].split()[1])

# Initialisation des Vi
while n < N:
    test[n] = [n, []]
    n = n + 1

# Configuration des Vi
for l in range(0, M):
    test[int(line[N + 1 + l].split()[0])][1].append(int(line[N + 1 + l].split()[1]))

# Creation du fichier .lp
File2 = open(sys.argv[2], 'w')
File2.write("Maximize\n")

# Ecriture de l'objectif à Maximiser
File2.write("z: ")
for k in range(0, N):
    if k == N - 1:
        File2.write(str(Ci[k]) + " x" + str(k))
    else:
        File2.write(str(Ci[k]) + " x" + str(k) + " + ")

#Ecriture des contraintes
File2.write("\nSubject To\n")
for k in range(0, N): # On parcourt les Vi pour Chaque valeur de N
    for n in range(0, N):
        if test[k][1]:# Test si le Vi est vide
            if n not in test[k][1] and n != k and k not in test[n][1]:# Test si n est dans Vk et si n n'est pas k et si k n'est pas dans Vn
                File2.write("Connaissance" + str(cpt) + ": x" + str(test[k][0]) + " + x" + str(n) + " <= 1\n")
                cpt += 1

#Ecriture des Variables
File2.write("\nBinaries\n")
for k in range(0, N):
    File2.write("x" + str(k) + "\n")
File2.write("End")

#Fermeture des Fichiers
File.close()
File2.close()
