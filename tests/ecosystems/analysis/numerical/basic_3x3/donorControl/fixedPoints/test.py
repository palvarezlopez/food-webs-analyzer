import foodWebsAnalyzer

# declare input-output parameters
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose-inputFile",
    "--numerical",
    "--calculateDonorControlModel",
    "--verbose-donorControlFixedPoints",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])