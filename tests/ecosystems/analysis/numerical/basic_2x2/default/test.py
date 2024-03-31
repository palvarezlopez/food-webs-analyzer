import foodWebsAnalyzer

# declare input-output parameters
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
     "--verbose",
     "--numerical",
     "--outputPlainFile", "plainOutput.txt",
     "--outputLatexFile", "latexOutput"
])