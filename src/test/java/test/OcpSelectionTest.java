package test;

import config.AppConfig;
import config.DynamicDaoConfig;
import metier.IMetier;
import org.junit.Test;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

/**
 * Test de non-régression validant le principe OCP (Step 16).
 * Vérifie que le conteneur Spring IoC sélectionne et injecte correctement
 * l'implémentation attendue sans modification de la classe métier MetierImpl.
 */
public class OcpSelectionTest {

    @Test
    public void testDaoDynamicSelection() {
        AnnotationConfigApplicationContext context = 
            new AnnotationConfigApplicationContext(AppConfig.class, DynamicDaoConfig.class);

        IMetier metier = context.getBean(IMetier.class);
        assertNotNull("Le bean IMetier ne doit pas être null", metier);

        // Avec dao.target=dao2 défini dans app.properties :
        // dao2.getValue() = 150.0 => calcul() = 150.0 * 2.0 = 300.0
        double resultat = metier.calcul();
        assertEquals(300.0, resultat, 0.001);

        context.close();
    }
}
