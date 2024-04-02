# import common libraries
import sympy as sp

# import libraries
from foodWebsAnalyzer.common.inputParameters import InputParameters
from foodWebsAnalyzer.common.printer import Printer
from foodWebsAnalyzer.ecosystems.data.foodWebData import FoodWebData
from foodWebsAnalyzer.ecosystems.data.symbolicData import SymbolicData
from foodWebsAnalyzer.ecosystems.analysis.steadyStates import SteadyStates
from foodWebsAnalyzer.ecosystems.analysis.consumptionIntensities import ConsumptionIntensities

# class donor control model (used for calculate all donor control parameters)
class DonorControlModel:

    # initializing, receive io parameters and symbolic data
    def __init__(self, inputParameters: InputParameters, printer: Printer, consumptionIntensities: ConsumptionIntensities,
                 symbolicData: SymbolicData, foodWebData: FoodWebData) -> None:
        # calculate derivative
        self.calculateDerivative(inputParameters, printer, consumptionIntensities, symbolicData, foodWebData)
        # calculate fixed points
        self.calculateFixedPoints(inputParameters, printer, symbolicData, foodWebData)
        # calculate jacobian
        self.calculateJacobian(inputParameters, printer, consumptionIntensities, symbolicData, foodWebData)
        # calculate steady states
        self.steadyStates = SteadyStates(inputParameters, printer, "DonorControl", self.jacobian, symbolicData, foodWebData)
             
    # calculate donor control model derivative
    def calculateDerivative(self, inputParameters: InputParameters, printer: Printer, consumptionIntensities: ConsumptionIntensities,
                            symbolicData: SymbolicData, foodWebData: FoodWebData) -> None:
        # get common size n
        n: int = foodWebData.n
        # init total system flows
        self.donorControlTotalSystemFlows = sp.Matrix(sp.ZeroMatrix(n, 1))
        # calculate total system flows
        for i in range(0, n):
            # declare partial sums
            sumDonorControl = 0
            for j in range(0, n):
                sumDonorControl += ((consumptionIntensities.donorControlConsumption[i,j] * symbolicData.biomass[j, 0]) -
                                    (consumptionIntensities.donorControlConsumption[j,i] * symbolicData.biomass[i, 0]))
            # add sums into total system flows
            self.donorControlTotalSystemFlows[i, 0] = sumDonorControl
        # init derivative
        self.db_dt = sp.Matrix(sp.ZeroMatrix(n, 1))
        # calculate derivative
        for i in range(0, n):
            self.db_dt[i, 0] = self.donorControlTotalSystemFlows[i, 0] - consumptionIntensities.outputConsumption[i, 0] + symbolicData.imports[i, 0]
        # print info
        if (inputParameters.verbose or inputParameters.verboseDonorControlDerivative):
            printer.printInfo("Calculating donor control model derivative for foodWebData '" + foodWebData.food_web_filename + "'")
            # donor control total system flows
            printer.printMatrixEvaluated(
                "Donor control total system flows",
                self.donorControlTotalSystemFlows, symbolicData.getFoodWebDataSubsValues(foodWebData))
            # result
            printer.printMatrixEvaluated(
                "Derivative",
                self.db_dt, symbolicData.getFoodWebDataSubsValues(foodWebData))

    # calculate donor control fixed points
    def calculateFixedPoints(self, inputParameters: InputParameters, printer: Printer, symbolicData: SymbolicData, foodWebData: FoodWebData) -> None:
        # evaluate parameters in db_dt
        db_dt_evaluated: sp.Matrix = self.db_dt.subs(symbolicData.getFoodWebDataSubsValues(foodWebData))
        # calculate donor control fixed points: evaluate initial biomass in db_dt_evaluated (b = b0)
        self.fixedPoints = db_dt_evaluated.subs(symbolicData.getBiomassSubsValues(foodWebData.getinitialBiomass()))
        # print info
        if (inputParameters.verbose or inputParameters.verboseDonorControlFixedPoints):
            printer.printInfo("Calculating donor control model fixed points for '" + foodWebData.food_web_filename + "'")
            printer.printMatrix("Fixed points(b = b0):", self.fixedPoints)

    # calculate donor control Jacobian
    def calculateJacobian(self, inputParameters: InputParameters, printer: Printer, consumptionIntensities: ConsumptionIntensities,
                          symbolicData: SymbolicData, foodWebData: FoodWebData) -> None:
        # first check if use sympy jacobian method or calculate manually
        if inputParameters.useSympyJacobian:
            # calculate use sympy jacobian
            self.jacobian = self.db_dt.jacobian(symbolicData.biomass)
            # print info
            if (inputParameters.verbose or inputParameters.verboseDonorControlJacobian):
                printer.printInfo("Calculating donor control model jacobian matrix for foodWebData '" + foodWebData.food_web_filename + "'")
                printer.printMatrixEvaluated(
                    "Jacobian (Sympy)",
                    self.jacobian,
                    symbolicData.getFoodWebDataSubsValues(foodWebData))
        else:
            # get common size n
            n: int = foodWebData.n
            # init jacobian matrix
            self.jacobian = sp.Matrix(sp.ZeroMatrix(n, n))
            # calculate consumptions
            for i in range(0, n):
                for j in range(0, n):
                    if (i != j):
                        self.jacobian[i, j] = consumptionIntensities.donorControlConsumption[i,j]
                    else:
                        # calculate sumatorial values
                        sumDonorControlConsumption = 0
                        for k in range(0, n):
                            sumDonorControlConsumption += consumptionIntensities.donorControlConsumption[k,i]
                        # calculate jacobian value
                        self.jacobian[i, j] = consumptionIntensities.donorControlConsumption[i, i] - sumDonorControlConsumption - consumptionIntensities.outputConsumption[i, 0]
            # print info
            if (inputParameters.verbose or inputParameters.verboseDonorControlJacobian):
                printer.printInfo("Calculating donor control model jacobian matrix for foodWebData '" + foodWebData.food_web_filename + "'")
                printer.printMatrixEvaluated(
                    "Jacobian",
                    self.jacobian,
                    symbolicData.getFoodWebDataSubsValues(foodWebData))

    # donor control total system flows
    donorControlTotalSystemFlows: sp.Matrix

    # derivative of b / derivative of t
    db_dt: sp.Matrix

    # fixed points
    fixedPoints: sp.Matrix

    # jacobian matrix
    jacobian: sp.Matrix

    # steady States
    steadyStates: SteadyStates