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
	
	
	
	
}