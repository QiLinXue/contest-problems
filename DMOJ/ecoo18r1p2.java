// Worked on actual ECOO day, but not on DMOJ

import java.util.*;
import java.io.*;

public class ecoo18r1p2 {

	public static void main(String[] args) {
		    // try {
			// fileReader = new FileReader("DATA22.txt");
			// BufferedReader bFileReader = new BufferedReader(fileReader);
            Scanner sc = new Scanner(System.in);
			String line = null;
			Map<Integer, Integer> mins = new HashMap<Integer, Integer>();
            // int max = Integer.parseInt(sc.nextLine());
			// for (int z=0; z<max+1; z++) {
                line = sc.nextLine();
				int linesToRead = Integer.parseInt(line);
				for (int i = 0; i < linesToRead; i++) {
					String lines = sc.nextLine();
					String[] numbers = lines.split(" ");
					int runningMin = Integer.MAX_VALUE;
					for (int j = 2; j < numbers.length; j++) {
						if (Integer.parseInt(numbers[j]) < runningMin) {
							runningMin = Integer.parseInt(numbers[j]);
						}
					}
					mins.put(Integer.parseInt(numbers[0]), runningMin);
				}
				int min = Integer.MAX_VALUE;
				for (int x : mins.keySet()) if (mins.get(x) < min) min = mins.get(x);
				List<Integer> shortests = new ArrayList<Integer>();
				for (int x : mins.keySet()) {
					if (mins.get(x) == min) {
						shortests.add(x);
					}
				}
				System.out.println((min + " ") + (shortests.toString().replace('[', '{').replace(']', '}').replace(" ", "")));
			//}
			// bFileReader.close();
		// } catch (IOException e) {
		// 	// TODO Auto-generated catch block
		// 	e.printStackTrace();
		// }
	}

}