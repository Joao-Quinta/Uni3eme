class TP1 {
    public static void main(String[] args) {
		
		    ////////////////////////////////// code fourni //////////////////////////////
			//Pour simplifier on considere que les arguments seront tous des double, 
			//i.e., notes entre 1.0 et 6.0 (pas de gestion des exceptions)
			
			//la longeur du tableau args est stockee dans la champ length de args, 
			//que vous pouvez pour l'instant simplement considerer comme une variable 
			// qui est automatiquement initialisee par la JVM lors du runtime et dont 
			//on accede avec la notation args.length (notation object)
			int n = args.length;
			
			double[] notes = new double[n];
			
			//convertir  tableau de Strings en tableau de double
			System.out.println("Notes:\n");
			notes = TP1Utils.str2double(args,n);
			
			//affichage des notes passees en arguments en ligne de commande
			TP1Utils.dispArr(notes, n);
			
			//////////////////////////////////////////////////////////////////////////////
			
			//A completer
			
			
    }
}