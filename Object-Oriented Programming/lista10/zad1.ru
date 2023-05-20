class Collection
    attr_accessor :elements
  
    def initialize(elements)
      @elements = elements
    end
  
    def length
      @elements.length
    end
  
    def get(i)
      @elements[i]
    end
  
    def swap(i, j)
      @elements[i], @elements[j] = @elements[j], @elements[i]
    end
  end
  
  class Sorter
    def sort1(collection)
      n = collection.length
      for i in 1...n
        j = i
        while j > 0 && collection.get(j-1) > collection.get(j)
          collection.swap(j, j-1)
          j -= 1
        end
      end
      collection.elements
    end
  
    def sort2(collection)
      n = collection.length
      loop do
        swapped = false
        for i in 1...n
          if collection.get(i-1) > collection.get(i)
            collection.swap(i-1, i)
            swapped = true
          end
        end
        break if not swapped
      end
      collection.elements
    end
  end
  
  # Test
  collection = Collection.new([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
  sorter = Sorter.new
  
  puts sorter.sort1(collection) 
  puts sorter.sort2(collection) 
  