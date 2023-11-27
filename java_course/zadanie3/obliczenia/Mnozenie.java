package obliczenia;

public class Mnozenie extends OperatorDwuargumentowy {
    public Mnozenie(Wyrazenie lewyOperand, Wyrazenie prawyOperand) {
        super(lewyOperand, prawyOperand);
    }

    @Override
    public double oblicz() {
        return lewyOperand.oblicz() * prawyOperand.oblicz();
    }

    @Override
    public String toString() {
        return "(" + lewyOperand + " * " + prawyOperand + ")";
    }
}
