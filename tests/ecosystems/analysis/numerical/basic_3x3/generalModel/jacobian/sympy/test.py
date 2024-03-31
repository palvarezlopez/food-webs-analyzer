import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--calculateGeneralModel",
    "--numerical",
    "--verbose-generalModelJacobian",
    "--useSympyJacobian",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])