import config.AppConfig;
import config.DynamicDaoConfig;
import metier.IMetier;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/**
 * Démonstration Stratégie C (Step 13 & 14) : Sélection par fichier app.properties.
 * Charge dao.target=dao2 depuis les propriétés externes.
 */
public class MainStrategyProperties {
    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println(" [STEPS 13 & 14] Stratégie C : Sélection par app.properties (dao.target=dao2)");
        System.out.println("================================================================================");

        AnnotationConfigApplicationContext context = 
            new AnnotationConfigApplicationContext(AppConfig.class, DynamicDaoConfig.class);

        IMetier metier = context.getBean(IMetier.class);
        double resultat = metier.calcul();

        System.out.println("Résultat final : " + resultat + " (150.0 * 2.0 = 300.0)");
        context.close();
        System.out.println("================================================================================");
    }
}
