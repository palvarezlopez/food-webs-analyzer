from common.inputParameters import InputParameters
from common.printer import Printer
from ecosystem.ecosystem import Ecosystem

# declare food web analyzer instance
inputParameters: InputParameters = InputParameters(
    ["--dataFolder", ".",
     "--checkLocalStability",
     "--outputPlainFile", "plainOutput.txt",
     "--outputLatexFile", "latexOutput"])

# init printer
printer: Printer = Printer(inputParameters)

# load food web data test
testData = Ecosystem(inputParameters, printer, "foodWebData.m", False)