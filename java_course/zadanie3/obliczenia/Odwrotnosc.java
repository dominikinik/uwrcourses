package obliczenia;

public class Odwrotnosc extends OperatorJednoargumentowy {
    public Odwrotnosc(Wyrazenie operand) {
        super(operand);
    }

    @Override
    public double oblicz() {
        double wynik = operand.oblicz();
        if (wynik != 0) {
            return 1 / wynik;
        } else {
            throw new ArithmeticException("Zero");
        }
    }

    @Override
    public String toString() {
        return "(1 / " + operand + ")";
    }
}
