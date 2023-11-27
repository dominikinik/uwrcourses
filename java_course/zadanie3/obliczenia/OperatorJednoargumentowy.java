package obliczenia;

public abstract class OperatorJednoargumentowy extends Wyrazenie {
    protected Wyrazenie operand;

    public OperatorJednoargumentowy(Wyrazenie operand) {
        this.operand = operand;
    }
}
