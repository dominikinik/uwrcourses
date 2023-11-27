package figury;

public final class Punkt {
    private double x,y;
    public Punkt(double x_val, double y_val) {
        x = x_val;
        y = y_val;
    }

    public double getX() {
        return x;
    }
    public double getY() {
        return y;
    }
    public void przesun(Wektor v) {
        this.x += v.dx;
        this.y += v.dy;
    }
    public void obroc(Punkt p, double kat) {
        double radians = Math.toRadians(kat);
        double cos = Math.cos(radians);
        double sin = Math.sin(radians);

        double newX = cos * (this.x - p.x) - sin * (this.y - p.y) + p.x;
        double newY = sin * (this.x - p.x) + cos * (this.y - p.y) + p.y;

        this.x = newX;
        this.y = newY;
    }
    public void odbij(Prosta p) {
        double d = 2 * (p.a * this.x + p.b * this.y + p.c) / (p.a * p.a + p.b * p.b);
        this.x -= d * p.a;
        this.y -= d * p.b;
    }
}
