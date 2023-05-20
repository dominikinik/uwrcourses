class Function
    def initialize(&block)
      @func = block
    end
  
    def value(x)
      @func.call(x)
    end
  
    def zero(a, b, e)
      return nil if value(a) * value(b) > 0
  
      mid = (a + b) / 2.0
      while (b - a).abs > e
        if value(mid) * value(a) < 0
          b = mid
        else
          a = mid
        end
        mid = (a + b) / 2.0
      end
      mid
    end
  
    def field(a, b)
      n = 1000
      h = (b - a) / n.to_f
      sum = 0.0
      x = a
      while x < b
        sum += value(x)
        x += h
      end
      sum * h
    end
  
    def deriv(x)
      h = 0.0001
      (value(x + h) - value(x)) / h
    end
  end

  f = Function.new { |x| x * x * Math.sin(x) }
puts f.value(0)     
puts f.zero(-2, 2, 0.0001) 
puts f.field(0, Math::PI)  
puts f.deriv(1)      