import sympy as sp
from common.inputParameters import InputParameters
from common import matrixOperations as mo
from common.printer import Printer
from ecosystems.ecosystem import Ecosystem

# declare input-output parameters
inputParameters: InputParameters = InputParameters(["--numerical", "--dataFolder", ".", "--calculateGeneralModel"])

# init printer
printer: Printer = Printer(inputParameters)

# load food web data test using manual mode
testDataA = Ecosystem(inputParameters, printer, "foodWebData.m", False)

# enable sympy
inputParameters.useSympyJacobian = True

# load food web data test using sympy mode mode
testDataB = Ecosystem(inputParameters, printer, "foodWebData.m", False)

# compare both jacobians
printer.printMatrix("Manual:", testDataA.generalModel.jacobian)
printer.printMatrix("Sympy:", testDataB.generalModel.jacobian)

if (mo.equals(testDataA.generalModel.jacobian, testDataB.generalModel.jacobian)):
    print("Same output")
else:
    raise Exception("different output")

