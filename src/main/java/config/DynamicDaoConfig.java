package config;

import dao.DaoApi;
import dao.DaoFile;
import dao.DaoImpl;
import dao.DaoImpl2;
import dao.IDao;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

/**
 * Stratégie C (Step 13) : Sélection par fichier de propriétés externe.
 * Lit la clé dao.target depuis app.properties et instancie dynamiquement
 * l'implémentation sélectionnée sans recompiler le projet ni modifier MetierImpl.
 */
@Configuration
public class DynamicDaoConfig {

    @Value("${dao.target:dao2}")
    private String daoTarget;

    @Bean
    @Primary
    public IDao dynamicDao() {
        switch (daoTarget) {
            case "dao":
                return new DaoImpl();
            case "dao2":
                return new DaoImpl2();
            case "daoFile":
                return new DaoFile();
            case "daoApi":
                return new DaoApi();
            default:
                throw new IllegalArgumentException("Cible DAO inconnue: " + daoTarget);
        }
    }
}
