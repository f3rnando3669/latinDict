import java.util.HashMap;
import java.util.Scanner;
public class LatinDictApp {

    // Dictionary to store word and definitions
    private static HashMap<String, String> dictionary;

    public static void main(String[] args) {
        dictionary = new HashMap<>();
        
        // Load some initial words into the dictionary (for now, hardcoded)
        //loadDictionary();
        
        // Scanner to read user input
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            System.out.println("Enter a word to search (or type 'exit' to quit):");
            String word = scanner.nextLine().trim().toLowerCase();
            
            if (word.equals("exit")) {
                System.out.println("Exiting...");
                break;
            }
            
            String definition = lookupWord(word);
            if (definition != null) {
                System.out.println("Definition of '" + word + "': " + definition);
            } else {
                System.out.println("Word not found in the dictionary.");
            }
        }
        
        scanner.close();
    }
    

private static String lookupWord(String word) {
    return dictionary.get(word);
}

}