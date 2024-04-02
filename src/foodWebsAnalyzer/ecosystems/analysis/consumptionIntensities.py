# import common libraries
import sympy as sp

# import libraries
from foodWebsAnalyzer.common.inputParameters import InputParameters
from foodWebsAnalyzer.common.printer import Printer
from foodWebsAnalyzer.ecosystems.data.foodWebData import FoodWebData
from foodWebsAnalyzer.ecosystems.data.symbolicData import SymbolicData

# class consumption intensities
class ConsumptionIntensities:

    # initializing, receive io parameters and symbolic data
    def __init__(self, inputParameters: InputParameters, printer: Printer, symbolicData: SymbolicData, foodWebData: FoodWebData) -> None:
        # get common size n
        n: int = foodWebData.n
        # declare consumptions for the three models
        self.donorControlConsumption = sp.Matrix(sp.ZeroMatrix(n, n))
        self.recipientConsumption = sp.Matrix(sp.ZeroMatrix(n, n))
        self.lotkaVolterraConsumption = sp.Matrix(sp.ZeroMatrix(n, n))
        # declare consumption matrix
        self.outputConsumption = sp.Matrix(sp.ZeroMatrix(n, n))
        # calculate consumption outputs
        for i in range(0, n):
            for j in range(0, n):
                self.donorControlConsumption[i,j] = (symbolicData.flowMatrix[i,j] / symbolicData.initialBiomass[j, 0])
                self.recipientConsumption[i,j] = (symbolicData.flowMatrix[i,j] / symbolicData.initialBiomass[i, 0])
                self.lotkaVolterraConsumption[i,j] = (symbolicData.flowMatrix[i,j] / (symbolicData.initialBiomass[i, 0] * symbolicData.initialBiomass[j, 0]))
            # calculate consumption output dividing exports and respirations by initial biomass
            self.outputConsumption[i, 0] = (symbolicData.exports[i, 0] + symbolicData.respiration[i, 0]) / symbolicData.initialBiomass[i, 0];
        # print info
        if (inputParameters.verbose or inputParameters.verboseGeneralModelDerivative):
            printer.printInfo("Calculating output consumption for foodWebData '" + foodWebData.food_web_filename + "'")
            # donor control
            printer.printMatrixEvaluated(
                "Output consumption",
                self.outputConsumption, symbolicData.getFoodWebDataSubsValues(foodWebData))     

    # donor control consumption intensity: F (/) bi
    donorControlConsumption: sp.Matrix

    # recipient consumption intensity: F (/) bj
    recipientConsumption: sp.Matrix

    # lotka volterra: F (/) bi*bj
    lotkaVolterraConsumption: sp.Matrix
    
    # consumption outputs (q + r) (/) bj
    outputConsumption: sp.Matrix