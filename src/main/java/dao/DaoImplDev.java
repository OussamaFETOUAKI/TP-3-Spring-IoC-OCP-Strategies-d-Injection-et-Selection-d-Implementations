package dao;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

/**
 * Implémentation DAO active uniquement sur le profil Spring 'dev'.
 */
@Component("daoDev")
@Profile("dev")
public class DaoImplDev implements IDao {
    @Override
    public double getValue() {
        System.out.println("[DAO] Lecture depuis le profil DEV");
        return 150.0;
    }
}
