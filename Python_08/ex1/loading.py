import importlib
import sys


def check_dependencies() -> bool:
    required_packages: dict[str, str] = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
    }

    missing: list[str] = []
    for package, description in required_packages.items():
        try:
            mod = importlib.import_module(package)
            print(f"[OK] {package} ({mod.__version__}) - {description}")
        except ImportError:
            print(f"[MISSING] {package} - NOT AVAILABLE")
            missing.append(package)
    if missing:
        print("\nMissing dependencies detected.")
        print("Install with pip:")
        print(" pip install -r requirements.txt")
        print("\n Or install with Poetry:")
        print(" poetry install")
        return False
    return True


def test_matplotlib() -> None:
    import matplotlib  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import requests  # type: ignore

    matplotlib.use("Agg")

    data: None | list[int] = None
    source: str = "simulated (numpy)"

    try:
        print("Accessing quantum vaccum fluctuations...")
        resp = requests.get(
            "https://qrng.anu.edu.au/API/jsonI.php?length=1000&type=uint8",
            timeout=10,
        )
        data = resp.json()["data"]
        source = "LIVE QUANTUM RANDOMNESS (LIVE API)"
        print("Connection established. Downloading...")
    except Exception:
        print("Signal lost. using local simulation...")
        data = np.random.exponential(scale=1.5, size=1000).tolist()

    df = pd.DataFrame({"intensity": data, "time": np.arange(1000)})
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(12, 6), facecolor="#050505")
    ax.set_facecolor("#050505")
    ax.fill_between(df["time"], df["intensity"], color="lime", alpha=0.15)
    ax.plot(
        df["time"], df["intensity"], color="lime", linewidth=0.7, alpha=0.8
    )
    plt.title(
        "QUANTUM RANDOMNESS ANALYSIS",
        loc="left",
        fontsize=16,
        color="lime",
        pad=20,
        fontweight="normal",
        family="monospace",
    )
    plt.xlabel(
        "TEMPORAL SEQUENCE",
        loc="right",
        color="#666666",
        fontsize=9,
        family="monospace",
    )
    plt.ylabel(
        "AMPLITUDE", loc="top", color="#666666", fontsize=9, family="monospace"
    )
    plt.text(
        0.02,
        0.95,
        f"Source: {source}",
        transform=ax.transAxes,
        color="lime",
        fontsize=8,
        family="monospace",
        verticalalignment="top",
        bbox=dict(
            boxstyle="square,pad=0.5",
            facecolor="none",
            edgecolor="lime",
            alpha=0.3,
        ),
    )
    plt.tight_layout()
    plt.savefig("matrix_analysis.png", facecolor=fig.get_facecolor(), dpi=200)
    plt.close()


if __name__ == "__main__":
    print("LOADING STATUS: Loading programs...")

    if not check_dependencies():
        sys.exit(1)
    print("\nAnalyzing Matrix data...")
    test_matplotlib()
    print("Processing 1000 data points...")
    print("Generating visualization...")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")
