import json

from SolarPlant import SolarPanel
from OilPlant import OilGenerator
from CoalPlant import CoalGenerator
from WindFarm import WindTurbine

def charge_battery(energy: dict = {}):

    # Load file
    with open(".battery", "r") as fh:
        data = json.load(fh)

    # Aggregate generated energy
    data["solar"] += energy["solar"]
    data["wind"] += energy["wind"]
    data["oil"] += energy["oil"]
    data["coal"] += energy["coal"]

    # Write data
    with open(".battery", "w") as fh:
        json.dump(data, fh)

def main():
    
    # Examples of renewables
    solar_panel_1 = SolarPanel()
    wind_turbine_1 = WindTurbine()

    # Examples of exhaustibles
    oil_plant = OilGenerator()
    oil_plant.use()
    coal_plant = CoalGenerator()
    coal_plant.use()

    # Call the charge
    charge_battery(
        {
            "solar": solar_panel_1.power,
            "wind": wind_turbine_1.power,
            "oil": oil_plant.energy,
            "coal": coal_plant.energy
        }
    )

if __name__ == "__main__":
    main()