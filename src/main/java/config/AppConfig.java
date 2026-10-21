package config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

/**
 * Configuration Spring principale (Step 8 & Step 14).
 * Active le scan des composants dans dao et metier et charge app.properties.
 */
@Configuration
@ComponentScan(basePackages = {"dao", "metier"})
@PropertySource(value = "classpath:app.properties", ignoreResourceNotFound = true)
public class AppConfig {
    // Configuration de base
}
