print("OPTION1: LAGRANGE'S INTERPOLATION\nOPTION2: GAUSSIAN EQUATION")
option = int(input("Enter your choice: "))

if option == 1:
    from other.maths import Analysis
    analysis = Analysis()
    analysis.LagrangeInterpolation()
    analysis.PlotAtOldValues()
    analysis.PlotAtNewValues()

elif option == 2:
    from other.maths import Algebra
    gauss = Algebra()
    import numpy as np
    variable_matrix = np.array([[2,3,-1],[1,-1,2],[3,2,1]])
    constant_matrix = np.array([[7],[5],[12]])
    
    gauss.GaussElimination(variable_matrix,constant_matrix)
print("Program ends!")