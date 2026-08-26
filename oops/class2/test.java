class Account
    Account(){
        System.out.println("Test Class - constructor method - special jilebi");
    }
    public void deposit(){
        System.out.println("deposit - normal method");
    }
    public static void main(String[] args) {
      Account T1=new Account();
      Account T2=new Account();
      Account T3 =new Account();
    }
}