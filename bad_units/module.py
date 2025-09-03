class UnitConversionError(Exception):
    pass

class Unit:
    unit_type = None
    base_units_per = None

    def __init__(self, amount=1):
        self.amount = amount

    def to(self, other):
        if not isinstance(other, Unit):
            raise TypeError("Can only convert to another Unit")

        if self.unit_type != other.unit_type:
            raise UnitConversionError("Units must be of the same type")
        
        return other.__class__((self.amount * self.base_units_per) / other.base_units_per)
    
    def __repr__(self):
        return f"{self.amount} {self.__class__.__name__}"