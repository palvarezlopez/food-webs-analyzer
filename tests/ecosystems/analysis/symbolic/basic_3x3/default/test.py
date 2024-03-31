import foodWebsAnalyzer

# declare input-output parameters
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])