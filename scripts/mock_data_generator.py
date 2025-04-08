# 🧪 Synthetic Race Data Generator and Saver

import pandas as pd
import numpy as np
import os

def generate_mock_race_data(seed=55, num_drivers=20, save=True):
    """Generate synthetic race data and optionally save to baseline input CSV."""
    np.random.seed(seed)
    drivers = [f'Driver_{i+1}' for i in range(num_drivers)]
    grid_positions = list(range(1, num_drivers + 1))
    true_podium = [1 if i < 3 else 0 for i in np.random.permutation(num_drivers)]  # Random podium

    df = pd.DataFrame({
        'Driver': drivers,
        'GridPosition': grid_positions,
        'Podium': true_podium
    })

    if save:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        save_path = os.path.join(base_dir, 'data', 'processed', 'v0_1_0')
        os.makedirs(save_path, exist_ok=True)
        full_path = os.path.join(save_path, 'baseline_input.csv')
        df.to_csv(full_path, index=False)
        print(f"✅ Saved synthetic baseline input to: {full_path}")
    
    return df

# Example usage
if __name__ == "__main__":
    df = generate_mock_race_data()
    print(df.head())
