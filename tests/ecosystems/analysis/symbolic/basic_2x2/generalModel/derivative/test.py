import foodWebsAnalyzer

# declare food web analyzer instance
foodWebsAnalyzer.FoodWebsAnalyzer(["--dataFolder", ".",
    "--verbose-inputFile",
    "--calculateGeneralModel",
    "--verbose-generalModelDerivative",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])