# import common libraries
import sympy as sp
import scipy as sc # type: ignore

# import libraries
from foodWebsAnalyzer.common.inputParameters import InputParameters
from foodWebsAnalyzer.common.printer import Printer
from foodWebsAnalyzer.ecosystems.proportions import Proportions
from foodWebsAnalyzer.ecosystems.data.foodWebData import FoodWebData
from foodWebsAnalyzer.ecosystems.data.symbolicData import SymbolicData
from foodWebsAnalyzer.ecosystems.analysis.generalModel import GeneralModel
from foodWebsAnalyzer.ecosystems.ode.odeChecker import ODEChecker
import foodWebsAnalyzer.utils.transform as tr
import foodWebsAnalyzer.utils.ode as ode


# class ODESolver (used for solve ODE)
class ODESolver:

    # Initializing, receive io parameters and symbolic data
    def __init__(self, inputParameters: InputParameters, printer: Printer, generalModel: GeneralModel,
                 symbolicData: SymbolicData, foodWebData: FoodWebData, proportions: Proportions) -> None:
        # use initial biomass
        generalModelResolved: sp.Matrix = generalModel.db_dt.subs(symbolicData.getFoodWebDataSubsValues(foodWebData))
        # also resolve for proportions
        generalModelResolved = generalModelResolved.subs(proportions.getProportionSubsValues(inputParameters.proportionSd, inputParameters.proportionSr))
        # call ode solver
        self.odeResult = ode.solveNonLinearOde(inputParameters.ODESolver, tr.matrixFloatToList(generalModelResolved), symbolicData.getBiomassVariables(),
                                               tr.matrixFloatToList(foodWebData.initialBiomass), inputParameters.timeEnd, 100)
        # calculate biomass final (in timeEnd)
        self.biomassFinal = sp.Matrix(sp.ZeroMatrix(foodWebData.n, 1))
        for i in range(0, foodWebData.n):
            self.biomassFinal[i,0] = self.odeResult.y[i][1]
        # save values in file
        printer.writeMatrixColumnMatLab(foodWebData.food_web_filename, "biomassFinal_" + str(inputParameters.proportionSd) + "_" +
                                        str(inputParameters.proportionSr) + ".m", "b", self.biomassFinal)
        # check if save ODE results in table form
        if (inputParameters.exportODETable):
            printer.printODETable(self.odeResult)
        # print info
        if (inputParameters.verbose or inputParameters.verboseGeneralModelODE):
            printer.printInfo("Resolving ODE for foodWebData '" + foodWebData.food_web_filename + "'")
            printer.printMatrix("General model resolved",generalModelResolved)
            # print graph
            printer.printInfo("ODE result")
            printer.printInfo(self.odeResult.t)
            for i in range(0, len(self.odeResult.y)):
                printer.printInfo(self.odeResult.y[i])
            # printe ode graph
            printer.printODEGraph(foodWebData.food_web_filename, self.odeResult)
            # biomass final
            printer.printMatrix("Biomass final", self.biomassFinal)
        # declare ode checker
        self.odeChecker = ODEChecker(inputParameters, printer, foodWebData, self.biomassFinal, generalModel)

    # ode result
    odeResult: sc.integrate._ivp.ivp.OdeResult

    # biomass final for tn
    biomassFinal: sp.Matrix

    # ODE Checker
    odeChecker: ODEChecker
