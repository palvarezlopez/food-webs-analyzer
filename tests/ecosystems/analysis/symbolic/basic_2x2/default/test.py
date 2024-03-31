import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer([
    "--dataFolder", ".",
    "--verbose",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])