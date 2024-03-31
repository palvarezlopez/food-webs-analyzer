import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--numerical",
    "--calculateDonorControlModel",
    "--verbose-donorControlJacobian",
    "--useSympyJacobian",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])