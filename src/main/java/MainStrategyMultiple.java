import config.AppConfig;
import dao.IDao;
import metier.MetierMultiple;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/**
 * Démonstration Step 20 : Injection de plusieurs DAO (List<IDao> et Map<String, IDao>).
 * Agrège les valeurs de l'ensemble des beans IDao enregistrés.
 */
public class MainStrategyMultiple {
    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println(" [STEP 20] Extension : Injection de Collections de DAOs (List & Map)");
        System.out.println("================================================================================");

        AnnotationConfigApplicationContext context = 
            new AnnotationConfigApplicationContext(AppConfig.class);

        MetierMultiple metierMultiple = context.getBean(MetierMultiple.class);

        System.out.println("\n[DAOs injectés dans la Map] :");
        metierMultiple.getDaoMap().forEach((beanName, daoInstance) -> {
            System.out.println(" - Bean: " + beanName + " -> " + daoInstance.getClass().getSimpleName() + " (valeur: " + daoInstance.getValue() + ")");
        });

        double sommeTotale = metierMultiple.calcul();
        System.out.println("\nSomme totale des valeurs collectées : " + sommeTotale);
        System.out.println("================================================================================");

        context.close();
    }
}
