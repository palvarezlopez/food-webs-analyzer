import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose",
    "--numerical",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])