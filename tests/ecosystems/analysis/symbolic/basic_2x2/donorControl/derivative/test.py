import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--calculateDonorControlModel",
    "--verbose-donorControlDerivative",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])