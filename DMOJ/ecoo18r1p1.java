// Worked on actual ECOO day, but not on DMOJ
import java.util.*;
import java.io.*;

public class ecoo18r1p1 {

	public static void main(String[] args) {
		// FileReader fileReader = null;
		// try {
			// fileReader = new FileReader("DATA11.txt");
			// BufferedReader bFileReader = new BufferedReader(fileReader);
			Scanner sc = new Scanner(System.in);
			String line = "";
			for (int i = 0; i < 10; i++) {
				line = sc.nextLine();
				String[] params = line.split(" ");
				int max = Integer.parseInt(params[0]);
				int days = Integer.parseInt(params[1]);
				int counter = -1;
				boolean done = false;

				for (int day = 0; day < days; day++) {
					String letter = sc.nextLine();
					if (done)
						continue;
					if (letter.matches("B") && counter == -1) {
						counter = max;
					} else if (counter > 0) {
						counter--;
						if (letter.matches("B")) {
							counter += max;
						}
					}
					if (counter == 0) {
						// System.out.println(0);
						done = true;
					}

					// System.out.println(counter);
				}
				if (counter == 0) {
					System.out.println(0);
				} else if (counter == -1) {
					System.out.println(0);
				} else {
					System.out.println(counter > 0 ? counter - 1 : counter);
				}
			}
		//} catch (IOException e) {
			// TODO Auto-generated catch block
			//e.printStackTrace();
		//}
	}

}