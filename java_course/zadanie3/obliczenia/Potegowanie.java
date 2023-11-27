package obliczenia;

public class Potegowanie extends OperatorJednoargumentowy {
    public Potegowanie(Wyrazenie operand) {
        super(operand);
    }

    @Override
    public double oblicz() {
        return Math.pow(operand.oblicz(),2);
    }

    @Override
    public String toString() {
        return  operand + "^2";
    }
}
