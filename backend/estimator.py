```python
import trimesh

# Define the density values for the filaments
DENSITIES = {
    "PLA": 1.24,  # g/cm³
    "PETG": 1.27  # g/cm³
}

class PrintEstimator:
    def __init__(self, model_path):
        # Load the model using trimesh
        self.mesh = trimesh.load_mesh(model_path)
        self.total_volume = sum([mesh.volume for mesh in self.mesh.geometry.values() if hasattr(mesh, 'volume')])

    def calculate_weight(self, filament_type, infill_percentage):
        """Calculate weight based on volume, filament type, and infill percentage."""
        density = DENSITIES.get(filament_type)
        if not density:
            raise ValueError(f"Unsupported filament type: {filament_type}")

        # Convert volume from mm³ to cm³
        volume_cm3 = self.total_volume * (infill_percentage / 100) / 1000
        weight = volume_cm3 * density
        return weight

    def calculate_pricing(self, weight, cost_price_per_kg, sale_price_per_kg):
        """Calculate the cost, sale price, and gross profit margin."""
        cost = (weight / 1000) * cost_price_per_kg
        sale_price = (weight / 1000) * sale_price_per_kg
        gross_profit_margin = ((sale_price - cost) / sale_price) * 100
        return cost, sale_price, gross_profit_margin

    def estimate(self, filament_type="PLA", infill_percentage=20, cost_price_per_kg=20, sale_price_per_kg=30):
        """Estimate the weight, dimensions, cost, sale price, and gross profit margin."""
        weight = self.calculate_weight(filament_type, infill_percentage)
        cost, sale_price, profit_margin = self.calculate_pricing(weight, cost_price_per_kg, sale_price_per_kg)

        return {
            "Weight (g)": weight,
            "Volume (cm³)": self.total_volume / 1000,
            "Cost Price ($)": cost,
            "Selling Price ($)": sale_price,
            "Gross Profit Margin (%)": profit_margin
        }
```