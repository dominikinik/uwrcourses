package obliczenia;

public class ZmianaZnaku extends OperatorJednoargumentowy {
    public ZmianaZnaku(Wyrazenie operand) {

        super(operand);
    }

    @Override
    public double oblicz() {
        return -operand.oblicz();
    }

    @Override
    public String toString() {
        return "(-" + operand + ")";
    }
}
