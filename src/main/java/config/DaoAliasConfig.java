package config;

import dao.DaoApi;
import dao.IDao;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

/**
 * Stratégie B (Step 12) : Alias via @Bean.
 * Permet de définir un pointeur dynamique vers l'implémentation souhaitée (ici DaoApi)
 * sans modifier aucune classe DAO ni la classe Metier.
 */
@Configuration
public class DaoAliasConfig {

    @Bean
    @Primary
    public IDao daoAlias() {
        // Pointe vers l'implémentation API REST
        return new DaoApi();
    }
}
