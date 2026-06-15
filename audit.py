#!/usr/bin/env python3
"""
audit.py - Mechanical cross-check untuk quiz data-correct di lessons/*.html

Untuk setiap <div class="quiz-box" data-correct="N"> di lesson HTML:
- Ekstrak index N
- Cari button ke-N di <button class="opt"> dalam box tsb
- Print: file:line | data-correct | option text di index tsb

Jika data-correct menunjuk ke button yang teksnya BUKAN jawaban benar,
itu Class 6 transcription bug (seperti commit c043e8c untuk Q3 lesson 13).

Usage:
    python3 audit.py                    # audit semua lesson
    python3 audit.py lessons/0019.html  # audit 1 file
    python3 audit.py --verbose          # tampilkan semua opsi (bukan cuma di correct idx)

Exit code 0 = bersih, 1 = ada out-of-range, 2 = ada warning.
"""
import re
import sys
from pathlib import Path

LESSONS_DIR = Path(__file__).parent.resolve()


def audit_file(path: Path, verbose: bool = False) -> list:
    """Cari semua quiz-box di file HTML dan ekstrak opsi-nya."""
    text = path.read_text(encoding="utf-8")
    findings = []

    # Pattern 1: data-correct di tag pembuka div
    # Contoh: <div class="quiz-box" data-correct="2">
    box_pattern = re.compile(
        r'<div\s+class="quiz-box"\s+data-correct="(\d+)"\s*>',
        re.MULTILINE
    )

    matches = list(box_pattern.finditer(text))
    for i, match in enumerate(matches):
        idx = int(match.group(1))
        line_no = text[:match.start()].count('\n') + 1

        # Tentukan batas box ini (sampai box berikutnya atau akhir file)
        next_match = matches[i + 1] if i + 1 < len(matches) else None
        end = next_match.start() if next_match else len(text)
        box_content = text[match.end():end]

        # Ekstrak semua opsi dalam box.
        # Lessons 4-15 pakai: <button class="opt">
        # Lessons 1-3 (legacy) pakai: <div class="quiz-option" onclick="...">
        opt_pattern = re.compile(
            r'(?:<button\s+class="opt"[^>]*>|<div\s+class="quiz-option"[^>]*>)(.*?)</(?:button|div)>',
            re.DOTALL
        )
        options_raw = opt_pattern.findall(box_content)
        # Bersihkan tag HTML di dalam button & normalize whitespace
        options_clean = [
            re.sub(r'<[^>]+>', '', opt).strip()
            for opt in options_raw
        ]

        # Tentukan status
        if idx < 0:
            status = "NEG"
            option_text = "[NEGATIVE INDEX]"
        elif idx >= len(options_clean):
            status = "OOR"  # Out of range
            option_text = f"[OUT OF RANGE - only {len(options_clean)} options]"
        else:
            status = "OK"
            option_text = options_clean[idx]

        findings.append({
            'file': path.name,
            'line': line_no,
            'idx': idx,
            'n_options': len(options_clean),
            'option_text': option_text,
            'all_options': options_clean,
            'status': status,
        })

    return findings


def main():
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    args = [a for a in sys.argv[1:] if a not in ("--verbose", "-v")]

    if args:
        targets = [Path(p) for p in args]
    else:
        targets = sorted(LESSONS_DIR.glob("*.html"))

    # Filter master-cheatsheet (tidak ada quiz)
    targets = [t for t in targets if "cheatsheet" not in t.name and "README" not in t.name]

    if not targets:
        print("No lesson HTML files found.")
        return 0

    total_boxes = 0
    total_options = 0
    out_of_range = []
    warnings = []

    for path in targets:
        findings = audit_file(path, verbose=verbose)
        if not findings:
            continue

        for f in findings:
            total_boxes += 1
            total_options += f['n_options']

            if f['status'] == "OOR":
                out_of_range.append(f)
                marker = "FAIL"
            elif f['status'] == "NEG":
                out_of_range.append(f)
                marker = "FAIL"
            else:
                marker = "OK  "

            text_preview = f['option_text'][:80].replace('\n', ' ')
            print(f"{marker} {f['file']}:{f['line']:>4}  idx={f['idx']} ({f['n_options']} opts)  ->  {text_preview}")

            if verbose and f['status'] == 'OK':
                for j, opt in enumerate(f['all_options']):
                    tag = ">>>" if j == f['idx'] else "   "
                    print(f"        {tag} [{j}] {opt[:75].replace(chr(10), ' ')}")
                print()

    # Print summary
    print()
    print("=" * 70)
    print(f"Total quiz boxes: {total_boxes}")
    print(f"Total options:    {total_options}")
    print(f"Out of range:     {len(out_of_range)}")
    print(f"Avg options/box:  {total_options/total_boxes:.1f}" if total_boxes else "")

    if out_of_range:
        print()
        print("CRITICAL: Out-of-range data-correct values found!")
        for f in out_of_range:
            print(f"  {f['file']}:{f['line']}  idx={f['idx']} (only {f['n_options']} options)")

    if warnings:
        print()
        print("Warnings:")
        for w in warnings:
            print(f"  {w}")

    if out_of_range:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
