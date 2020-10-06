class Ecrit extends Thread{
  public Ecrit(String texts,int nb){
    this.texte = texts;
    this.nb = nb;
  }

  public void run(){
    for(int i=0; i<nb; i++){
      System.out.print(texte);
    }
  }
  
  private String texte;
  private int nb;
}
