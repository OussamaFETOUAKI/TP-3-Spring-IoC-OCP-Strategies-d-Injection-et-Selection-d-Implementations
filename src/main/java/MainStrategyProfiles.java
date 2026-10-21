import config.AppConfig;
import dao.IDao;
import metier.IMetier;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/**
 * Démonstration Step 17 : Profils Spring (dev et prod).
 * Active alternativement le profil 'dev' (150.0 * 2 = 300.0) et 'prod' (100.0 * 2 = 200.0).
 */
public class MainStrategyProfiles {
    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println(" [STEP 17] Gestion des Profils Spring (dev vs prod)");
        System.out.println("================================================================================");

        // 1. Profil DEV
        System.out.println("\n--- Activation du profil 'dev' ---");
        AnnotationConfigApplicationContext devContext = new AnnotationConfigApplicationContext();
        devContext.getEnvironment().setActiveProfiles("dev");
        devContext.register(AppConfig.class);
        devContext.refresh();

        IDao devDao = devContext.getBean("daoDev", IDao.class);
        System.out.println("[DEV] DAO actif : " + devDao.getClass().getSimpleName() + ", valeur = " + devDao.getValue());
        devContext.close();

        // 2. Profil PROD
        System.out.println("\n--- Activation du profil 'prod' ---");
        AnnotationConfigApplicationContext prodContext = new AnnotationConfigApplicationContext();
        prodContext.getEnvironment().setActiveProfiles("prod");
        prodContext.register(AppConfig.class);
        prodContext.refresh();

        IDao prodDao = prodContext.getBean("daoProd", IDao.class);
        System.out.println("[PROD] DAO actif : " + prodDao.getClass().getSimpleName() + ", valeur = " + prodDao.getValue());
        prodContext.close();

        System.out.println("================================================================================");
    }
}
