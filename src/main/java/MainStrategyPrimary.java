import dao.DaoImpl;
import dao.IDao;
import metier.IMetier;
import metier.MetierImpl;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

/**
 * Démonstration Stratégie A (Step 11) : Utilisation de @Primary.
 * Définit DaoImpl comme le choix par défaut pour IDao.
 */
public class MainStrategyPrimary {

    @Configuration
    static class StrategyAPrimaryConfig {
        @Bean
        @Primary
        public IDao daoPrimary() {
            return new DaoImpl();
        }

        @Bean
        public IMetier metier(IDao dao) {
            return new MetierImpl(dao);
        }
    }

    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println(" [STEP 11] Stratégie A : Utilisation de @Primary (DaoImpl par défaut)");
        System.out.println("================================================================================");

        AnnotationConfigApplicationContext context = 
            new AnnotationConfigApplicationContext(StrategyAPrimaryConfig.class);

        IMetier metier = context.getBean(IMetier.class);
        double resultat = metier.calcul();

        System.out.println("Résultat final : " + resultat + " (100.0 * 2.0 = 200.0)");
        context.close();
        System.out.println("================================================================================");
    }
}
