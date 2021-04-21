class Road:

    def __init__(self,length,width):
        self._length = length
        self._width = width
    def asphalt_mass(self, surface_thickness):
        self.surface_thickness = surface_thickness
        asphalt_mass_m2_cm = 0.03
        self.asphalt_mass = self._length * self._width * asphalt_mass_m2_cm * self.surface_thickness
        print(f' Масса дорожного покрытия {self.asphalt_mass} тонн')
print("Рассчет массу дорожного покрытия, ширину 25 м и длина 200 м")
road1 = Road(25, 200)
road1.asphalt_mass(10)