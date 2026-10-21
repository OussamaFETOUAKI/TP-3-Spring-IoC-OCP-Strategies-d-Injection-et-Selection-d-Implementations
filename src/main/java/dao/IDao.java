package dao;

/**
 * Interface DAO définissant le contrat d'accès aux données.
 * Point de couplage faible entre le métier et les sources de données (Principe OCP).
 */
public interface IDao {
    /**
     * Récupère une valeur numérique depuis la source de données.
     * @return la valeur récupérée
     */
    double getValue();
}
