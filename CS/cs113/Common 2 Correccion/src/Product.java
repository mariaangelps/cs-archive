class Product {
    private int price;
    private String description;

    public Product(int price, String description) {
        this.price = price;
        this.description = description;
    }

    public  String getDescription() {
        return description;
    }

    public int compareTo(Product other) {
        if (price < other.price) {
            return -1;
        } else if (price == other.price) {
            return 0;
        } else return 1;
    }

    public static String shoppingCart(Product[] array){
        Product exp = array[0];
    for(int i=0; i<array.length;i++){
        if(array[i].compareTo(exp)>0){
            array[i]=exp;
            array[i].getDescription();
        }

    }
    return exp.getDescription();
    }

    public static void main(String[] args) {
        Product[] arr = {new Product(65, "Sweater"), new Product(34,"Botas"),
                         new Product(32,"Sombrillas")
        };
       System.out.println(shoppingCart(arr));
        }
    }



