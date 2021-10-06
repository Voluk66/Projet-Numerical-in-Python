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
Vij = N*[[0]]

memory = 0
cpt = 0
print(line[301])
for k in range(0,M):
    if N+k == N+M:
        if int(line[N  + k - 1].split()[0]) == int(line[N + 1 + k].split()[0]):
            if cpt == 0:
                Vij[int(line[N + 1 + memory].split()[0])][cpt] = int(line[N + 1 + memory].split()[1])
                cpt = cpt + 1
            else :
                Vij[int(line[N + 1 + memory].split()[0])].append(int(line[N + 1 + memory].split()[1]))
                cpt = cpt + 1
        else:
            cpt = 0
            Vij[int(line[N + 1 + k].split()[0])][cpt] = int(line[N + 1 + k].split()[1])
            cpt = cpt + 1

    if N+k != N+M:
        if int(line[N+k].split()[0]) == int(line[N+k+1].split()[0]):
            if cpt == 0:
                Vij[int(line[N+1 + memory].split()[0])][cpt] = int(line[N+1 + memory].split()[1])
                cpt = cpt + 1
            else:
                Vij[int(line[N + 1 + memory].split()[0])].append(int(line[N + 1 + memory].split()[1]))
                cpt = cpt + 1
        else:
            cpt=0
            Vij[int(line[N + 1 + k].split()[0])][cpt] = int(line[N + 1 + k].split()[1])
            cpt +=1
    memory = k

print(Vij[299][0])
File.close()
File2 = open(sys.argv[2],'w')
File2.write("Maximize\n")
File2.write("z: ")

for k in range(0,N):
    if (k == N-1):
        File2.write(str(Ci[k])+" x"+str(k))
    else:
        File2.write(str(Ci[k]) + " x" + str(k) + " + ")
File2.write("\nSubject To")

File2.write("\nBinaries\n")
for k in range(0,N):
    File2.write("x"+str(k)+"\n")
File2.write("End")



