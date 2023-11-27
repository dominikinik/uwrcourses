package figury;



public final class Trojkat {
    private Punkt punktA, punktB, punktC;

    public Trojkat(Punkt punktA_val, Punkt punktB_val, Punkt punktC_val) {

        if (czyWspolliniowe(punktA_val, punktB_val, punktC_val)) {
            throw new IllegalArgumentException("to nie trokat ten");
        }

        punktA = punktA_val;
        punktB = punktB_val;
        punktC = punktC_val;
    }

    private boolean czyWspolliniowe(Punkt a, Punkt b, Punkt c) {
        return (b.getY() - a.getY()) * (c.getX() - b.getX()) == (c.getY() - b.getY()) * (b.getX() - a.getX());
    }

    public Punkt getPunktA() {
        return punktA;
    }

    public Punkt getPunktB() {
        return punktB;
    }

    public Punkt getPunktC() {
        return punktC;
    }
    public void przesun(Wektor v) {
        punktA.przesun(v);
        punktB.przesun(v);
        punktC.przesun(v);
    }
    public void obroc(Punkt p, double kat) {
        punktA.obroc(p,kat);
        punktB.obroc(p,kat);
        punktC.obroc(p,kat);
    }
    public void odbij(Prosta p){
        punktA.odbij(p);
        punktB.odbij(p);
        punktC.odbij(p);
    }
}

