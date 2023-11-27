// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
import figury.*;
public class Main {
    public static void main(String[] args) {
        testPunkt();
        testWektor();
        testProsta();
        testOdcinek();
        testTrojkat();
    }

    private static void testPunkt() {
        Punkt p1 = new Punkt(1, 2);
        System.out.println("Punkt p1: " + p1.getX() + ", " + p1.getY());

        Wektor v = new Wektor(2, 3);
        p1.przesun(v);
        System.out.println("Punkt p1 po przesunięciu: " + p1.getX() + ", " + p1.getY());

        Punkt p2 = new Punkt(4, 5);
        p2.obroc(p1, 90);
        System.out.println("Punkt p2 po obrócie względem p1 o 90 stopni: " + p2.getX() + ", " + p2.getY());

        Prosta os = new Prosta(1, -1, 0);
        p2.odbij(os);
        System.out.println("Punkt p2 po odbiciu względem prostej x-y: " + p2.getX() + ", " + p2.getY());
    }

    private static void testWektor() {
        Wektor v1 = new Wektor(2, 3);
        Wektor v2 = new Wektor(-1, 2);

        Wektor suma = Wektor.skladaj(v1, v2);
        System.out.println("Wektor suma: dx = " + suma.dx + ", dy = " + suma.dy);
    }

    private static void testProsta() {
        Prosta p1 = new Prosta(1, -1, 0);
        Prosta p2 = new Prosta(-2, 2, 1);

        System.out.println("Czy proste p1 i p2 są równoległe? " + Prosta.czyRownolegle(p1, p2));
        System.out.println("Czy proste p1 i p2 są prostopadłe? " + Prosta.czyProstopadle(p1, p2));


    }

    private static void testOdcinek() {
        Punkt punkt1 = new Punkt(1, 2);
        Punkt punkt2 = new Punkt(4, 5);

        Odcinek odcinek = new Odcinek(punkt1, punkt2);

        Wektor v = new Wektor(2, 3);
        odcinek.przesun(v);
        System.out.println("Odcinek po przesunięciu: punkt1 = (" + odcinek.getPunktA().getX() + ", " +
                odcinek.getPunktA().getY() + "), punkt2 = (" + odcinek.getPunktB().getX() + ", " +
                odcinek.getPunktB().getY() + ")");
    }

    private static void testTrojkat() {
        Punkt punktA = new Punkt(1, 4);
        Punkt punktB = new Punkt(4, 5);
        Punkt punktC = new Punkt(7, 8);

        Trojkat trojkat = new Trojkat(punktA, punktB, punktC);

        Wektor v = new Wektor(2, 3);
        trojkat.przesun(v);
        System.out.println("Trójkąt po przesunięciu: punktA = (" + trojkat.getPunktA().getX() + ", " +
                trojkat.getPunktA().getY() + "), punktB = (" + trojkat.getPunktB().getX() + ", " +
                trojkat.getPunktB().getY() + "), punktC = (" + trojkat.getPunktC().getX() + ", " +
                trojkat.getPunktC().getY() + ")");
    }
}