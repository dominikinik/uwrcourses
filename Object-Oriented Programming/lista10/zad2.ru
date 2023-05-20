class Kolekcja
    class Element
      attr_accessor :value, :prev, :next
  
      def initialize(value, prev = nil, next_elem = nil)
        @value = value
        @prev = prev
        @next = next_elem
      end
    end
  
    attr_accessor :head, :tail
  
    def initialize
      @head = nil
      @tail = nil
    end
  
    def dodaj(element)
      node = Element.new(element)
      if @head.nil?
        @head = node
        @tail = node
      elsif element < @head.value
        node.next = @head
        @head.prev = node
        @head = node
      elsif element > @tail.value
        node.prev = @tail
        @tail.next = node
        @tail = node
      else
        current = @head
        while current.next && current.next.value < element
          current = current.next
        end
        node.next = current.next
        node.prev = current
        current.next.prev = node
        current.next = node
      end
    end
  
    def to_a
      arr = []
      current = @head
      while current
        arr << current.value
        current = current.next
      end
      arr
    end
  end
  
  class Wyszukiwanie
    def self.wyszukaj_binarnie(kolekcja, element)
      left = 0
      right = kolekcja.to_a.length - 1
  
      while left <= right
        mid = (left + right) / 2
        if kolekcja.to_a[mid] == element
          return mid
        elsif kolekcja.to_a[mid] < element
          left = mid + 1
        else
          right = mid - 1
        end
      end
      return nil
    end
  
    def self.wyszukaj_interpolacyjnie(kolekcja, element)
      left = 0
      right = kolekcja.to_a.length - 1
  
      while left <= right && element >= kolekcja.to_a[left] && element <= kolekcja.to_a[right]
        pos = left + ((element - kolekcja.to_a[left]) * (right - left)) / (kolekcja.to_a[right] - kolekcja.to_a[left])
        if kolekcja.to_a[pos] == element
          return pos
        elsif kolekcja.to_a[pos] < element
          left = pos + 1
        else
          right = pos - 1
        end
      end
      return nil
    end
  end
  
  
  # Test
  kolekcja = Kolekcja.new
  kolekcja.dodaj(3)
  kolekcja.dodaj(1)
  kolekcja.dodaj(4)
  kolekcja.dodaj(1)
  kolekcja.dodaj(5)
  kolekcja.dodaj(9)
  kolekcja.dodaj(2)
  kolekcja.dodaj(6)
  kolekcja.dodaj(5)
  kolekcja.dodaj(3)
  kolekcja.dodaj(5)
  
  puts Wyszukiwanie.wyszukaj_binarnie(kolekcja, 1000)
  puts Wyszukiwanie.wyszukaj_interpolacyjnie(kolekcja, 1000) 
  puts Wyszukiwanie.wyszukaj_binarnie(kolekcja, 2)
  puts Wyszukiwanie.wyszukaj_interpolacyjnie(kolekcja, 2) 
  