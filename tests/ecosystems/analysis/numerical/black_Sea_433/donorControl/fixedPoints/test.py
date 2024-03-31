import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--numerical",
    "--calculateDonorControlModel",
    "--verbose-donorControlFixedPoints",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])