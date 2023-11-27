package figury;

public final class Prosta {
    public final double a,b,c;
    public Prosta(double a_val,double b_val,double c_val){
        a=a_val;
        b=b_val;
        c=c_val;
    }
    public static Prosta przesunProsta(Prosta p, Wektor v) {
        return new Prosta(p.a, p.b, p.c - p.a * v.dx - p.b * v.dy);
    }

    public static boolean czyRownolegle(Prosta p1, Prosta p2) {
        return p1.a * p2.b - p2.a * p1.b == 0;
    }

    public static boolean czyProstopadle(Prosta p1, Prosta p2) {
        return p1.a * p2.a + p1.b * p2.b == 0;
    }

    public static Punkt punktPrzeciecia(Prosta p1, Prosta p2) {
        double det = p1.a * p2.b - p2.a * p1.b;
        if (det == 0) {
            throw new IllegalArgumentException("nie ma przeciecia ten");
        }
        double x = (p2.c * p1.b - p1.c * p2.b) / det;
        double y = (p1.c * p2.a - p2.c * p1.a) / det;
        return new Punkt(x, y);
    }
}
