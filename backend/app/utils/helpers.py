from pathlib import Path
import json

from starlette.responses import FileResponse

RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

def get_file_path(filename: str) -> Path:
    return RESULTS_DIR / f"{filename}.txt"

def clear_file(filepath: Path) -> None:
    filepath.write_text("", encoding="utf-8")


def write_table(filename: str, simulation: dict, params: dict = None):
    filepath = get_file_path(filename)

    t = simulation["t"]
    result = simulation["result"]
    eps_inf = simulation["eps_inf"]
    eps_prod = simulation["eps_prod"]

    with open(filepath, "w", encoding="utf-8") as file:

        if params:
            file.write("=== ПАРАМЕТРЫ ===\n")
            file.write(
                json.dumps(
                    params,
                    indent=2,
                    ensure_ascii=False
                )
            )
            file.write("\n\n")

        file.write("=== РЕЗУЛЬТАТЫ ===\n")
        file.write(
            "t\tT\tL\tI\tV\tC\teps_inf\teps_prod\n"
        )

        for ti, row, ei, ep in zip(
            t,
            result,
            eps_inf,
            eps_prod
        ):
            file.write(
                f"{ti:.4f}\t"
                f"{row[0]:.4f}\t"
                f"{row[1]:.4f}\t"
                f"{row[2]:.4f}\t"
                f"{row[3]:.4f}\t"
                f"{row[4]:.4f}\t"
                f"{ei:.4f}\t"
                f"{ep:.4f}\n"
            )

def download_result():
    file_path = RESULTS_DIR / "result.txt"
    if not file_path.exists():
        return {"error": "File not found"}
    return FileResponse(
        path=file_path,
        filename="simulation_results.txt",
        media_type="text/plain"
    )
