import foodWebsAnalyzer

# declare input-output parameters
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--useManualJacobian",
    "--calculateDonorControlModel",
    "--verbose-donorControlJacobian",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])