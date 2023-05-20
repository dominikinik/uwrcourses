class Function2D
    def initialize(f)
      @f = f
    end
    
    def value(x, y)
      @f.call(x, y)
    end
    
    def volume(a, b, c, d, step=0.1)
      vol = 0
      (a/step...b/step).step(step).each do |x|
        (c/step...d/step).step(step).each do |y|
          vol += step * step * @f.call(x*step, y*step)
        end
      end
      vol
    end
    
    def contour_line(a, b, c, d, height, step=0.1)
      points = []
      (a/step...b/step).step(step).each do |x|
        (c/step...d/step).step(step).each do |y|
          if (@f.call(x*step, y*step) - height).abs < step
            points << [x*step, y*step]
          end
        end
      end
      points
    end
  end
f = ->(x, y) { x**2 + y**2 }

func = Function2D.new(f)

val = func.value(1, 2)
puts val 

vol = func.volume(0, 1, 0, 2)
puts vol 


