
import obliczenia.*;


public class Main {
    public static void main(String[] args) {


        Zmienna.ustawZmienna("x", 1.618);


        testujWyrazenie("7 + 5 * 3 - 1", new Dodawanie(new Liczba(7), new Odejmowanie(new Mnozenie(new Liczba(5), new Liczba(3)), new Liczba(1))));
        testujWyrazenie("~ (2 - x) * e", new Mnozenie(new ZmianaZnaku(new Odejmowanie(new Liczba(2), new Zmienna("x"))), new Stala("e")));
        testujWyrazenie("(3 * π - 1) / (x + 5)", new Dzielenie(new Odejmowanie(new Mnozenie(new Liczba(3), new Stala("π")), new Liczba(1)), new Dodawanie(new Zmienna("x"), new Liczba(5))));
        testujWyrazenie("sin((x + 13) * π / (1 - x))", new Sinus(new Dzielenie(new Mnozenie(new Dodawanie(new Zmienna("x"), new Liczba(13)), new Stala("π")), new Odejmowanie(new Liczba(1), new Zmienna("x")))));
        testujWyrazenie("exp(5) + x * log(e, x)", new Dodawanie(new Potegowanie(new Stala("e")), new Mnozenie(new Zmienna("x"), new Logarytm(new Stala("e")))));
    }

    private static void testujWyrazenie(String opis, Wyrazenie wyrazenie) {
        System.out.println("Wyrażenie: " + opis);
        System.out.println("Drzewo obliczeń: " + wyrazenie);

        double wynik = wyrazenie.oblicz();
        System.out.println("Wynik obliczeń: " + wynik);

        System.out.println();
    }
}

