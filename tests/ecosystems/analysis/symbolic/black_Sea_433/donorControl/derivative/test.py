import foodWebsAnalyzer

# declare input-output parameters
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--calculateDonorControlModel",
    "--verbose-donorControlDerivative",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])