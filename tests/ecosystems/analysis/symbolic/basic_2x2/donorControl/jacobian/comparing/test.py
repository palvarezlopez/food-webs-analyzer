import sympy as sp
from common.inputParameters import InputParameters
from common import matrixOperations as mo
from common.printer import Printer
from ecosystem.ecosystem import Ecosystem

# declare input-output parameters
inputParameters: InputParameters = InputParameters(["--dataFolder", ".", "--calculateDonorControlModel"])

# init printer
printer: Printer = Printer(inputParameters)

# load food web data test using manual mode
testDataA = Ecosystem(inputParameters, printer, "foodWebData.m", False)

# enable sympy
inputParameters.useSympyJacobian = True

# load food web data test using sympy mode mode
testDataB = Ecosystem(inputParameters, printer, "foodWebData.m", False)

# evaluate jacobians
resultA = testDataA.donorControlModel.jacobian.subs(testDataA.symbolicData.getFoodWebDataSubsValues(testDataA.foodWebData))
resultB = testDataB.donorControlModel.jacobian.subs(testDataB.symbolicData.getFoodWebDataSubsValues(testDataB.foodWebData))

# compare both jacobians
printer.printMatrix("Manual:", resultA)
printer.printMatrix("Sympy:", resultB)
if (mo.equals(resultA, resultB)):
    print("Same output")
else:
    raise Exception("different output")

