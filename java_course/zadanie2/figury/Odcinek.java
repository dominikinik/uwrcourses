package figury;

public final  class Odcinek {
    private Punkt punktA;
    private Punkt punktB;

    public Odcinek(Punkt punktA_val, Punkt punktB_val) {
        punktA = punktA_val;
        punktB = punktB_val;
    }

    public Punkt getPunktA() {
        return punktA;
    }

    public Punkt getPunktB() {
        return punktB;
    }
    public void przesun(Wektor v) {
        punktA.przesun(v);
        punktB.przesun(v);

    }
    public void obroc(Punkt p, double kat) {
        punktA.obroc(p,kat);
        punktB.obroc(p,kat);
    }
    public void odbij(Prosta p){
        punktA.odbij(p);
        punktB.odbij(p);
    }
}
