# converter
class converter:
    def __init__(self, n, unit):
        self.n = n
        self.unit = unit
       #print(self.unit)
    def feet(self):
        feet = {"meter": self.n * 0.3048, "centimeter": self.n * 30.48, "millimeter": self.n * 304.8, "kilometer": self.n * 0.0003048, "mile": self.n * 0.000189394, "inch": self.n * 12, "yard": self.n * 0.333333}  # type: ignore
        print("your asked conversion is:", feet[(self.unit)])

    def centimeter(self):
        centimeter = {"meter": self.n * 0.01, "millimeter": self.n * 10, "kilometer": self.n * 1e-5, "mile": self.n * 6.2137e-6, "feet": self.n * 0.0328084, "inch": self.n * 0.393701, "yard": self.n * 0.0109361}  # type: ignore
        print("your required conversion is", centimeter[self.unit])

    def kilometer(self):
        kilometer = {"meter": self.n * 1000, "centimeter": self.n * 100000, "millimeter": self.n * 1000000, "mile": self.n * 0.621371, "feet": self.n * 3280.84, "inch": self.n * 39370.1, "yard": self.n * 1093.61}  # type: ignore
        print("your required conversion is", kilometer[self.unit])

    def mile(self):
        mile = {"meter": self.n * 1609.34, "centimeter": self.n * 160934, "millimeter": self.n * 1609340, "kilometer": self.n * 1.60934, "feet": self.n * 5280, "inch": self.n * 63360, "yard": self.n * 1760}  # type: ignore
        print("your required conversion is", mile[self.unit])

    def millimeter(self):
        millimeter = {"meter": self.n * 0.001, "centimeter": self.n * 0.1, "kilometer": self.n * 1e-6, "mile": self.n * 6.2137e-7, "feet": self.n * 0.00328084, "inch": self.n * 0.0393701, "yard": self.n * 0.00109361}
        print("your required conversion is", millimeter[self.unit])

    def meter(self):
        meter = {"centimeter": self.n * 100, "millimeter": self.n * 1000, "kilometer": self.n * 0.001, "mile": self.n * 0.000621371, "feet": self.n * 3.28084, "inch": self.n * 39.3701, "yard": self.n * 1.09361}  # type: ignore
        print("your required conversion is", meter[self.unit])

    def inch(self):
        self.n = 
        inch = {"meter": self.n * 0.0254, "centimeter": self.n * 2.54, "millimeter": self.n * 25.4, "kilometer": self.n * 2.54e-5, "mile": self.n * 1.5783e-5, "feet": self.n * 0.0833333, "yard": self.n * 0.0277778}  # type: ignore
        print("your required conversion is", inch[self.unit])

    def yard(self):
        yard = {"meter": self.n * 0.9144, "centimeter": self.n * 91.44, "millimeter": self.n * 914.4, "kilometer": self.n * 0.0009144, "mile": self.n * 0.000568182, "feet": self.n * 3, "inch": self.n * 36}  # type: ignore
        print("your required conversion is", yard[self.unit])+
c = converter(9, "centimeter")
c.feet() 
c.inch()  
c.yard()

        
        
        