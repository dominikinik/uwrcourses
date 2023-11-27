package obliczenia;

public class Sinus extends OperatorJednoargumentowy {
    public Sinus(Wyrazenie operand) {
        super(operand);
    }

    @Override
    public double oblicz() {
        return Math.sin(operand.oblicz());
    }

    @Override
    public String toString() {
        return "sin(" + operand + ")";
    }
}
