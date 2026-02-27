# Probability Experiments: Pólya's Urn

This repository explores various probability experiments, starting with **Pólya's Urn**.

## Pólya's Urn Experiment

The Pólya's Urn is a type of statistical model used as an idealized representation of certain real-world processes. It demonstrates "path dependence" and how small initial differences can lead to vastly different long-term outcomes.

### How it works
1. Start with an urn containing $R$ red balls and $G$ green balls.
2. At each step, draw a ball at random from the urn.
3. Observe its color and return it to the urn, along with $c$ additional balls of the same color.
4. Repeat.

### Key Observation
The proportion of red balls in the urn eventually converges to a random variable that follows a Beta distribution $\text{Beta}(R/c, G/c)$.

## Interactive Visualization

You can view the interactive simulation online via PyScript.

[Link to GitHub Pages (to be set up)]

## Local Development

### Prerequisites
- Python 3.11+
- python3-venv

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/li-kuan-gi/probability-experiments.git
   cd probability-experiments
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Linux/macOS
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Simulations
You can run a local simulation and generate a plot:
```bash
python -m polya_urn.simulation --red 1 --green 1 --add 1 --trials 200 --steps 500
```
This will save a plot named `polya_simulation.png` in the `polya_urn/` directory.
