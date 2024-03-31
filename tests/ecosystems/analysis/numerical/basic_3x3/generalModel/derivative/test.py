import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer(["--dataFolder", ".",
    "--verbose-inputFile",
    "--calculateGeneralModel",
    "--numerical",
    "--verbose-generalModelDerivative",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])