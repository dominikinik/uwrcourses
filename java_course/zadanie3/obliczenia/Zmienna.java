package obliczenia;
import struktury.Para;
import struktury.ZbiorTablicowy;
import java.util.Objects;
public class Zmienna extends Wyrazenie {
    private final String identyfikator;

    private static final ZbiorTablicowy zbiorZmiennych = new ZbiorTablicowy(100);

    public Zmienna(String identyfikator) {
        this.identyfikator = identyfikator;
    }

    @Override
    public double oblicz() {
        Para para = zbiorZmiennych.szukaj(identyfikator);
        if (para != null) {
            return para.getWartosc();
        }
        throw new IllegalArgumentException("Brak wartości dla zmiennej: " + identyfikator);
    }


    public static void ustawZmienna(String identyfikator, double wartosc) {
        zbiorZmiennych.wstaw(new Para(identyfikator, wartosc));
    }

    @Override
    public String toString() {
        return identyfikator;
    }

    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Zmienna zmienna = (Zmienna) obj;
        return Objects.equals(this.identyfikator, zmienna.identyfikator);
    }
}
