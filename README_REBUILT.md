# Electro-Py Rebuilt

Start the application with:

```bash
python3 Electro_Py.py
```

or:

```bash
python3 START_ELECTRO_PY.py
```

## Why this version is easier to maintain

The original calculators remain separate files, but the main program no longer imports and executes them with `runpy`. Each calculator opens in a separate Python process. That makes old Tkinter scripts much safer to launch from one application.

The visible categories are stored in `calculator_registry.py`. To add a new calculator:

1. Copy the new Python file into the Electro-Py folder.
2. It automatically appears under **All Tools**.
3. Optionally add one `Tool(...)` line in `calculator_registry.py` to place it on a named tab.

## Repairs in this rebuild

- Replaced the fragile original launcher with a class-based Tkinter launcher.
- Added automatic discovery/search of Python tools.
- Removed dependence on missing launcher targets.
- Repaired `V_I_to_Ohms_Watts.py`, including its indentation failure and zero-current handling.
- Corrected invalid `is` comparisons in `Vector_math_W_GUI.py`.
- Kept the project standard-library friendly.
- Preserved the original source files for calculators so they can be modernized one at a time.
