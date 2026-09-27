"""Registry for Electro-Py tools.

To add a calculator to a named tab, add one Tool(...) entry below.
The launcher automatically discovers other .py files on the All Tools tab.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Tool:
    name: str
    module: str
    category: str
    description: str = ""


TOOLS = [
    Tool("Ohm's Law Calculator", "Ohms_Law_Singlecalc_v2", "Ohm's Law", "Voltage/current/resistance/power calculations."),
    Tool("Resistance & Power", "RPcalc", "Ohm's Law"),
    Tool("Current & Power", "IPcalc", "Ohm's Law"),
    Tool("Voltage & Power", "VPcalc", "Ohm's Law"),
    Tool("Voltage + Current → Ohms + Watts", "V_I_to_Ohms_Watts", "Ohm's Law"),
    Tool("Parallel Resistor", "select_resistor", "Ohm's Law"),
    Tool("Voltage Divider", "Vdiv", "Ohm's Law"),
    Tool("LM317T Regulator", "LM317T_calc", "Ohm's Law"),

    Tool("Scientific Calculator", "SciCalcV3", "Calculators"),
    Tool("Custom Step Calculator", "Custom_Calc", "Calculators"),
    Tool("Spreadsheet-like Calculator", "Spreadsheet_like_Calc", "Calculators"),
    Tool("Engineering Math", "Eng_MathapstdlibV1", "Calculators"),
    Tool("Vector Math", "Vector_math_W_GUI", "Calculators"),

    Tool("Decimal → Base 2–36", "DEC_2_36", "Number Bases"),
    Tool("Hex → Dec/Oct/Bin", "FHEX", "Number Bases"),
    Tool("Octal → Dec/Hex/Bin", "FOCT", "Number Bases"),
    Tool("Binary → Dec/Oct/Hex", "FBIN", "Number Bases"),
    Tool("Decimal → Binary", "Dec2Bin", "Number Bases"),
    Tool("Base Number Converter", "base_number converter", "Number Bases"),

    Tool("LC Resonant Frequency", "LC_Freq", "Frequency / RF"),
    Tool("Find C from Frequency + L", "Freq_L_find_C", "Frequency / RF"),
    Tool("Find L from Frequency + C", "Freq_C_find_L", "Frequency / RF"),
    Tool("Frequency → Wavelength", "Frequency2Meters", "Frequency / RF"),
    Tool("Wavelength → Frequency", "LenghttoFreq", "Frequency / RF"),
    Tool("dBm → Watts / Volts", "dbm2w_v_rmsv2", "Frequency / RF"),
    Tool("mW → dBm", "mW2dBm", "Frequency / RF"),
    Tool("VSWR → Return Loss", "vswer_to_Returnlossv4", "Frequency / RF"),

    Tool("LED Current-limit Resistor", "LED_Current_Limit_calc", "Components"),
    Tool("Resonant Calculator", "Resonant_Calculator", "Components"),

    Tool("Temperature Converter", "temperature_converter", "Unit Conversion"),
    Tool("Miles ↔ Kilometers", "km_mi", "Unit Conversion"),
    Tool("Inch / cm / mm", "inch_cm_mm", "Unit Conversion"),
    Tool("General Unit Converter", "unit_convert", "Unit Conversion"),

    Tool("Sine Wave", "sinewave", "Graphs"),
    Tool("Waveform 1", "waveform1", "Graphs"),
    Tool("Waveform 2", "waveform2", "Graphs"),
    Tool("Waveform 3", "waveform3", "Graphs"),
    Tool("Waveform 4", "waveform4", "Graphs"),
    Tool("Waveform 5", "waveform5", "Graphs"),
    Tool("Multi-variable Graph Calculator", "math Multi_var Graph_calc", "Graphs"),

    Tool("Character / Symbol Pad", "symbol_pad_JH", "Utilities"),
    Tool("Engineering Spec ± Calculator", "spec", "Utilities"),
    Tool("Information Section", "Info_Section", "Utilities"),
]
