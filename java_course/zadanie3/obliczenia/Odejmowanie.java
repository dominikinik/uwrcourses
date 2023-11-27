package obliczenia;

public class Odejmowanie extends OperatorDwuargumentowy {
    public Odejmowanie(Wyrazenie lewyOperand, Wyrazenie prawyOperand) {
        super(lewyOperand, prawyOperand);
    }

    @Override
    public double oblicz() {
        return lewyOperand.oblicz() - prawyOperand.oblicz();
    }

    @Override
    public String toString() {
        return "(" + lewyOperand + " - " + prawyOperand + ")";
    }
}
