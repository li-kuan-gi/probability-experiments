# pyright: reportUnusedCallResult=false
# pyright: reportUnknownMemberType=false
# pyright: reportAny=false
import numpy as np
import matplotlib.pyplot as plt
import argparse
import os
from .polya_urn import PolyaUrn

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate Polya's Urn")
    parser.add_argument("--red", type=int, default=1, help="Initial red balls")
    parser.add_argument("--green", type=int, default=1, help="Initial green balls")
    parser.add_argument("--add", type=int, default=1, help="Balls to add per step")
    parser.add_argument("--steps", type=int, default=500, help="Steps per trial")
    parser.add_argument("--trials", type=int, default=200, help="Number of trials")
    args = parser.parse_args()

    red: int = args.red
    green: int = args.green
    add: int = args.add
    steps: int = args.steps
    trials: int = args.trials

    print(
        f"Running Polya's Urn Simulation: Red={red}, Green={green}, Add={add}, Steps={steps}, Trials={trials}"
    )

    all_histories: list[np.ndarray] = []
    final_proportions: list[float] = []

    for i in range(trials):
        urn: PolyaUrn = PolyaUrn(red, green, add)
        history: np.ndarray = urn.simulate(steps)
        all_histories.append(history)
        final_proportions.append(history[-1])

    # Visualization
    plt.figure(figsize=(12, 5))

    # Trajectories
    plt.subplot(1, 2, 1)
    for hist in all_histories[:50]:  # Plot first 50 trials to avoid clutter
        plt.plot(hist, alpha=0.3, linewidth=1)
    plt.title(f"Proportion of Red Balls (First 50/{trials} Trials)")
    plt.xlabel("Step")
    plt.ylabel("Proportion Red")
    plt.ylim(0, 1)
    plt.axhline(
        y=red / (red + green),
        color="k",
        linestyle="--",
        alpha=0.5,
        label="Initial Proportion",
    )
    plt.legend()

    # Histogram of final proportions
    plt.subplot(1, 2, 2)
    plt.hist(
        final_proportions,
        bins=30,
        density=True,
        alpha=0.7,
        color="purple",
        edgecolor="black",
    )
    plt.title("Distribution of Final Red Proportions")
    plt.xlabel("Proportion Red")
    plt.xlim(0, 1)

    # Beta distribution theory overlay
    # For Polya's urn starting with R red and G green, limit is Beta(R/c, G/c)
    # where c is the number of balls added per step
    from scipy.stats import beta

    x: np.ndarray = np.linspace(0, 1, 100)
    alpha: float = red / add
    beta_param: float = green / add
    y: np.ndarray = beta.pdf(x, alpha, beta_param)
    plt.plot(x, y, "r-", linewidth=2, label=f"Beta({alpha:.1f}, {beta_param:.1f})")
    plt.legend()

    plt.tight_layout()
    output_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "polya_simulation.png"
    )
    plt.savefig(output_file)
    print(f"Simulation complete. Plot saved to {output_file}")
    print(f"Mean final proportion: {np.mean(final_proportions):.4f}")
    print(f"Expected mean: {red / (red + green):.4f}")
