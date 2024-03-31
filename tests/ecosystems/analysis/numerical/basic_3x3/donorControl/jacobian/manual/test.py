import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--numerical",
    "--useManualJacobian",
    "--calculateDonorControlModel",
    "--verbose-donorControlJacobian",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])