class Lenght 
    def initialize(len)
        @metr = len
    end
    def jard
        0.9144*@metr
    end
    def jard=(len)
        @metr = (1/0.9144)*len
    end
end
class Weight 
    def initialize(mas)
        @kg = mas
    end
    def funt
        2.20462*@kg
    end
    def funt=(mas)
        @kg = (1/2.20462)*mas
    end
end
class Surface
    def initialize(hectares, square_inches)
      @hectares = hectares
      @square_inches = square_inches
    end
    
    def acres
      @hectares * 2.47105
    end
    
    def acres=(value)
      @hectares = value / 2.47105
    end
    
    def square_feet
      @square_inches / 144
    end
    
    def square_feet=(value)
      @square_inches = value * 144
    end
  end
  
class Pressure
    def initialize(bars, pounds_per_square_inch)
      @bars = bars
      @pounds_per_square_inch = pounds_per_square_inch
    end
    
    def pounds_per_square_foot
      @pounds_per_square_inch * 144
    end
    
    def pounds_per_square_foot=(value)
      @pounds_per_square_inch = value / 144
    end
    
    def kilopascals
      @bars * 100
    end
    
    def kilopascals=(value)
      @bars = value / 100
    end
end
  
hectares = 10
square_inches = 1000000
bars = 2
pounds_per_square_inch = 50

surface = Surface.new(hectares, square_inches)
pressure = Pressure.new(bars, pounds_per_square_inch)

puts "Powierzchnia:"
puts "W jednostkach SI\t|\tW jednostkach anglosaskich"
puts "---------------------------------------------------"
puts "#{surface.instance_variable_get(:@hectares)} ha\t|\t#{surface.acres.round(2)} ac"
puts "#{surface.instance_variable_get(:@square_inches)} in²\t|\t#{surface.square_feet.round(2)} ft²"

puts "\nCiśnienie:"
puts "W jednostkach SI\t|\tW jednostkach anglosaskich"
puts "---------------------------------------------------"
puts "#{pressure.instance_variable_get(:@bars)} bar\t|\t#{pressure.kilopascals.round(2)} kPa"
puts "#{pressure.instance_variable_get(:@pounds_per_square_inch)} psi\t|\t#{pressure.pounds_per_square_foot.round(2)} lb/ft²"

