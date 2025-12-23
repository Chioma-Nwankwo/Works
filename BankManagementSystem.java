import java.util.Scanner;

//base class for accounts
class Account {        
    private final int accountNumber; //private variable that cannot be changed after initialization
    private double balance; //private variable to store balance

    //constructor to initialize account number and balance
    public Account(int accountNumber, double initialBalance) {   
        this.accountNumber = accountNumber; //used to access the instance variales from the Account class
        this.balance = initialBalance;
    }

    //getter method to retrieve the value of the private variable(Encapsulation)
    public int getAccountNumber() {  
        return accountNumber;
    }

    public double getBalance() {
        return balance;
    }

    //method for adding a positive value inputted from the keyboard
    public void deposit(double amount) {  
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: " + amount + "$");
        } else {
            System.out.println("Invalid deposit amount.");
        }
    }

    //method to withdraw a positive value entered from the keyboard
    public void withdraw(double amount) {  
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount +"$");
        } else {
            System.out.println("Insufficient funds or invalid amount.");
        }
    }

    public double calculateInterest() {
        return 0; 
    }
}

//class inheriting attributes from Account class(Inheritance)
class SavingsAccount extends Account {  
    private static final double INTEREST_RATE = 0.03;

    public SavingsAccount(int accountNumber, double initialBalance) {
        super(accountNumber, initialBalance);
    }

    @Override  //method that overrides the calculateInterest method in the superclass(Account)
    public double calculateInterest() {
        return getBalance() * INTEREST_RATE;   //Calculates and returns interest based on the balance and the interest rate(Polymorphism)
    }
}

class CheckingAccount extends Account {
    private static final double INTEREST_RATE = 0.01;

    public CheckingAccount(int accountNumber, double initialBalance) {
        super(accountNumber, initialBalance);
    }

    @Override    
    public double calculateInterest() {
        return getBalance() * INTEREST_RATE;
    }
}

class CurrentAccount extends Account {
    public CurrentAccount(int accountNumber, double initialBalance) {
        super(accountNumber, initialBalance);  //used to call the constructor of the parent class(Account)
    }

    @Override   
    public double calculateInterest() {
        return 0;
    }
}

//class for bank managing accounts
class Bank {   
    private static final int MAX_ACCOUNTS = 100;  //private constant that limits number of accounts to 100
    private Account[] accounts = new Account[MAX_ACCOUNTS]; //array to store accounts
    private int accountCount = 0;
    private Scanner scanner = new Scanner(System.in); //prompts user input

    public void createAccount() {   //prompts user for account details and creates an account based on type specified
        if (accountCount >= MAX_ACCOUNTS) {
            System.out.println("Cannot create more accounts. Maximum limit reached.");
            return;
        }

        System.out.print("Enter Account Number: ");
        int accountNumber = scanner.nextInt();

        System.out.print("Enter Initial Balance: ");
        double initialBalance = scanner.nextDouble();

        System.out.print("Enter Account Type (1 for Savings, 2 for Checking, 3 for Current): ");
        int type = scanner.nextInt();

        Account account;
        switch (type) {  //switch case to choose account type
            case 1:
                  account = new SavingsAccount(accountNumber, initialBalance);
                  break;
            case 2:
                  account = new CheckingAccount(accountNumber, initialBalance);
                  break;
            case 3:
                  account = new CurrentAccount(accountNumber, initialBalance);
                  break;
            default:
                System.out.println("Invalid account type.");
                return;
            
        }

        accounts[accountCount++] = account; //adds account created to the numberof accounts in the bank
        System.out.println("Account created successfully.");
    }

    //finds an account by number and allows the user to deposit money
    public void depositMoney() {  
        Account account = findAccount();
        if (account != null) {
            System.out.print("Enter Deposit Amount: ");
            double amount = scanner.nextDouble();
            account.deposit(amount);
        }
    }

    //finds an account by number and allows the user to withdraw money
    public void withdrawMoney() {   
        Account account = findAccount();
        if (account != null) {
            System.out.print("Enter Withdrawal Amount: ");
            double amount = scanner.nextDouble();
            account.withdraw(amount);
        }
    }

    //finds an account by number and allows the user to check the balance of their account
    public void checkBalance() {    
        Account account = findAccount();
        if (account != null) {
            System.out.println("Balance: " + account.getBalance() +"$");
        }
    }

    //method to search for an account by number and returns null if not found
    private Account findAccount() {    
        System.out.print("Enter Account Number: ");
        int accountNumber = scanner.nextInt();

        for (int i = 0; i < accountCount; i++) {
            if (accounts[i].getAccountNumber() == accountNumber) {
                return accounts[i];
            }
        }

        System.out.println("Account not found.");
        return null;
    }
}

public class BankManagementSystem {  
    public static void main(String[] args) {  //main method
        Bank bank = new Bank();   //creation of object 'Bank'
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("------------------");
            System.out.println("|Menu:           |");
            System.out.println("------------------");

            System.out.println("1. Create Account|");
            System.out.println("2. Deposit Money |");
            System.out.println("3. Withdraw Money|");
            System.out.println("4. Check Balance |");
            System.out.println("5. Exit          |");
            System.out.println("------------------");
            System.out.print("Choose an option: |");
            System.out.println("\n------------------");
            

            int choice = scanner.nextInt();

            switch (choice) {
                case 1 : 
                     bank.createAccount();  //Call the createAccount menthod
                     break;
                case 2: 
                     bank.depositMoney();   //Call the depositMoney method
                     break;
                case 3: 
                     bank.withdrawMoney();  //Call the withdrawMoney method
                     break;
                case 4 : 
                     bank.checkBalance();  //Call the checkBalance method
                     break;
                case 5: 
                    System.out.println("Thank you for using the Bank Management System.");
                    scanner.close();  //close the scanner
                    return;
                
                default: 
                    System.out.println("Invalid option. Please try again.");
            }
        }
    }
}
