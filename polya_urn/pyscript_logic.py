import numpy as np
import matplotlib.pyplot as plt
from polya_urn import PolyaUrn
from pyodide.ffi import create_proxy
from pyscript import display, document
import js

def run_simulation(event=None):
    # Get values from inputs
    red = int(document.querySelector("#red").value)
    green = int(document.querySelector("#green").value)
    add = int(document.querySelector("#add").value)
    steps = int(document.querySelector("#steps").value)
    trials = int(document.querySelector("#trials").value)

    # Clear previous plot
    plot_div = document.querySelector("#plot")
    plot_div.innerHTML = '<div class="loading">Simulating...</div>'

    # Run trials
    all_histories = []
    for _ in range(trials):
        urn = PolyaUrn(red, green, add)
        history = urn.simulate(steps)
        all_histories.append(history)

    # Dynamic figsize based on window width
    window_width = js.window.innerWidth
    if window_width < 640: # Match CSS media query
        fig_size = (6.5, 4.5) # Stable size for scrollable mobile view
    else:
        fig_size = (10, 6) # Larger size for desktop

    # Visualization
    fig, ax = plt.subplots(figsize=fig_size, constrained_layout=True)
    
    for hist in all_histories:
        ax.plot(hist, alpha=0.5, linewidth=1)
    
    ax.set_title(f"Proportion of Red Balls ({trials} Trials)")
    ax.set_xlabel("Step")
    ax.set_ylabel("Proportion Red")
    ax.set_ylim(-0.02, 1.02)
    ax.axhline(y=red/(red+green), color='k', linestyle='--', alpha=0.5, label='Initial Proportion')
    ax.legend(loc='upper right', fontsize='x-small')
    ax.grid(True, alpha=0.3)

    # Clear "Simulating..." and display plot
    plot_div.innerHTML = ""
    display(fig, target="plot")

# Initial run
run_simulation()
