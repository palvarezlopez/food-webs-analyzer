# import libraries
from foodWebsAnalyzer.common.inputParameters import InputParameters
from foodWebsAnalyzer.common.printer import Printer
from foodWebsAnalyzer.ecosystems.ode.odeSolver import ODESolver
from foodWebsAnalyzer.ecosystems.balancing import Balancing
from foodWebsAnalyzer.ecosystems.proportions import Proportions
from foodWebsAnalyzer.ecosystems.analysis.consumptionIntensities import ConsumptionIntensities
from foodWebsAnalyzer.ecosystems.analysis.donorControlModel import DonorControlModel
from foodWebsAnalyzer.ecosystems.analysis.generalModel import GeneralModel
from foodWebsAnalyzer.ecosystems.data.foodWebData import FoodWebData
from foodWebsAnalyzer.ecosystems.data.symbolicData import SymbolicData


# class ecosystem
class Ecosystem:

    # Initializing, receive filename and fill all food web data
    def __init__(self, inputParameters: InputParameters, printer: Printer, fileName: str, customInitialBiomass: bool):
        # init folder and latex document
        printer.initFolderAndLatexDocument(fileName)
        # declare food web data
        self.foodWebData = FoodWebData(inputParameters, printer, fileName, customInitialBiomass)
        # declare symbolic data
        self.symbolicData = SymbolicData(inputParameters, self.foodWebData)
        # declare proportions associated with this food web data
        self.proportions = Proportions()
        # calculate donor control model
        if (inputParameters.checkBalancing):
            self.balancing = Balancing(inputParameters, printer, self.foodWebData)
        # check if calculate consumptions
        if (inputParameters.calculateDonorControlModel or inputParameters.calculateGeneralModel):
            self.consumptionIntensities = ConsumptionIntensities(inputParameters, printer, self.symbolicData, self.foodWebData)
        else:
            self.consumptionIntensities = None
        # calculate donor control model
        if (inputParameters.calculateDonorControlModel):
            self.donorControlModel = DonorControlModel(inputParameters, printer, self.consumptionIntensities, self.symbolicData, self.foodWebData)
        else:
            self.donorControlModel = None
        # calculate general model
        if (inputParameters.calculateGeneralModel):
            self.generalModel = GeneralModel(inputParameters, printer, self.consumptionIntensities, self.symbolicData, self.foodWebData, self.proportions)
        else:
            self.generalModel = None
        # check if calculate biomass dynamic
        if (inputParameters.calculateBiomassDynamic):
            self.odeSolver = ODESolver(inputParameters, printer, self.generalModel, self.symbolicData, self.foodWebData, self.proportions)
        else:
            self.odeSolver = None
        # write output files
        printer.writeOutputFiles(self.foodWebData.food_web_filename)

    # foodWeb data
    foodWebData: FoodWebData

    # symbolic data
    symbolicData: SymbolicData

    # proportions
    proportions: Proportions

    # balancing
    balancing: Balancing

    # consumption intensities
    consumptionIntensities: ConsumptionIntensities

    # donor control model
    donorControlModel: DonorControlModel

    # general model
    generalModel: GeneralModel

    # ODE Solver
    odeSolver: ODESolver