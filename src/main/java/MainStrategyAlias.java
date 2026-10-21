import config.AppConfig;
import config.DaoAliasConfig;
import metier.IMetier;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/**
 * Démonstration Stratégie B (Step 12) : Alias via @Bean.
 * Utilise DaoAliasConfig pour pointer dynamiquement vers DaoApi (220.0 * 2 = 440.0)
 * sans modifier ni MetierImpl ni aucune classe DAO.
 */
public class MainStrategyAlias {
    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println(" [STEP 12] Stratégie B : Alias via @Bean (Pointeur vers DaoApi)");
        System.out.println("================================================================================");

        AnnotationConfigApplicationContext context = 
            new AnnotationConfigApplicationContext(AppConfig.class, DaoAliasConfig.class);

        IMetier metier = context.getBean(IMetier.class);
        double resultat = metier.calcul();

        System.out.println("Résultat final : " + resultat + " (220.0 * 2.0 = 440.0)");
        context.close();
        System.out.println("================================================================================");
    }
}
