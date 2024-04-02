# import common libraries
import sympy as sp

# import libraries
from foodWebsAnalyzer.common.inputParameters import InputParameters
from foodWebsAnalyzer.common.printer import Printer
from foodWebsAnalyzer.ecosystems.data.foodWebData import FoodWebData
from foodWebsAnalyzer.ecosystems.data.symbolicData import SymbolicData
from foodWebsAnalyzer.ecosystems.proportions import Proportions
from foodWebsAnalyzer.ecosystems.analysis.steadyStates import SteadyStates
from foodWebsAnalyzer.ecosystems.analysis.stability import Stability
from foodWebsAnalyzer.ecosystems.controlSpaces.controlSpaceJacobian import ControlSpaceJacobian
from foodWebsAnalyzer.ecosystems.analysis.consumptionIntensities import ConsumptionIntensities

# class general model (used for calculate all donor control parameters)
class GeneralModel:

    # initializing, receive io parameters and symbolic data
    def __init__(self, inputParameters: InputParameters, printer: Printer, consumptionIntensities: ConsumptionIntensities,
                 symbolicData: SymbolicData, foodWebData: FoodWebData, proportions: Proportions) -> None:
        # calculate derivative
        self.calculateDerivative(inputParameters, printer, consumptionIntensities, symbolicData, foodWebData, proportions)
        # calculate jacobian
        self.calculateJacobian(inputParameters, printer, consumptionIntensities, symbolicData, foodWebData, proportions)
        # check if calculate steady states
        if (inputParameters.checkCalculateSteadyStates()):
            self.steadyStates = SteadyStates(inputParameters, printer, "GeneralModel", self.jacobian, symbolicData, foodWebData)
        else:
            self.steadyStates = None
        # check if analyze fixed points
        if (inputParameters.checkLocalStability):
            # calculate stability
            self.stability = Stability(self.jacobian, symbolicData, foodWebData)
            self.controlSpaceJacobian = ControlSpaceJacobian(printer, self.stability, foodWebData)
        else:
            self.stability = None
            self.controlSpaceJacobian = None

    # calculate general model derivative
    def calculateDerivative(self, inputParameters: InputParameters, printer: Printer, consumptionIntensities: ConsumptionIntensities,
                            symbolicData: SymbolicData, foodWebData: FoodWebData, proportions: Proportions) -> None:
        # get common size n
        n: int = foodWebData.n
        # init total system flows
        self.donorControlTotalSystemFlows = sp.Matrix(sp.ZeroMatrix(n, 1))
        self.recipientTotalSystemFlows = sp.Matrix(sp.ZeroMatrix(n, 1))
        self.mixedTotalSystemFlows = sp.Matrix(sp.ZeroMatrix(n, 1))
        # calculate total system flows
        for i in range(0, n):
            # declare partial sums
            sumDonorControl = 0
            sumRecipient = 0
            sumMixed = 0
            for j in range(0, n):
                sumDonorControl += ((consumptionIntensities.donorControlConsumption[i,j] * symbolicData.biomass[j, 0]) -
                                    (consumptionIntensities.donorControlConsumption[j,i] * symbolicData.biomass[i, 0]))
                sumRecipient += ((consumptionIntensities.recipientConsumption[i,j] * symbolicData.biomass[i, 0]) -
                                 (consumptionIntensities.recipientConsumption[j,i] * symbolicData.biomass[j, 0]))
                sumMixed += ((consumptionIntensities.lotkaVolterraConsumption[i,j] * symbolicData.biomass[i, 0] * symbolicData.biomass[j, 0]) -
                             (consumptionIntensities.lotkaVolterraConsumption[j,i] * symbolicData.biomass[i, 0] * symbolicData.biomass[j, 0]))
            # add sums into total system flows
            self.donorControlTotalSystemFlows[i, 0] = sumDonorControl
            self.recipientTotalSystemFlows[i, 0] = sumRecipient
            self.mixedTotalSystemFlows[i, 0] = sumMixed
        # init total system flows
        self.totalSystemFlows = sp.Matrix(sp.ZeroMatrix(n, 1))
        # calculate total system flows
        for i in range(0, n):
            self.totalSystemFlows[i, 0] = ((proportions.s_d * self.donorControlTotalSystemFlows[i, 0]) +
                                           (proportions.s_r * self.recipientTotalSystemFlows[i, 0]) +
                                           (proportions.s_l * self.mixedTotalSystemFlows[i, 0]))
        # init derivative
        self.db_dt = sp.Matrix(sp.ZeroMatrix(n, 1))
        # calculate derivative
        for i in range(0, n):
            self.db_dt[i, 0] = self.totalSystemFlows[i, 0] - consumptionIntensities.outputConsumption[i, 0] + symbolicData.imports[i, 0]
        # print info
        if (inputParameters.verbose or inputParameters.verboseGeneralModelDerivative):
            printer.printInfo("Calculating general model derivative for foodWebData '" + foodWebData.food_web_filename + "'")
            # donor control
            printer.printMatrixEvaluated(
                "Donor control total system flows",
                self.donorControlTotalSystemFlows, symbolicData.getFoodWebDataSubsValues(foodWebData))
            # recipient
            printer.printMatrixEvaluated(
                "Recipient total system flows",
                self.recipientTotalSystemFlows, symbolicData.getFoodWebDataSubsValues(foodWebData))
            # mixed
            printer.printMatrixEvaluated(
                "Mixed total system flows",
                self.mixedTotalSystemFlows, symbolicData.getFoodWebDataSubsValues(foodWebData))
            # result
            printer.printMatrixEvaluated(
                "Total system flows",
                self.totalSystemFlows, symbolicData.getFoodWebDataSubsValues(foodWebData))
            printer.printMatrixEvaluated(
                "Derivative",
                self.db_dt, symbolicData.getFoodWebDataSubsValues(foodWebData))

    # calculate general model derivative
    def calculateJacobian(self, inputParameters: InputParameters, printer: Printer, consumptionIntensities: ConsumptionIntensities,
                          symbolicData: SymbolicData, foodWebData: FoodWebData, proportions: Proportions) -> None:
        # check if use sympy jacobian method or calculate manually
        if inputParameters.useSympyJacobian:
            # calculate use sympy jacobian
            self.jacobian = self.db_dt.jacobian(symbolicData.biomass)
            # print info
            if (inputParameters.verbose or inputParameters.verboseGeneralModelJacobian):
                printer.printInfo("Calculating general model jacobian matrix for foodWebData '" + foodWebData.food_web_filename + "'")
                printer.printMatrixEvaluated(
                    "Jacobian (Sympy)",
                    self.jacobian, symbolicData.getFoodWebDataSubsValues(foodWebData))
        else:
            # get common size n
            n: int = foodWebData.n
            # init jacobian matrix
            self.jacobian = sp.Matrix(sp.ZeroMatrix(n, n))
            # calculate consumptions
            for i in range(0, n):
                for j in range(0, n):
                    if (i != j):
                        self.jacobian[i, j] = ((proportions.s_d * consumptionIntensities.donorControlConsumption[i,j]) -
                                               (proportions.s_r * consumptionIntensities.recipientConsumption[j,i]) +
                                               (proportions.s_l * (consumptionIntensities.lotkaVolterraConsumption[i, j] - consumptionIntensities.lotkaVolterraConsumption[j,i]) * symbolicData.biomass[i, 0]))
                    else:
                        # calculate sumatorial values
                        sumDonorControlInitialConsumptionIntensity = 0
                        sumRecipientControlInitialConsumptionIntensity = 0
                        sumMixed = 0
                        for k in range(0, n):
                            sumDonorControlInitialConsumptionIntensity += consumptionIntensities.donorControlConsumption[k,i]
                            sumRecipientControlInitialConsumptionIntensity += consumptionIntensities.recipientConsumption[i,k]
                            sumMixed += ((consumptionIntensities.lotkaVolterraConsumption[i, k] * symbolicData.biomass[k, 0]) -
                                         (consumptionIntensities.lotkaVolterraConsumption[k, i] * symbolicData.biomass[k, 0]))
                        # calculate jacobian value
                        self.jacobian[i, j] = ((proportions.s_d * (consumptionIntensities.donorControlConsumption[i,i] - sumDonorControlInitialConsumptionIntensity)) +
                                               (proportions.s_r * (sumRecipientControlInitialConsumptionIntensity - consumptionIntensities.recipientConsumption[i,i])) +
                                               (proportions.s_l * sumMixed) - consumptionIntensities.outputConsumption[i])
            # print info
            if (inputParameters.verbose or inputParameters.verboseGeneralModelJacobian):
                printer.printInfo("Calculating general jacobian matrix for foodWebData '" + foodWebData.food_web_filename + "'")
                printer.printMatrixEvaluated(
                    "Jacobian",
                    self.jacobian, symbolicData.getFoodWebDataSubsValues(foodWebData))

    # donor control total system flows
    donorControlTotalSystemFlows: sp.Matrix

    # recipient total system flows
    recipientTotalSystemFlows: sp.Matrix

    # mixed total system flows
    mixedTotalSystemFlows: sp.Matrix

    # total system flow
    totalSystemFlows: sp.Matrix

    # derivative of b / derivative of t
    db_dt: sp.Matrix

    # jacobian matrix
    jacobian: sp.Matrix

    # steady States
    steadyStates: SteadyStates

    # domeig components
    stability: Stability

    # control space jacobian
    controlSpaceJacobian: ControlSpaceJacobian

    