package obliczenia;

public class Stala extends Wyrazenie {
    private final double wartosc;
    private final String oznaczenie;

    public Stala( String oznaczenie) {
        if(oznaczenie.equals("π")){
            this.wartosc = 3.13;

        }
        else{
            this.wartosc = 2.72;

        }
        this.oznaczenie = oznaczenie;
    }

    @Override
    public double oblicz() {
        return wartosc;
    }

    @Override
    public String toString() {
        return oznaczenie;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Stala stala = (Stala) obj;
        return Double.compare(stala.wartosc, wartosc) == 0;
    }
}
