import java.lang.Math;

class TP1Utils{

	////////////////// code fourni aux etudiants ///////////////////////////

	//caster les elemnts de arr en double et stocker dans
	//une array d double
	static double[] str2double(String[] arrIn, int n)	{
		//on utilise ici la fonction parsedouble qui prend
		//en argument un String et renvoie un double
		double[] arrOut = new double[n];
		for(int i=0;i<n;i++){
			arrOut[i] = Double.parseDouble(arrIn[i]);
		}
		return arrOut;
	}

	//affichage d un tableai d double
	static void dispArr(double[] arr, int n){
		for(int i=0;i<n;i++){
			System.out.println(arr[i]);
		}
	}


	////////////////////////////////////////////////////////////////////////

	//A vous d ajouter les fonctions statiques demandees dans le TP et de les
	//appeler dans le main

	//calcul et affiche la moyenne
	static double calMoye(double[] arr, int n){
		double total = 0.0;
		for(int i=0;i<n;i++){
			total = total + arr[i];
		}
		total = total/n;

		return total;
	}

	static double calEcar(double[] arr, int n){
		double moyenne = calMoye(arr, n);
		double sum = 0.0;
		for(int i=0;i<n;i++){
			sum = sum + Math.pow((arr[i]-moyenne), 2);
		}
		sum = sum / n;
		sum = Math.sqrt(sum);
		return sum;
	}

	static double[] triBulles(double[] arr, int n){
		for (int i=n-1; i>0; i--){
			for (int j=0; j<i-1; j++){
				if (arr[j+1] < arr[j]){
					double j_0 = arr[j];
					double j_1 = arr[j+1];
					arr[j] = j_1;
					arr[j+1] = j_0;
				}
			}
		}
		return arr;
	}

	static double calMedi(double[] arr, int n){
		double mediane;
		arr = triBulles(arr, n);
		if (n%2 == 0){
			mediane = (arr[n/2] + arr[(n/2)-1])/2;
		}else{
			int m = (int) Math.ceil(n/2);
			mediane = arr[m];
		}
		return mediane;
	}
}
