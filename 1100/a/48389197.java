// package ItsaProject;

import java.util.Scanner;
import java.lang.*;


public class baka {

	
	
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int k = in.nextInt();
		int [] tabinf= new int [n];
		int [] b=new int [n];
		int testwale=0;
		int faltu=0;
		
		
		
		
				
		for (int i = 0; i < n; i++) {
			tabinf[i]=in.nextInt();
			if (tabinf[i]==1) {
				testwale++;
				
				
				
			}
			else {
				faltu++;
				
			}
			
			
		}
		for (int i = 0; i < n; i++) {
			int l=0;
			int m=0;
			int e=testwale;
			int s=faltu;
			
			
			for (int j = 0; j < tabinf.length; j++) {
				
				if ((Math.abs(j-i))%k==0) {
					if (tabinf[j]==1) {
						e--;
						
					}
					else {
						s--;
						
						
					}
					
					
				}
			}
			b[i]=Math.abs(e-s);
			
			
				
			}
		int max=0;
		for (int i = 0; i < b.length; i++) {
			if (b[i]>max) {
				max=b[i];
				
			}
		
		}
			System.out.println(max);
			
		}
		
		
	}

