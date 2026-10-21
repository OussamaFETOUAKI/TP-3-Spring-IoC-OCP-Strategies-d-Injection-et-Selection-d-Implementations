import config.AppConfig;
import config.DynamicDaoConfig;
import metier.IMetier;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/**
 * Point d'entrée principal de l'application (Step 9).
 * Initialise le conteneur Spring IoC et exécute la logique métier sans modifier MetierImpl.
 */
public class Main {
    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println(" TP 3 : Spring IoC & OCP - Stratégies d'Injection et Sélection d'Implémentations");
        System.out.println("================================================================================");

        // Initialisation du conteneur Spring avec configuration des beans et chargement de app.properties
        AnnotationConfigApplicationContext context = 
            new AnnotationConfigApplicationContext(AppConfig.class, DynamicDaoConfig.class);

        // Récupération du bean métier (couplage faible via l'interface IMetier)
        IMetier metier = context.getBean(IMetier.class);

        // Exécution du calcul métier
        double resultat = metier.calcul();
        System.out.println("Résultat final : " + resultat);

        // Fermeture propre du contexte
        context.close();
        System.out.println("================================================================================");
    }
}
