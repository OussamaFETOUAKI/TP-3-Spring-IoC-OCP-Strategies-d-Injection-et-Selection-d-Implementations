package metier;

/**
 * Interface métier définissant le contrat de calcul.
 */
public interface IMetier {
    /**
     * Effectue le traitement métier basé sur les données du DAO.
     * @return résultat du calcul
     */
    double calcul();
}
