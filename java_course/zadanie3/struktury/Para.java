package struktury;

public class Para implements Cloneable,Comparable<Para>  {
    public final String klucz;
    private double wartosc;
    public Para(String klucz, double wartosc) {
        if (klucz == null || klucz.isEmpty() || !klucz.matches("^[a-z]+$")) {
            throw new IllegalArgumentException(" co ty wpisujesz pacanie ");
        }

        this.klucz = klucz;
        this.wartosc = wartosc;
    }
    public double getWartosc(){
        return wartosc;
    }
    public void setWartosc(double wartosc) {
        this.wartosc = wartosc;
    }
    @Override
    public String toString() {
        return "Para{" +
                "klucz='" + klucz + '\'' +
                ", wartosc=" + wartosc +
                '}';
    }
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Para para = (Para) obj;
        return klucz.equals(para.klucz);
    }
    @Override
    public Para clone() {
        try {
            return (Para) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new InternalError(e);
        }
    }
    @Override
    public int compareTo(Para p) {
        return this.klucz.compareTo(p.klucz);
    }

}



