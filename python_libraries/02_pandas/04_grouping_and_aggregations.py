import pandas as pd

# Multi-particle tracking dataset
df = pd.DataFrame(
    {
        "Particle_ID": ["P1", "P1", "P1", "P2", "P2", "P3", "P3", "P3"],
        "Time_s": [0, 1, 2, 0, 1, 0, 1, 2],
        "Velocity_m_s": [10.2, 12.5, 11.8, 5.1, 4.8, 22.1, 21.9, 23.0],
        "Mass_kg": [1.0, 1.0, 1.0, 2.0, 2.0, 0.5, 0.5, 0.5],
    }
)

print("Particle Dataset")
print(df)

# 1. Grouping by Particle_ID and calculating mean velocity
grouped = df.groupby("Particle_ID")

print("\nAverage Velocity per Particle")
print(grouped["Velocity_m_s"].mean())

# 2. Applying Multiple Aggregations simultaneously
stats = grouped["Velocity_m_s"].agg(["mean", "std", "min", "max"])
print("\nVelocity Summary Statistics per Particle")
print(stats)

# 3. Merging (Joining) Datasets
particle_metadata = pd.DataFrame(
    {
        "Particle_ID": ["P1", "P2", "P3"],
        "Material": ["Copper", "Aluminum", "Silicon"],
    }
)

merged_df = pd.merge(df, particle_metadata, on="Particle_ID")
print("\nMerged Dataset with Metadata")
print(merged_df.head(4))
