package struktury;

public class ZbiorTablicowy implements Zbior, Cloneable {
    private Para[] zbiór;
    private int zapełnienie;
    public ZbiorTablicowy(int roz){
        if(roz<=0){
            throw new IllegalArgumentException("ta tablica to taka nie za duza");
        }
        this.zbiór = new Para[roz];
        this.zapełnienie = 0;
    }
    @Override
    public Para szukaj(String k){
        for (Para para : zbiór){
            if(para != null && para.klucz.equals(k)){
                return para;
            }
        }
        return null;
    }
    @Override
    public void wstaw(Para p){
        if(zapełnienie == zbiór.length){
            throw new IllegalArgumentException("tych argumentow to troche duzo daj juz spokoj");
        }
        for (int i=0;i<zapełnienie;i++){
            if(zbiór[i].klucz.equals(p.klucz)){
                zbiór[i].setWartosc(p.getWartosc());
                return;
            }
        }
        zbiór[zapełnienie++]=p;

    }
    @Override
    public void usuń(String k){
        for(int i=0;i<zapełnienie;i++){
            if(zbiór[i] != null && zbiór[i].klucz.equals(k)){
                zbiór[i]=null;
            }

            for(int j=i+1;j<zapełnienie;j++){
                zbiór[j-1]=zbiór[j];
            }
            zbiór[zapełnienie] = null;
            zapełnienie--;
            return;
        }
    }
    @Override
    public void czyść(){
        for(int i=0;i<zapełnienie;i++) {
            zbiór[i]=null;
        }
        zapełnienie=0;
    }
    @Override
    public ZbiorTablicowy clone(){
        try {
            ZbiorTablicowy klon = (ZbiorTablicowy) super.clone();
            klon.zbiór = zbiór.clone();
            return klon;
        } catch (CloneNotSupportedException e) {
            throw new InternalError(e);
        }
    }
    @Override
    public int ile() {
        return zapełnienie;
    }

}

