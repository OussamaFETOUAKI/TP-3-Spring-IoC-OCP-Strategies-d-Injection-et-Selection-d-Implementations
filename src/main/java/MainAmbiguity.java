import config.AppConfig;
import dao.IDao;
import metier.IMetier;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

/**
 * Démonstration du problème d'ambiguïté (Step 10).
 * Montre l'exception NoUniqueBeanDefinitionException lorsque 4 implémentations IDao
 * sont détectées par @ComponentScan sans règle de désambiguïsation.
 */
public class MainAmbiguity {
    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println(" [STEP 10] Démonstration de l'Ambiguïté : NoUniqueBeanDefinitionException");
        System.out.println("================================================================================");

        try {
            // Tentative de résolution de IDao sans @Primary : Spring trouve 4 beans et lève NoUniqueBeanDefinitionException
            AnnotationConfigApplicationContext context = 
                new AnnotationConfigApplicationContext(AppConfig.class);

            System.out.println("Recherche du bean IDao dans le conteneur...");
            IDao dao = context.getBean(IDao.class);
            System.out.println("DAO récupéré : " + dao);
            context.close();
        } catch (Exception e) {
            System.out.println("\n[ERREUR CAPTURÉE COMME ATTENDU AU STEP 10] :");
            System.out.println(e.getClass().getName() + " : " + e.getMessage());
            if (e.getCause() != null) {
                System.out.println("Cause : " + e.getCause().getMessage());
            }
        }
        System.out.println("================================================================================");
    }
}
