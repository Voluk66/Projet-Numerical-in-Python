import sys
N = 0
M = 0
Maximiser = True



File = open(sys.argv[1],'r')
line = File.readlines()
N=int(line[0].split()[0])
M=int(line[0].split()[1])
Ci=[]
for k in range(0,N):
    Ci.append(line[k+1].split()[1])
compteur = M * [2 * [0]]
for l in range(0 , M):
    compteur[l] = [int(line[N+1+l].split()[0]), int(line[N+1+l].split()[1])]

File2 = open(sys.argv[2], 'w')
File2.write("Maximize\n")
File2.write("z: ")

for k in range(0,N):
    if (k == N-1):
        File2.write(str(Ci[k])+" x"+str(k))
    else:
        File2.write(str(Ci[k]) + " x" + str(k) + " + ")
File2.write("\nSubject To")
tmp = 299
for k in range(0, M):
    if compteur[k][0] != tmp:
        if tmp == 299:
            tmp = 0
        else:
            tmp += 1

    else:
        print(compteur[k][0], "coucou")
File2.write("\nBinaries\n")
for k in range(0, N):
    File2.write("x"+str(k)+"\n")
File2.write("End")
File.close()
File2.close()


