# klasa reprezentująca długość
class Length
    def initialize(kilometers)
      @km = kilometers
    end
  
    def nautical_miles
      @km / 1.852
    end
  
    def kilometers=(kilometers)
      @km = kilometers
    end
  end
  
  # klasa reprezentująca czas
  class Time
    def initialize(hours)
      @h = hours
    end
  
    def seconds
      @h * 3600
    end
  
    def hours=(hours)
      @h = hours
    end
  end
  
  class Speed
    def initialize(kph)
      @kph = kph
    end
  
    def knots
      @kph / 1.852
    end
  
    def kph=(kph)
      @kph = kph
    end
  end
  
  class Acceleration
    def initialize(kms2)
      @kms2 = kms2
    end
  
    def mmh2
      @kms2 * 12960
    end
  
    def kms2=(kms2)
      @kms2 = kms2
    end
  end
  
  speed = Speed.new(100)
  acceleration = Acceleration.new(10)
  
  puts "Prędkość:"
  puts "W jednostkach SI\t|\tW jednostkach spoza układu SI"
  puts "---------------------------------------------------"
  puts "#{speed.instance_variable_get(:@kph)} km/h\t|\t#{speed.knots.round(2)} knots"
  
  puts "\nPrzyspieszenie:"
  puts "W jednostkach SI\t|\tW jednostkach spoza układu SI"
  puts "---------------------------------------------------"
  puts "#{acceleration.instance_variable_get(:@kms2)} km/s²\t|\t#{acceleration.mmh2.round(2)} mm/h²"
  