package figury;

public final class Wektor {
    public final double dx, dy;

    public Wektor(double dx_val, double dy_val) {
        dx = dx_val;
        dy = dy_val;
    }
    public static Wektor skladaj(Wektor v1,Wektor v2){
        return new Wektor(v1.dx + v2.dx, v1.dy+v2.dy);
    }
}
