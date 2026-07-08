from pathlib import Path
FORBIDDEN = [
    "TODO",
    "console.log",
    "print("
]
MAX_LINES = 500

violations = []

for file in Path(".").rglob("*"):
    if file.is_dir():
        continue
    if ".git" in str(file):
        continue
    try:
        text = file.read_text(encoding="utf-8")
    except:
        continue
    lines = text.splitlines()
    if len(lines) > MAX_LINES:
        violations.append(
            f"{file}: exceeds {MAX_LINES} lines"
        )
    for number, line in enumerate(lines, start=1):
        for keyword in FORBIDDEN:
            if keyword in line:
                violations.append(
                    f"{file}:{number} contains '{keyword}'"
                )

if violations:
    print("Review Failed\n")
    for v in violations:
        print(v)
    exit(1)
print("Review Passed")