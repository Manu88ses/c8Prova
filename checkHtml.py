"""
Clouds & Cims Consulting — HTML Quick Check


Eina interna per fer una validació mínima d'un fitxer HTML abans de desplegar-lo.
Comprova elements bàsics d'estructura i genera un informe textual.
"""


from __future__ import annotations


import argparse
from datetime import datetime
from pathlib import Path




def contains_tag(text: str, tag: str) -> bool:
   # Simple case-insensitive substring check for an HTML tag
   return tag.lower() in text.lower()






parser = argparse.ArgumentParser(description="Minimal HTML structure checker.")
parser.add_argument(
   "file",
   nargs="?",
   default="index.html",
   help="",
)
parser.add_argument(
   "-o",
   "--output",
   default="html_quickcheck_report.txt",
   help="Output report file (default: html_quickcheck_report.txt)",
)
args = parser.parse_args()


target = Path(args.file)


lines = []
lines.append("Clouds & Cims Consulting — HTML Quick Check")
lines.append(f"Data i hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
lines.append(f"Fitxer analitzat: {target}")
lines.append("-" * 50)


if not target.exists():
   lines.append("RESULTAT: ERROR")
   lines.append("Motiu: El fitxer no existeix.")
   report = "\n".join(lines) + "\n"
   Path(args.output).write_text(report, encoding="utf-8")
   print(f"[ERROR] Fitxer no trobat. Informe generat: {args.output}")


text = target.read_text(encoding="utf-8", errors="replace")


checks = [
   ("DOCTYPE HTML", "<!doctype html"),
   ("Etiqueta <html>", "<html"),
   ("Etiqueta <head>", "<head"),
   ("Etiqueta <body>", "<body"),
   ("Etiqueta <title> (recomanat)", "<title"),
]


ok_count = 0
for label, needle in checks:
   ok = contains_tag(text, needle)
   status = "OK" if ok else "MANCANT"
   lines.append(f"{label}: {status}")
   ok_count += 1 if ok else 0


lines.append("-" * 50)


# Considerem "PASSA" si té DOCTYPE + html + head + body (4 primers checks)
mandatory_ok = (
   contains_tag(text, "<!doctype html")
   and contains_tag(text, "<html")
   and contains_tag(text, "<head")
   and contains_tag(text, "<body")
)


if mandatory_ok:
   lines.append("RESULTAT: PASSA (estructura mínima correcta)")
   if not contains_tag(text, "<title"):
       lines.append("AVÍS: Falta <title> (no és crític, però és recomanat).")
else:
   lines.append("RESULTAT: NO PASSA (estructura mínima incompleta)")
   lines.append("Acció suggerida: revisi el DOCTYPE i les etiquetes bàsiques.")


report = "\n".join(lines) + "\n"
Path(args.output).write_text(report, encoding="utf-8")
print(f"[OK] Informe generat: {args.output}")
