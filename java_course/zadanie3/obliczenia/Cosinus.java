package obliczenia;

public class Cosinus extends OperatorJednoargumentowy {
    public Cosinus(Wyrazenie operand) {
        super(operand);
    }

    @Override
    public double oblicz() {
        return Math.cos(operand.oblicz());
    }

    @Override
    public String toString() {
        return "cos(" + operand + ")";
    }
}
