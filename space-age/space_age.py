class SpaceAge:

    earthYearInSec = 31557600
    planetYears = {'Mercury': 0.2408467, 'Venus': 0.61519726, 'Earth': 1., 'Mars': 1.8808158, 
                   'Jupiter': 11.862615, 'Saturn': 29.447498, 'Uranus': 84.016846, 'Neptune': 164.79132}

    def __init__(self, seconds):
        self.seconds = float(seconds)

    def on_mercury(self):
        return round(self.seconds/(SpaceAge.earthYearInSec*SpaceAge.planetYears['Mercury']), 2)

    def on_venus(self):
        return round(self.seconds/(SpaceAge.earthYearInSec*SpaceAge.planetYears['Venus']), 2)

    def on_earth(self):
        return round(self.seconds/(SpaceAge.earthYearInSec*SpaceAge.planetYears['Earth']), 2)

    def on_mars(self):
        return round(self.seconds/(SpaceAge.earthYearInSec*SpaceAge.planetYears['Mars']), 2)

    def on_jupiter(self):
        return round(self.seconds/(SpaceAge.earthYearInSec*SpaceAge.planetYears['Jupiter']), 2)

    def on_saturn(self):
        return round(self.seconds/(SpaceAge.earthYearInSec*SpaceAge.planetYears['Saturn']), 2)

    def on_uranus(self):
        return round(self.seconds/(SpaceAge.earthYearInSec*SpaceAge.planetYears['Uranus']), 2)

    def on_neptune(self):
        return round(self.seconds/(SpaceAge.earthYearInSec*SpaceAge.planetYears['Neptune']), 2)
