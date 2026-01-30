from pathlib import Path

README_PATH = Path("2_OOPC.md")
FILES = sorted(Path("Files/2_OOPC/").glob("*.md"))

def main():
    if not README_PATH.exists():
        raise FileNotFoundError("2_OOPC.md not found")

    toc_content = ("# Table of Contents" + "\n\n")
    # Generate TOC -------------------------------------------------------------------------
    for file in FILES:
        if not file.exists():
            raise FileNotFoundError(f"Missing chapter file: {file}")

        base = file.stem
        parts = base.split("_")

        # "2 Abc Xyz"
        first = f"{int(parts[0])}. {' '.join(parts[1:])}"
        # "abc-xyz"
        second = "-".join(parts[1:]).lower()

        toc_content += f"[{first}](#{second})" + "\n\n"

    # Generate Content ----------------------------------------------------------------------
    chapters_content = []
    for file in FILES:
        if not file.exists():
            raise FileNotFoundError(f"Missing chapter file: {file}")
        chapters_content.append(file.read_text(encoding="utf-8").rstrip() + "\n")

    # Merge Them and Create Folder Readme ----------------------------------------------------------
    new_readme = (toc_content + "\n".join(chapters_content))
    README_PATH.write_text(new_readme, encoding="utf-8")

if __name__ == "__main__":
    main()