# import common libraries
import sympy as sp

# import libraries
from foodWebsAnalyzer.common.inputParameters import InputParameters
from foodWebsAnalyzer.common.printer import Printer
from foodWebsAnalyzer.ecosystems.data.foodWebData import FoodWebData


# class balancing (using for check if the given biomass is balanced)
class Balancing:

    # Initializing
    def __init__(self, inputParameters: InputParameters, printer: Printer, foodWebData: FoodWebData) -> None:
        print("test")