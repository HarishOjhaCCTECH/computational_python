import numpy as np    

class Analysis:
    def __init__(self):
        self.x = np.array([0,20,40,60,80,100], float)
        self.y = np.array([1.000, 0.899,0.745,0.582, 0.412,0.248])

    def LagrangeInterpolation(self):
        xp = float(input("Enter X: "))
        yp = 0
        for xi,yi in zip(self.x, self.y):
            yp += yi * np.prod((xp - self.x[self.x != xi])/(xi - self.x[self.x != xi]))
        print('For x = %.2f, y = %.3f' %(xp,yp))
        
    def PlotAtOldValues(self):
        import matplotlib.pyplot as plt
        xplt = np.linspace(self.x[0], self.x[-1])
        yplt = np.array([], float)
        for xp in xplt:
            yp = 0
            for xi, yi in zip(self.x, self.y):
                yp += yi * np.prod((xp - self.x[self.x != xi]) / (xi - self.x[self.x != xi]))
            yplt = np.append(yplt, yp)
        plt.plot(self.x, self.y, 'ro', xplt, yplt, 'b-')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

    def PlotAtNewValues(self):
        import matplotlib.pyplot as plt
        x_new = np.array([10,30,50,70,90], float)
        y_new = np.array([], float)
        for xp in x_new:                
            yp = 0
            for xi,yi in zip(self.x, self.y):
                yp += yi * np.prod((xp - self.x[self.x != xi]) / (xi - self.x[self.x != xi]))
            y_new = np.append(y_new, yp)
        plt.plot(x_new, y_new, 'ro')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()


class Algebra:
    def __init__(self):
        pass
    def GaussElimination(self, a_matrix, b_matrix):
        if a_matrix.shape[0] != a_matrix.shape[1]:
            print("ERROR: Square matrix not given!")
            return
        if b_matrix.shape[1] > 1 or b_matrix.shape[0] != a_matrix.shape[0]:
            print('ERROR: Constant vector incorrectly sized')
            return
        
        # Initialization of necessary vatriables
        n = len(b_matrix)
        m = n-1
        i = 0
        j = i-1
        x = np.zeros(n)
        new_line = "\n"
        
        # Create our augmented matrix through Numpy's Concatenate feature
        augmented_matrix = np.concatenate((a_matrix, b_matrix), axis=1, dtype=float)
        print(f"The initial augmented matrix is {new_line}{augmented_matrix}")
        print("Solving for the upper-triangular matrix:")
        
        # Apply Gauss Elimination:
        while i<n:
            if augmented_matrix[i][i] == 0.0: # Fail-safe to eliminate divide by zero error!
                print("Divide by zero error")
                return
            for j in range(i+1, n):
                scaling_factor = augmented_matrix[j][i] / augmented_matrix[i][i]
                augmented_matrix[j] = augmented_matrix[j] - (scaling_factor * augmented_matrix[i])
                print(augmented_matrix) 
            i = i + 1
        
        # Backward substitution
        x[m] = augmented_matrix[m][n]/augmented_matrix[m][m]
        for k in range(n-2, -1,-1):
            x[k] = augmented_matrix[k][n]
            
            for j in range(k +1, n):
                x[k] = x[k] / augmented_matrix[k][k]
        # Displaying Solution
        print(f"The following x-vector matrix solves the above augmented matrix:")   
        for answer in range(n):
            print(f"x{answer} is {x[answer]}")