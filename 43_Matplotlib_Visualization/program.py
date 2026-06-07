# Chapter 43: Matplotlib for Data Visualization
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:12:15
# ============================================

try:
    import matplotlib
    matplotlib.use("Agg")  # Non-interactive backend for script
    import matplotlib.pyplot as plt
    import numpy as np
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("matplotlib not installed. Run: pip install matplotlib")

if HAS_MATPLOTLIB:
    import numpy as np
    
    # Use a built-in style
    plt.style.use("seaborn-v0_8")
    
    # -----------------------------------------------
    # SECTION 1: Line Plot
    # -----------------------------------------------
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle("Python Matplotlib Examples", fontsize=16, fontweight="bold")
    
    # Line plot
    x = np.linspace(0, 10, 100)
    axes[0,0].plot(x, np.sin(x), label="sin(x)", color="blue")
    axes[0,0].plot(x, np.cos(x), label="cos(x)", color="red", linestyle="--")
    axes[0,0].set_title("Line Plot: sin & cos")
    axes[0,0].set_xlabel("x")
    axes[0,0].set_ylabel("y")
    axes[0,0].legend()
    axes[0,0].grid(True)
    
    # Bar Chart
    categories = ["Python", "JavaScript", "Java", "C++", "Go"]
    popularity = [30, 25, 20, 15, 10]
    colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FECA57"]
    axes[0,1].bar(categories, popularity, color=colors, edgecolor="white")
    axes[0,1].set_title("Programming Language Popularity")
    axes[0,1].set_ylabel("Usage (%)")
    for i, (cat, val) in enumerate(zip(categories, popularity)):
        axes[0,1].text(i, val + 0.5, f"{val}%", ha="center", fontweight="bold")
    
    # Histogram
    np.random.seed(42)
    data = np.random.normal(170, 10, 500)
    axes[0,2].hist(data, bins=30, color="steelblue", edgecolor="white", alpha=0.8)
    axes[0,2].axvline(data.mean(), color="red", linestyle="--", label=f"Mean: {data.mean():.1f}")
    axes[0,2].set_title("Height Distribution (Normal)")
    axes[0,2].set_xlabel("Height (cm)")
    axes[0,2].set_ylabel("Frequency")
    axes[0,2].legend()
    
    # Scatter Plot
    x = np.random.randn(100)
    y = 2 * x + np.random.randn(100) * 0.5
    scatter = axes[1,0].scatter(x, y, c=x, cmap="viridis", alpha=0.7)
    plt.colorbar(scatter, ax=axes[1,0])
    axes[1,0].set_title("Scatter Plot with Color")
    axes[1,0].set_xlabel("X")
    axes[1,0].set_ylabel("Y")
    
    # Pie Chart
    sizes = [35, 25, 20, 15, 5]
    labels = ["Engineering", "Marketing", "Sales", "HR", "Other"]
    explode = (0.1, 0, 0, 0, 0)
    axes[1,1].pie(sizes, explode=explode, labels=labels, autopct="%1.1f%%",
                  shadow=True, startangle=90)
    axes[1,1].set_title("Department Distribution")
    
    # Box Plot
    np.random.seed(42)
    box_data = [np.random.normal(0, std, 100) for std in [1, 2, 3, 4]]
    bp = axes[1,2].boxplot(box_data, labels=["A", "B", "C", "D"], patch_artist=True)
    colors_box = ["lightblue", "lightgreen", "lightsalmon", "lightyellow"]
    for patch, color in zip(bp["boxes"], colors_box):
        patch.set_facecolor(color)
    axes[1,2].set_title("Box Plot: Data Distribution")
    axes[1,2].set_ylabel("Values")
    
    plt.tight_layout()
    plt.savefig("matplotlib_examples.png", dpi=100, bbox_inches="tight")
    plt.close()
    print("Chart saved as matplotlib_examples.png")
    
    # Time series example
    fig, ax = plt.subplots(figsize=(12, 5))
    dates = pd.date_range("2024-01-01", periods=365) if False else np.arange(365)
    values = np.cumsum(np.random.randn(365)) + 100
    ax.plot(np.arange(365), values, color="royalblue", linewidth=1.5)
    ax.fill_between(np.arange(365), values, alpha=0.3, color="royalblue")
    ax.set_title("Stock Price Simulation (365 days)", fontsize=14)
    ax.set_xlabel("Day")
    ax.set_ylabel("Price ($)")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig("timeseries.png", dpi=100)
    plt.close()
    print("Time series saved as timeseries.png")

print("\n" + "="*50)
print("Chapter 43 Complete!")
print("="*50)