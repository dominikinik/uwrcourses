package obliczenia;

public abstract class Wyrazenie implements Obliczalny {

    public abstract double oblicz();
    public static double  suma (Wyrazenie... wyrs){
        double sum = 0;
        for(Wyrazenie wyr : wyrs){
            sum += wyr.oblicz();
        }
        return sum;
    }
    public static double  iloczyn (Wyrazenie... wyrs){ //nie wiem czemu w przykladzie jest int dla mnie to dziwne troche wiec dalem double ale nie oceniam :)
        double mul = 1;
        for(Wyrazenie wyr : wyrs){
            mul *= wyr.oblicz();
        }
        return mul;
    }
}
