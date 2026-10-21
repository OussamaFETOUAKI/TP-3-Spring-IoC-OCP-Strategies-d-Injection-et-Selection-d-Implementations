package metier;

import dao.IDao;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Map;

/**
 * Extension Step 20 : Injection de collections de beans DAO.
 * Démontre la capacité de Spring à injecter toutes les implémentations disponibles
 * dans une List et dans une Map indicée par le nom du bean.
 */
@Service
public class MetierMultiple implements IMetier {
    private final List<IDao> daos;
    private final Map<String, IDao> daoMap;

    public MetierMultiple(List<IDao> daos, Map<String, IDao> daoMap) {
        this.daos = daos;
        this.daoMap = daoMap;
    }

    @Override
    public double calcul() {
        // Somme de toutes les valeurs retournées par tous les DAO
        return daos.stream().mapToDouble(IDao::getValue).sum();
    }

    public List<IDao> getDaos() {
        return daos;
    }

    public Map<String, IDao> getDaoMap() {
        return daoMap;
    }
}
