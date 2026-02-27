import numpy as np


class PolyaUrn:
    def __init__(self, initial_red: int, initial_green: int, add_count: int) -> None:
        self.initial_red: int = initial_red
        self.initial_green: int = initial_green
        self.red: int = initial_red
        self.green: int = initial_green
        self.add_count: int = add_count
        self.history: list[float] = []

    def step(self) -> None:
        """Perform one draw and update."""
        total: int = self.red + self.green
        prob_red: float = self.red / total

        # Draw
        draw_red: bool = np.random.random() < prob_red

        # Update
        if draw_red:
            self.red += self.add_count
        else:
            self.green += self.add_count

    def simulate(self, n_steps: int) -> np.ndarray:
        """Run for n_steps and return the history of red proportions."""
        self.red = self.initial_red
        self.green = self.initial_green
        self.history = [self.red / (self.red + self.green)]

        for _ in range(n_steps):
            self.step()
            self.history.append(self.red / (self.red + self.green))

        return np.array(self.history)
