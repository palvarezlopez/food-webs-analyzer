from common.inputParameters import InputParameters
from common.printer import Printer
from ecosystems.ecosystem import Ecosystem

# declare input-output parameters
inputParameters: InputParameters = InputParameters(
    ["--dataFolder", ".",
     "--verbose-inputFile",
     "--calculateBiomassDynamic",
     "--proportion-sd", "0.0",
     "--proportion-sr", "1.0",
     "--verbose-generalModelODE",
     "--outputPlainFile", "plainOutput.txt",
     "--outputLatexFile", "latexOutput"])

# init printer
printer: Printer = Printer(inputParameters)

# load food web data test
testData = Ecosystem(inputParameters, printer, "foodWebData.m", False)