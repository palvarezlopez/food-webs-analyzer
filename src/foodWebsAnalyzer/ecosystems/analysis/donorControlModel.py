# import common libraries
import sympy as sp

# import libraries
from foodWebsAnalyzer.common.inputParameters import InputParameters
from foodWebsAnalyzer.common.printer import Printer
from foodWebsAnalyzer.common import matrixOperations as mo
from foodWebsAnalyzer.ecosystems.data.foodWebData import FoodWebData
from foodWebsAnalyzer.ecosystems.data.symbolicData import SymbolicData
from foodWebsAnalyzer.ecosystems.analysis.steadyStates import SteadyStates

# class donor control model (used for calculate all donor control parameters)
class DonorControlModel:

    # initializing, receive io parameters and symbolic data
    def __init__(self, inputParameters: InputParameters, printer: Printer, symbolicData: SymbolicData, foodWebData: FoodWebData) -> None:
        # calculate consumption outputs
        self.calculateConsumptionOutputs(inputParameters, printer, symbolicData, foodWebData)
        # calculate derivative
        self.calculateDerivative(inputParameters, printer, symbolicData, foodWebData)
        # calculate fixed points
        self.calculateFixedPoints(inputParameters, printer, symbolicData, foodWebData)
        # calculate jacobian
        #self.calculateJacobian(inputParameters, printer, symbolicData, foodWebData)
        # calculate steady states
        #self.steadyStates = SteadyStates(inputParameters, printer, "DonorControl", self.jacobian, symbolicData, foodWebData)

    # calculate consumption outputs
    def calculateConsumptionOutputs(self, inputParameters: InputParameters, printer: Printer, symbolicData: SymbolicData, foodWebData: FoodWebData) -> None:
        # get common size n
        n: int = foodWebData.n
        # declare consumption matrix
        self.consumptionOutputs = sp.Matrix(sp.ZeroMatrix(n, n))
        # calculate consumption outputs
        for i in range(0, n):
            self.consumptionOutputs[i, 0] = (symbolicData.exports[i, 0] + symbolicData.respiration[i, 0]) / symbolicData.initialBiomass[i, 0];
        # print info
        if (inputParameters.verbose or inputParameters.verboseGeneralModelDerivative):
            printer.printInfo("Calculating consumption outputs for foodWebData '" + foodWebData.food_web_filename + "'")
            # donor control
            printer.printMatrixEvaluated(
                "Consumption outputs",
                self.consumptionOutputs, symbolicData.getFoodWebDataSubsValues(foodWebData))        
        
    # calculate donor control model derivative
    def calculateDerivative(self, inputParameters: InputParameters, printer: Printer, symbolicData: SymbolicData, foodWebData: FoodWebData) -> None:
        # get common size n
        n: int = foodWebData.n
        # declare consumption matrix
        self.donorControlInitialConsumptionIntensity = sp.Matrix(sp.ZeroMatrix(n, n))
        # calculate consumptions
        for i in range(0, n):
            for j in range(0, n):
                self.donorControlInitialConsumptionIntensity[i,j] = (symbolicData.flowMatrix[i,j] / symbolicData.initialBiomass[j, 0])
        # init total system flows
        self.donorControlTotalSystemFlows = sp.Matrix(sp.ZeroMatrix(n, 1))
        # calculate total system flows
        for i in range(0, n):
            # declare partial sums
            sumDonorControl = 0
            for j in range(0, n):
                sumDonorControl += ((self.donorControlInitialConsumptionIntensity[i,j] * symbolicData.biomass[j, 0]) -
                                    (self.donorControlInitialConsumptionIntensity[j,i] * symbolicData.biomass[i, 0]))
            # add sums into total system flows
            self.donorControlTotalSystemFlows[i, 0] = sumDonorControl
        # init derivative
        self.db_dt = sp.Matrix(sp.ZeroMatrix(n, 1))
        # calculate derivative
        for i in range(0, n):
            self.db_dt[i, 0] = self.donorControlTotalSystemFlows[i, 0] - self.consumptionOutputs[i, 0] + symbolicData.imports[i, 0]
        # print info
        if (inputParameters.verbose or inputParameters.verboseDonorControlDerivative):
            printer.printInfo("Calculating donor control model derivative for foodWebData '" + foodWebData.food_web_filename + "'")
            # donor control
            printer.printMatrixEvaluated(
                "Donor control initial consumption intensity",
                self.donorControlInitialConsumptionIntensity, symbolicData.getFoodWebDataSubsValues(foodWebData))
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
    def calculateJacobian(self, inputParameters: InputParameters, printer: Printer, symbolicData: SymbolicData, foodWebData: FoodWebData) -> None:
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
            # get the sume of units exports and respirations
            exportUnits : sp.Matrix = mo.add(self.unitsExport, self.unitsRespiration)
            # calculate diagonal matrix of the sumo of consumption intensity and outflows
            diagonal: sp.Matrix = mo.diagonal(mo.add(self.consumptionIntensity, exportUnits));
            # calculate jacobian substracting the calculated diagonal to the consumptionIntensity matrix
            self.jacobian = mo.substract(self.initialConsumptionIntensity, diagonal)
            # print info
            if (inputParameters.verbose or inputParameters.verboseDonorControlJacobian):
                printer.printInfo("Calculating donor control model jacobian matrix for foodWebData '" + foodWebData.food_web_filename + "'")
                # get dictionary with food web data subs values
                foodWebDataSubsValues = symbolicData.getFoodWebDataSubsValues(foodWebData)
                printer.printMatrixEvaluated(
                    "Diagonal: consumptionIntensity + outflows",
                    diagonal, foodWebDataSubsValues)
                printer.printMatrixEvaluated(
                    "Jacobian: initialConsumptionIntensity - diagonal",
                    self.jacobian, foodWebDataSubsValues)

    # consumption outputs
    consumptionOutputs: sp.Matrix

    # donor control consumption intensity: F (/) bi
    donorControlInitialConsumptionIntensity: sp.Matrix

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