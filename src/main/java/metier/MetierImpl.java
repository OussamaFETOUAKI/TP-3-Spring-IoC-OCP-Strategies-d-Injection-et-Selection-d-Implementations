package metier;

import dao.IDao;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;
import javax.annotation.PostConstruct;

/**
 * Implémentation principale du service métier.
 * Respecte le principe OCP : dépend uniquement de l'abstraction IDao et ne change jamais
 * quelle que soit la source de données configurée.
 */
@Service("metier")
@Primary
public class MetierImpl implements IMetier {
    private final IDao dao;

    /**
     * Injection par constructeur recommandée par Spring.
     * @param dao dépendance vers l'interface IDao
     */
    public MetierImpl(IDao dao) {
        this.dao = dao;
    }

    @PostConstruct
    public void init() {
        System.out.println("[TRACE] Implémentation DAO injectée : " + dao.getClass().getSimpleName());
    }

    @Override
    public double calcul() {
        double valeur = dao.getValue();
        // Logique métier : multiplie par 2 la valeur récupérée
        return valeur * 2.0;
    }

    public IDao getDao() {
        return dao;
    }
}
