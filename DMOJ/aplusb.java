import java.util.*;
import java.io.*;

public class aplusb {

	public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                int size = Integer.parseInt(sc.nextLine());
                String[] inputList = new String[size];
                for(int i=0; i < size; i++){
                        inputList[i] = sc.nextLine();
                }
                for(int i=0; i<size; i++){
			String[] input = inputList[i].split(" ");
			int x = Integer.parseInt(input[0]);
			int y = Integer.parseInt(input[1]);
                        System.out.println(x+y);
                }
 
	}

}