import foodWebsAnalyzer

# declare input-output parameters
foodWebsAnalyzer.FoodWebsAnalyzer(["--dataFolder", ".",
    "--verbose-inputFile",
    "--calculateGeneralModel",
    "--verbose-generalModelDerivative",
    "--outputPlainFile", "plainOutput.txt",
    "--outputLatexFile", "latexOutput"
])