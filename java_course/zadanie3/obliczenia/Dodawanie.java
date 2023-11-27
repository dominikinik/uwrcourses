package obliczenia;

public class Dodawanie extends OperatorDwuargumentowy {
    public Dodawanie(Wyrazenie lewyOperand, Wyrazenie prawyOperand) {
        super(lewyOperand, prawyOperand);
    }

    @Override
    public double oblicz() {
        return lewyOperand.oblicz() + prawyOperand.oblicz();
    }

    @Override
    public String toString() {
        return "(" + lewyOperand + " + " + prawyOperand + ")";
    }
}
