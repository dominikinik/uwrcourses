package obliczenia;

public abstract class OperatorDwuargumentowy extends Wyrazenie {
    protected Wyrazenie lewyOperand;
    protected Wyrazenie prawyOperand;

    public OperatorDwuargumentowy(Wyrazenie lewyOperand, Wyrazenie prawyOperand) {
        this.lewyOperand = lewyOperand;
        this.prawyOperand = prawyOperand;
    }
}