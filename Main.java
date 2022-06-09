class Dog {
  public void run() {

    System.out.println("Dog Runs");
  }

}

class Rabit extends Dog {
  public void eat() {
    System.out.println("Rabit eats");

  }
}

class Main {

  public static void main(String[] args) {

    Rabit R = new Rabit();
    R.run();
    R.eat();

  }
}