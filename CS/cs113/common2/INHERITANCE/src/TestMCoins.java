
//Maria Angel Palacios Sarmiento
// UCID: 3158891

public class TestMCoins {
    public static void main(String[] args) {
        // Creates the Array
        MonetaryCoin[][] coin = new MonetaryCoin[3][5];
        for (int i = 0; i < coin.length; i++) {
            for (int j = 0; j < coin[i].length; j++) {
                coin[i][j] = new MonetaryCoin();
                coin[i][j].flip();
            }
        }
        totalHeads(coin);
    }
    private static void totalHeads(MonetaryCoin[][] coin) {
        for (MonetaryCoin[] monetaryCoins : coin) {
            int totalHeads = 0;
            for (MonetaryCoin monetaryCoin : monetaryCoins) {
                System.out.print("(" + monetaryCoin.getValue() + ", " + (monetaryCoin.isHeads() ? "HEADS" : "TAILS") + ") ");
                if (monetaryCoin.isHeads()) {
                    totalHeads += monetaryCoin.getValue();
                }
            }
            System.out.println("Total number of Heads: " + totalHeads);
        }
    }
}

