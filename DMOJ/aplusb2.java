// Didn't completely solve
import java.util.*;
import java.io.*;

public class aplusb2 {

	public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                int size = Integer.parseInt(sc.nextLine());
                String[] inputList = new String[size];
                for(int i=0; i < size; i++){
                        inputList[i] = sc.nextLine();
                }
                for(int i=0; i<size; i++){
			String[] input = inputList[i].split(" ");
			String x = input[0];
			String y = input[1];
                        System.out.println(add(x,y));
                }
	}

        static String add(String s1,String s2){
                int carried = 0;
                String mode = "";
                if(s2.charAt(0) == '-'){
                        mode = "-";
                        s2=s2.substring(1);
                }
                else{
                        mode = "+";
                }
                if(s1.charAt(0) == '-'){
                        mode = "-" + mode;
                        s1=s1.substring(1);
                }
                else{
                        mode = "+" + mode;
                }

                boolean negative = false;

                if(s1.length() > s2.length()){
                        while(s1.length() > s2.length()){
                                s2 = "0"+s2;
                        }
                        if(mode.charAt(0) == '-'){
                                negative = true;
                        }
                }
                if(s2.length() > s1.length()){
                        while(s2.length() > s1.length()){
                                s1 = "0"+s1;
                        }
                        if(mode.charAt(1) == '-'){
                                negative = true;
                        }
                }
                if(mode.equals("++") || mode.equals("--")){
                        s1 = "0"+s1;
                        s2 = "0"+s2;
                }
                if(s1.length() == s2.length()){
                        if(mode.charAt(0) == '-' &&  s1.charAt(0) > s2.charAt(0)){
                                negative = true;
                        }
                        if(mode.charAt(1) == '-' &&  s1.charAt(0) < s2.charAt(0)){
                                negative = true;
                        }                    
                }

                String[] sum = new String[s1.length()];
                if(mode.equals("-+")){
                        String temp = s1;
                        s1 = s2;
                        s2 = temp;
                        mode = "+-";
                }
                for(int i=sum.length-1; i>=0; i--){
                        int x = Integer.parseInt(Character.toString(s1.charAt(i)));
                        int y = Integer.parseInt(Character.toString(s2.charAt(i)));
                        if(mode.equals("++") || mode.equals("--")){
                                int miniSum = carried + x + y;
                                if(miniSum > 9){
                                        miniSum = miniSum-10;
                                        carried = 1;
                                }
                                else{
                                        carried = 0;
                                }
                                sum[i] = ""+miniSum;
                        }
                        if(mode.equals("+-") && !negative){
                                int miniSum = carried + x - y;
                                if(miniSum < 0 && i != 0){
                                        miniSum = 10+miniSum;
                                        carried = -1;
                                }
                                else{
                                        carried = 0;
                                }
                                sum[i] = ""+miniSum;
                        }
                        if(mode.equals("+-") && negative){

                                int miniSum = carried + y - x;
                                if(miniSum < 0 && i != 0){
                                        miniSum = 10+miniSum;
                                        carried = -1;
                                }
                                else{
                                        carried = 0;
                                }
                                sum[i] = ""+miniSum;
                        }
                }
                String finalValue = String.join("",sum);

                while(finalValue.charAt(0) == '0' && finalValue.length() != 1){
                        finalValue = finalValue.substring(1);
                }
                if(negative){
                        finalValue = "-"+finalValue;
                }
                return finalValue;
        }



}