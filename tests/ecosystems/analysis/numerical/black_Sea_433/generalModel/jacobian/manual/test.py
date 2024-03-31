import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--numerical",
    "--useManualJacobian",
    "--calculateGeneralModel",
    "--verbose-generalModelJacobian",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])