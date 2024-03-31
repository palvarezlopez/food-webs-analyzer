import foodWebsAnalyzer

# declare input-output parameters
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--calculateDonorControlModel",
    "--verbose-donorControlJacobian",
    "--useSympyJacobian",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])