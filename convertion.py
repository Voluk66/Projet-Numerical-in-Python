import sys
N = 0
M = 0
Maximiser = True
cpt = 0

File = open(sys.argv[1],'r')
line = File.readlines()
N=int(line[0].split()[0])
M=int(line[0].split()[1])
Ci=[]
for k in range(0,N):
    Ci.append(line[k+1].split()[1])

test = N * [[0]]
verif = N * [[0]]
n = 0


while n < N:
    test[n] = [n, []]
    verif[n] = [n, []]
    n = n + 1
for l in range(0, M):
    test[int(line[N+1+l].split()[0])][1].append(int(line[N+1+l].split()[1]))
File2 = open(sys.argv[2], 'w')
File2.write("Maximize\n")
File2.write("z: ")

for k in range(0,N):
    if (k == N-1):
        File2.write(str(Ci[k])+" x"+str(k))
    else:
        File2.write(str(Ci[k]) + " x" + str(k) + " + ")

File2.write("\nSubject To\n")
cpt = 0
for k in range(0, N):
    for n in range(0, N):
        if test[k][1]:
            'for j in range(0):'

            if n not in test[k][1] and n != k and k not in test[n][1]:
                File2.write("Connaissance"+str(cpt)+": x"+str(test[k][0])+" + x"+str(n)+" <= 1\n")
                verif[n][1].append(k);
                cpt += 1

print(verif[225])
File2.write("\nBinaries\n")
for k in range(0, N):
    File2.write("x"+str(k)+"\n")
File2.write("End")
File.close()
File2.close()


