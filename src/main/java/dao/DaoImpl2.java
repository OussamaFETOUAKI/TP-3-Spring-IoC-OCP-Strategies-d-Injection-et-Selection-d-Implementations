package dao;

import org.springframework.stereotype.Component;

/**
 * Implémentation DAO simulant une base de données de développement.
 */
@Component("dao2")
public class DaoImpl2 implements IDao {
    @Override
    public double getValue() {
        System.out.println("[DAO] Lecture depuis la base de données (dev)");
        return 150.0;
    }
}
