package obliczenia;

public class Logarytm extends OperatorJednoargumentowy {
    public Logarytm(Wyrazenie operand) {
        super(operand);
    }

    @Override
    public double oblicz() {
        return Math.log(operand.oblicz());
    }

    @Override
    public String toString() {
        return  "log(" + operand + ")";
    }
}
