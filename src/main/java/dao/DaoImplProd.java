package dao;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

/**
 * Implémentation DAO active uniquement sur le profil Spring 'prod'.
 */
@Component("daoProd")
@Profile("prod")
public class DaoImplProd implements IDao {
    @Override
    public double getValue() {
        System.out.println("[DAO] Lecture depuis le profil PROD");
        return 100.0;
    }
}
