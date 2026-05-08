from pathlib import Path

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

def get_file_path(filename: str) -> Path:
    return RESULTS_DIR / f"{filename}.txt"

def clear_file(filepath: Path) -> None:
    filepath.write_text("", encoding="utf-8")

def write_table(filename: str, result, t):
    filepath = get_file_path(filename)

    with open(filepath, "w", encoding="utf-8") as file:
        for time_value, row in zip(t, result):
            values = "\t".join(f"{x:.4f}" for x in row)
            file.write(f"{time_value:.4f}\t{values}\n")