package obliczenia;

public class Dzielenie extends OperatorDwuargumentowy {
    public Dzielenie(Wyrazenie lewyOperand, Wyrazenie prawyOperand) {
        super(lewyOperand, prawyOperand);
    }

    @Override
    public double oblicz() {
        double prawyWynik = prawyOperand.oblicz();
        if (prawyWynik != 0) {
            return lewyOperand.oblicz() / prawyWynik;
        } else {
            throw new ArithmeticException("Dzielenie przez zero!");
        }
    }

    @Override
    public String toString() {
        return "(" + lewyOperand + " / " + prawyOperand + ")";
    }
}