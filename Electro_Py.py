#!/usr/bin/env python3
"""Electro-Py Engineering & Math Toolkit.

A stable launcher for the original collection of calculators.  Each tool is
started in its own Python process, so a calculator can close or fail without
bringing down the main application.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import tkinter as tk
from tkinter import messagebox, ttk

from calculator_registry import TOOLS, Tool

APP_DIR = Path(__file__).resolve().parent
EXCLUDED = {
    Path(__file__).stem,
    "calculator_registry",
    "GENERIC_UNIT_COMBOBOX_FULLRANGE_TEMPLATE",
}


class ElectroPyApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Electro-Py Engineering & Math Toolkit")
        self.geometry("1120x760")
        self.minsize(850, 560)
        self._processes: list[subprocess.Popen] = []
        self.search_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Ready")
        self._build_ui()

    def _build_ui(self) -> None:
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        header = ttk.Frame(self, padding=(12, 10))
        header.grid(row=0, column=0, sticky="ew")
        header.columnconfigure(0, weight=1)
        ttk.Label(header, text="Electro-Py", font=("TkDefaultFont", 20, "bold")).grid(row=0, column=0, sticky="w")
        ttk.Label(header, text="Engineering, electronics, RF, math, graphing and conversion tools").grid(row=1, column=0, sticky="w")
        ttk.Button(header, text="About", command=self._about).grid(row=0, column=1, rowspan=2, padx=(10, 0))

        notebook = ttk.Notebook(self)
        notebook.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 8))

        categories = []
        for tool in TOOLS:
            if tool.category not in categories:
                categories.append(tool.category)
        for category in categories:
            items = [t for t in TOOLS if t.category == category and self._module_exists(t.module)]
            if items:
                notebook.add(self._tool_page(notebook, items), text=category)

        notebook.add(self._all_tools_page(notebook), text="All Tools")
        notebook.add(self._reference_page(notebook), text="Reference")

        status = ttk.Label(self, textvariable=self.status_var, relief="sunken", anchor="w", padding=(8, 4))
        status.grid(row=2, column=0, sticky="ew")

    def _tool_page(self, parent: ttk.Notebook, tools: list[Tool]) -> ttk.Frame:
        outer = ttk.Frame(parent)
        canvas = tk.Canvas(outer, highlightthickness=0)
        scrollbar = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
        inner = ttk.Frame(canvas, padding=12)
        inner.bind("<Configure>", lambda _e: canvas.configure(scrollregion=canvas.bbox("all")))
        window = canvas.create_window((0, 0), window=inner, anchor="nw")
        canvas.bind("<Configure>", lambda e: canvas.itemconfigure(window, width=e.width))
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        inner.columnconfigure(0, weight=1)

        for row, tool in enumerate(tools):
            box = ttk.LabelFrame(inner, text=tool.name, padding=10)
            box.grid(row=row, column=0, sticky="ew", pady=5)
            box.columnconfigure(0, weight=1)
            desc = tool.description or f"Open {tool.name}."
            ttk.Label(box, text=desc, wraplength=720).grid(row=0, column=0, sticky="w")
            ttk.Button(box, text="Open", command=lambda t=tool: self.launch(t.module, t.name)).grid(row=0, column=1, padx=(12, 0))
        return outer

    def _all_tools_page(self, parent: ttk.Notebook) -> ttk.Frame:
        frame = ttk.Frame(parent, padding=12)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)
        ttk.Label(frame, text="Search every Python tool in this project. This list is discovered automatically.").grid(row=0, column=0, sticky="w")
        entry = ttk.Entry(frame, textvariable=self.search_var)
        entry.grid(row=1, column=0, sticky="ew", pady=(8, 8))

        self.all_list = tk.Listbox(frame, activestyle="dotbox")
        self.all_list.grid(row=2, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.all_list.yview)
        scroll.grid(row=2, column=1, sticky="ns")
        self.all_list.configure(yscrollcommand=scroll.set)
        self.all_list.bind("<Double-1>", lambda _e: self._launch_selected())
        ttk.Button(frame, text="Open Selected Tool", command=self._launch_selected).grid(row=3, column=0, sticky="e", pady=(8, 0))

        self.search_var.trace_add("write", lambda *_: self._refresh_all_tools())
        self._refresh_all_tools()
        return frame

    def _reference_page(self, parent: ttk.Notebook) -> ttk.Frame:
        frame = ttk.Frame(parent, padding=12)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        text = tk.Text(frame, wrap="word", height=20)
        text.grid(row=0, column=0, sticky="nsew")
        reference = (
            "ADDING A NEW CALCULATOR\n\n"
            "1. Put the new .py file in this Electro-Py folder.\n"
            "2. It will immediately appear on the All Tools tab.\n"
            "3. To give it a permanent category tab, add one Tool(...) line to calculator_registry.py.\n\n"
            "DESIGN NOTE\n\n"
            "Calculators are deliberately launched as separate processes. This keeps old standalone Tkinter programs compatible and prevents one calculator from freezing or closing the main application.\n\n"
            "A future calculator can still be refactored into classes/functions at any time without changing this launcher."
        )
        text.insert("1.0", reference)
        text.configure(state="disabled")
        return frame

    def _discover_modules(self) -> list[str]:
        return sorted(
            p.stem for p in APP_DIR.glob("*.py")
            if p.stem not in EXCLUDED and not p.name.startswith(".")
        )

    def _refresh_all_tools(self) -> None:
        needle = self.search_var.get().strip().lower()
        self.all_list.delete(0, tk.END)
        for module in self._discover_modules():
            if not needle or needle in module.lower():
                self.all_list.insert(tk.END, module)

    def _launch_selected(self) -> None:
        selection = self.all_list.curselection()
        if not selection:
            messagebox.showinfo("Select a tool", "Select a tool from the list first.", parent=self)
            return
        module = self.all_list.get(selection[0])
        self.launch(module, module.replace("_", " "))

    @staticmethod
    def _module_exists(module: str) -> bool:
        return (APP_DIR / f"{module}.py").is_file()

    def launch(self, module: str, display_name: str) -> None:
        path = APP_DIR / f"{module}.py"
        if not path.is_file():
            messagebox.showerror("Tool not found", f"The calculator file is missing:\n{path.name}", parent=self)
            return
        try:
            process = subprocess.Popen([sys.executable, str(path)], cwd=str(APP_DIR))
        except OSError as exc:
            messagebox.showerror("Could not start tool", str(exc), parent=self)
            return
        self._processes = [p for p in self._processes if p.poll() is None]
        self._processes.append(process)
        self.status_var.set(f"Opened: {display_name}")

    def _about(self) -> None:
        available = len(self._discover_modules())
        messagebox.showinfo(
            "About Electro-Py",
            f"Electro-Py Engineering & Math Toolkit\n\n{available} Python tools detected.\n"
            "The rebuilt launcher uses only the Python standard library.",
            parent=self,
        )


def main() -> None:
    app = ElectroPyApp()
    app.mainloop()


if __name__ == "__main__":
    main()
