global SOLUTION_H

def help(r):


def

class C_Solution:





    S_Tab_Vji = []
    S_Xi = []
    S_Cibles_Couvertes = []



    def __init__(self, p_nbr_capteurs, p_nbr_cibles, p_Tab_Cout, p_Tab_Vij):

        for i in range(p_nbr_capteurs):
            S_Xi.append(0)

        self.S_Cout = 0
        self.S_Tab_Cout = p_Tab_Cout
        self.S_nbr_capteurs = p_nbr_capteurs
        self.S_nbr_cibles = p_nbr_cibles
        self.S_M = p_nbr_cibles
        self.S_Tab_Vij = p_Tab_Vij
        self.CreationTabVji()




    def CalculeCiblesCouvertes(self):

        self.S_Cibles_Couvertes = []

        for i in range(self.S_nbr_cibles):

            self.S_Cibles_Couvertes.append(0)

            for j in range(len(self.S_Tab_Vij[i])):

                if self.S_Xi[self.S_Tab_Vij[i][j] - 1] == 1:

                    self.S_Cibles_Couvertes[i] = 1



    def CreationTabVji(self):

        capteur = []

        for i in range(self.S_nbr_capteurs):

            for j in range(self.S_nbr_cibles):

                for k in range(len(self.S_Tab_Vij[j])):

                    if i == self.S_Tabj_Vij[j][k] - 1:

                        capteur.append(j+1)

            self.S_Tab_Vji.append(capteur)

            capteur = []


    def Heuristique(self):

        self.CalculeCiblesCouvertes()
        Index = 0
        Score = []

        for i in range(self.S_nbr_capteurs):

            Score.append(0)

            for j in range(len(S_TabVji[i])):

                if (S_Cibles_Couvertes[S_Tab_Vji[i][j] - 1] == 0):

                    Score[i] = Score[i] + 1

            Score[i] = float(Score[i] / S_Tab_Count[i])

            if Score[i] > Score[Index]:

                Index = i

        return Index



    def CalculCout(self):

        self.S_Cout = 0

        for i in range(self.S_nbr_capteurs):

            self.S_Cout = self.S_Cout + self.S_Xi[i] * self.S_Tab_Cout[i]

        return self.S_Cout




    def AlgorythmeGlouton(self):

        while self.S_M > 0:

            i = self.Heuristique()
            S_Xi[i] = 1
            S_M = S_nbr_Cibles
            self.CalculeCiblesCouvertes()

            for j in range(S_nbr_cibles):

                S_M = S_M - self.S_Cibles_Couvertes[j]

        return self.CalculCout()

