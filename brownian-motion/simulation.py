# pyright: reportUnusedCallResult=false
# pyright: reportUnknownMemberType=false
# pyright: reportAny=false
import numpy as np
import matplotlib.pyplot as plt
import os


def simulate_brownian_1d(
    n_steps: int = 1000, dt: float = 0.1
) -> tuple[np.ndarray, np.ndarray]:
    """
    Simulates a 1D Brownian motion.

    Args:
        n_steps (int): Number of time steps.
        dt (float): Time step size.

    Returns:
        t (ndarray): Time array.
        x (ndarray): Position array.
    """
    t = np.linspace(0, n_steps * dt, n_steps + 1)
    # Generate random steps from Normal(0, sqrt(dt))
    # W_t+1 = W_t + sqrt(dt) * Z, where Z ~ N(0, 1)
    steps: np.ndarray = np.sqrt(dt) * np.random.randn(n_steps)
    x: np.ndarray = np.concatenate(([0], np.cumsum(steps)))
    return t, x


def simulate_brownian_2d(
    n_steps: int = 1000, dt: float = 0.1
) -> tuple[np.ndarray, np.ndarray]:
    """
    Simulates a 2D Brownian motion.
    """
    # X and Y are independent 1D Brownian motions
    _, x = simulate_brownian_1d(n_steps, dt)
    _, y = simulate_brownian_1d(n_steps, dt)
    return x, y


def plot_1d(t: np.ndarray, x: np.ndarray, filename: str = "brownian_1d.png") -> None:
    plt.figure(figsize=(10, 6))
    plt.plot(t, x, lw=1)
    plt.title("1D Brownian Motion Simulation")
    plt.xlabel("Time (t)")
    plt.ylabel("Position (x)")
    plt.grid(True, alpha=0.3)
    plt.savefig(filename)
    plt.close()
    print(f"Saved 1D plot to {filename}")


def plot_2d(x: np.ndarray, y: np.ndarray, filename: str = "brownian_2d.png") -> None:
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, lw=0.8, alpha=0.8)
    plt.plot(x[0], y[0], "go", label="Start")
    plt.plot(x[-1], y[-1], "ro", label="End")
    plt.title("2D Brownian Motion Simulation")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axis("equal")
    plt.savefig(filename)
    plt.close()
    print(f"Saved 2D plot to {filename}")


if __name__ == "__main__":
    np.random.seed(42)  # For reproducibility

    # Ensure plots directory exists if we wanted one, but we'll save in current dir
    print("Simulating 1D Brownian Motion...")
    t, x = simulate_brownian_1d(n_steps=1000)
    filename_1d = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "brownian_1d.png"
    )
    plot_1d(t, x, filename_1d)

    print("Simulating 2D Brownian Motion...")
    bx, by = simulate_brownian_2d(n_steps=5000)
    filename_2d = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "brownian_2d.png"
    )
    plot_2d(bx, by, filename_2d)
