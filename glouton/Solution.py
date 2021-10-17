


class C_Solution:





    S_Tab_Vji = []
    S_Xi = []
    S_Conns_Confirmees = []



    def __init__(self, p_nbr_contraintes, p_nbr_Conns, p_Tab_Cout, p_Tab_Vij):

        for i in range(p_nbr_contraintes):
            S_Xi.append(0)

        self.S_Cout = 0
        self.S_Tab_Cout = p_Tab_Cout
        self.S_nbr_contraintes = p_nbr_contraintes
        self.S_nbr_Conns = p_nbr_Conns
        self.S_M = p_nbr_Conns
        self.S_Tab_Vij = p_Tab_Vij
        self.CreationTabVji()




    def CalculeConnConfirmee(self):

        self.S_Conns_Confirmees = []

        for i in range(self.S_nbr_Conns):

            self.S_Conns_Confirmees.append(0)

            for j in range(len(self.S_Tab_Vij[i])):

                if self.S_Xi[self.S_Tab_Vij[i][j] - 1] == 1:

                    self.S_Conns_Confirmee[i] = 1



    def CreationTabVji(self):

        contrainte = []

        for i in range(self.S_nbr_contraintes):

            for j in range(self.S_nbr_Conns):

                for k in range(len(self.S_Tab_Vij[j])):

                    if i == self.S_Tabj_Vij[j][k] - 1:

                        contrainte.append(j+1)

            self.S_Tab_Vji.append(contrainte)

            contrainte = []


    def Heuristique(self):

        self.CalculeConnsConfirmees()
        Index = 0
        Score = []

        for i in range(self.S_nbr_contraintes):

            Score.append(0)

            for j in range(len(S_TabVji[i])):

                if (S_Conns_Confirmees[S_Tab_Vji[i][j] - 1] == 0):

                    Score[i] = Score[i] + 1

            Score[i] = float(Score[i] / S_Tab_Count[i])

            if Score[i] > Score[Index]:

                Index = i

        return Index



    def CalculConn(self):

        self.S_Cout = 0

        for i in range(self.S_nbr_contraintes):

            self.S_Cout = self.S_Cout + self.S_Xi[i] * self.S_Tab_Cout[i]

        return self.S_Cout




    def AlgorithmeGlouton(self):

        while self.S_M > 0:

            i = self.Heuristique()
            S_Xi[i] = 1
            S_M = S_nbr_Conn
            self.CalculeConnConfirmee()

            for j in range(S_nbr_Conns):

                S_M = S_M - self.S_Conns_Confirmees[j]

        return self.CalculCout()

