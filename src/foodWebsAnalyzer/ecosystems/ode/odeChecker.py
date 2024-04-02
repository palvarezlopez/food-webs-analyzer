# import common libraries
import sympy as sp

# import libraries
from foodWebsAnalyzer.common.inputParameters import InputParameters
from foodWebsAnalyzer.common.printer import Printer
from foodWebsAnalyzer.ecosystems.data.foodWebData import FoodWebData
from foodWebsAnalyzer.ecosystems.analysis.generalModel import GeneralModel


# class ODEChecker (used for check ODE results)
class ODEChecker:

    # Initializing, receive input parameters, printer and ode solver
    def __init__(self, inputParameters: InputParameters, printer: Printer, foodWebData: FoodWebData,
                 biomassFinal: sp.Matrix, generalModel: GeneralModel) -> None:
        # check if biomass final size is different of initial biomass
        sameSize: bool = (len(foodWebData.initialBiomass) == len(biomassFinal))
        # declare matrix with the differences between initial biomass and calculated biomass final
        differenceMatrix = sp.Matrix(sp.ZeroMatrix(foodWebData.n, 1))
        for i in range(0, foodWebData.n):
            if (sameSize):
                differenceMatrix[i,0] = (foodWebData.initialBiomass[i,0] - biomassFinal[i,0])
            else:
                differenceMatrix[i,0] = None 
        # print info
        if (inputParameters.verbose or inputParameters.verboseGeneralModelODEChecker):
            printer.printInfo("Checking ODE Results for foodWebData '" + foodWebData.food_web_filename + "'")
            printer.printMatrix("Differences between initialBiomass and biomass calculated by ODE", differenceMatrix)
            printer.printGraphMatrix(differenceMatrix)
