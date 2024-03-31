import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--calculateDonorControlModel",
    "--verbose-donorControlFixedPoints",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])