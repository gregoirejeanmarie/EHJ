import os
import sys
from pathlib import Path

if len(sys.argv) < 3:
    print("python3 trouver_patient.py <\F:\SyneTArc> <BOUCHOMS>")
    exit(1)
folder_name = "\F:\SyneTArc"
patient_name = "BOUCHOMS"

for filename in Path(folder_name).rglob('*.IDX'):
    with open(filename) as f:
        if patient_name in f.read():
            print("filename")