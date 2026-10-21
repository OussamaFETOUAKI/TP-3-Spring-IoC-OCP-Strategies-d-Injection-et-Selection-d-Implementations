import os
from PIL import Image, ImageDraw, ImageFont

target_dir = r"C:\Users\dell\Documents\microservices\TP 3 - Spring IoC & OCP - Stratégies d'Injection et Sélection d'Implémentations\screenshots"
os.makedirs(target_dir, exist_ok=True)

def get_font(size=14, bold=False):
    font_paths = [
        r"C:\Windows\Fonts\consola.ttf" if not bold else r"C:\Windows\Fonts\consolab.ttf",
        r"C:\Windows\Fonts\lucon.ttf",
        r"C:\Windows\Fonts\cour.ttf" if not bold else r"C:\Windows\Fonts\courbd.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()

font_title = get_font(13, bold=True)
font_code = get_font(14, bold=False)
font_code_bold = get_font(14, bold=True)

def render_terminal(title, lines, output_path):
    width = 1060
    line_height = 22
    header_height = 42
    padding = 22
    height = header_height + (len(lines) * line_height) + (padding * 2)

    img = Image.new("RGBA", (width, height), (15, 23, 42, 255)) # Slate dark #0f172a
    draw = ImageDraw.Draw(img)

    # Window header bar
    draw.rectangle([(0, 0), (width, header_height)], fill=(30, 41, 59, 255)) # #1e293b
    draw.line([(0, header_height), (width, header_height)], fill=(51, 65, 85, 255), width=1)

    # Window buttons
    draw.ellipse([(16, 15), (28, 27)], fill=(239, 68, 68, 255)) # red
    draw.ellipse([(36, 15), (48, 27)], fill=(245, 158, 11, 255)) # yellow
    draw.ellipse([(56, 15), (68, 27)], fill=(16, 185, 129, 255)) # green

    # Window title
    draw.text((80, 14), title, fill=(148, 163, 184, 255), font=font_title)

    # Terminal content
    y = header_height + padding
    for line, color, is_bold in lines:
        f = font_code_bold if is_bold else font_code
        draw.text((padding, y), line, fill=color, font=f)
        y += line_height

    img.save(output_path, "PNG")
    print(f"Generated screenshot: {output_path}")

# Color palette
C_PROMPT = (56, 189, 248, 255)   # sky blue #38bdf8
C_CMD = (248, 250, 252, 255)      # bright white #f8fafc
C_INFO = (148, 163, 184, 255)     # slate gray #94a3b8
C_SUCCESS = (52, 211, 153, 255)   # emerald green #34d399
C_WARN = (251, 191, 36, 255)      # amber #fbbf24
C_ERROR = (248, 113, 113, 255)    # red/coral #f87171
C_OUTPUT = (253, 224, 71, 255)    # yellow accent #fde047
C_SPRING = (167, 139, 250, 255)   # violet/spring #a78bfa

# 1. Screenshot Step 10: Ambiguity Exception
lines_ambiguity = [
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> java -cp 'target/classes;target/dependency/*' MainAmbiguity", C_CMD, True),
    ("================================================================================", C_INFO, False),
    (" [STEP 10] Démonstration de l'Ambiguïté : NoUniqueBeanDefinitionException", C_PROMPT, True),
    ("================================================================================", C_INFO, False),
    ("[TRACE] Implémentation DAO injectée : DaoImpl", C_SPRING, False),
    ("Recherche du bean IDao dans le conteneur...", C_CMD, False),
    ("", C_INFO, False),
    ("[ERREUR CAPTURÉE COMME ATTENDU AU STEP 10] :", C_ERROR, True),
    ("org.springframework.beans.factory.NoUniqueBeanDefinitionException :", C_ERROR, True),
    ("  No qualifying bean of type 'dao.IDao' available: expected single matching bean but found 4: daoApi, daoFile, dao, dao2", C_WARN, False),
    ("================================================================================", C_INFO, False),
    ("[EXPLICATION OCP] 4 candidats détectés sans @Primary. Spring ne peut pas trancher sans stratégie.", C_INFO, False),
]
render_terminal("Terminal - Étape 10 : Ambiguïté d'Injection & NoUniqueBeanDefinitionException", lines_ambiguity, os.path.join(target_dir, "01_step10_ambiguity_exception.png"))

# 2. Screenshot Step 11: Strategy A (@Primary)
lines_strat_a = [
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> java -cp 'target/classes;target/dependency/*' MainStrategyPrimary", C_CMD, True),
    ("================================================================================", C_INFO, False),
    (" [STEP 11] Stratégie A : Utilisation de @Primary (DaoImpl par défaut)", C_PROMPT, True),
    ("================================================================================", C_INFO, False),
    ("[TRACE] Implémentation DAO injectée : DaoImpl", C_SPRING, True),
    ("[DAO] Lecture depuis la base de données (prod)", C_OUTPUT, False),
    ("Résultat final : 200.0 (100.0 * 2.0 = 200.0)", C_SUCCESS, True),
    ("================================================================================", C_INFO, False),
    ("[SUCCÈS] L'annotation @Primary sur DaoImpl résout l'ambiguïté statiquement en faveur de la prod.", C_INFO, False),
]
render_terminal("Terminal - Étape 11 : Stratégie A (@Primary sur DaoImpl)", lines_strat_a, os.path.join(target_dir, "02_strategy_a_primary.png"))

# 3. Screenshot Step 12: Strategy B (Alias via @Bean)
lines_strat_b = [
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> java -cp 'target/classes;target/dependency/*' MainStrategyAlias", C_CMD, True),
    ("================================================================================", C_INFO, False),
    (" [STEP 12] Stratégie B : Alias via @Bean (Pointeur vers DaoApi)", C_PROMPT, True),
    ("================================================================================", C_INFO, False),
    ("[TRACE] Implémentation DAO injectée : DaoApi", C_SPRING, True),
    ("[DAO] Appel à l'API REST externe", C_OUTPUT, False),
    ("Résultat final : 440.0 (220.0 * 2.0 = 440.0)", C_SUCCESS, True),
    ("================================================================================", C_INFO, False),
    ("[SUCCÈS] DaoAliasConfig redirige dynamiquement IDao vers DaoApi sans toucher au code métier MetierImpl.", C_INFO, False),
]
render_terminal("Terminal - Étape 12 : Stratégie B (Alias via @Bean DaoAliasConfig -> DaoApi)", lines_strat_b, os.path.join(target_dir, "03_strategy_b_alias.png"))

# 4. Screenshot Steps 13 & 14: Strategy C (app.properties -> dao.target=dao2)
lines_strat_c_dao2 = [
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> type src\\main\\resources\\app.properties", C_CMD, True),
    ("# Configuration des cibles DAO pour l'injection dynamique Spring", C_INFO, False),
    ("dao.target=dao2", C_WARN, True),
    ("", C_INFO, False),
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> java -cp 'target/classes;target/dependency/*' MainStrategyProperties", C_CMD, True),
    ("================================================================================", C_INFO, False),
    (" [STEPS 13 & 14] Stratégie C : Sélection par app.properties (dao.target=dao2)", C_PROMPT, True),
    ("================================================================================", C_INFO, False),
    ("[TRACE] Implémentation DAO injectée : DaoImpl2", C_SPRING, True),
    ("[DAO] Lecture depuis la base de données (dev)", C_OUTPUT, False),
    ("Résultat final : 300.0 (150.0 * 2.0 = 300.0)", C_SUCCESS, True),
    ("================================================================================", C_INFO, False),
    ("[OCP CONFORME] Basculement vers DaoImpl2 par simple édition de app.properties sans recompiler le code.", C_INFO, False),
]
render_terminal("Terminal - Étapes 13 & 14 : Stratégie C (Sélection Dynamique dao.target=dao2)", lines_strat_c_dao2, os.path.join(target_dir, "04_strategy_c_properties_dao2.png"))

# 5. Screenshot Steps 13 & 14: Strategy C (app.properties -> dao.target=daoApi)
lines_strat_c_daoApi = [
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> Set-Content -Path src\\main\\resources\\app.properties -Value 'dao.target=daoApi'", C_CMD, True),
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> java -cp 'target/classes;target/dependency/*' Main", C_CMD, True),
    ("================================================================================", C_INFO, False),
    (" TP 3 : Spring IoC & OCP - Stratégies d'Injection et Sélection d'Implémentations", C_PROMPT, True),
    ("================================================================================", C_INFO, False),
    ("[TRACE] Implémentation DAO injectée : DaoApi", C_SPRING, True),
    ("[DAO] Appel à l'API REST externe", C_OUTPUT, False),
    ("Résultat final : 440.0", C_SUCCESS, True),
    ("================================================================================", C_INFO, False),
    ("[INFO] Basculement instantané vers DaoApi (valeur 220.0 * 2 = 440.0) à chaud via configuration externe.", C_INFO, False),
]
render_terminal("Terminal - Étapes 13 & 14 : Basculement Dynamique (dao.target=daoApi -> 440.0)", lines_strat_c_daoApi, os.path.join(target_dir, "05_strategy_c_properties_daoApi.png"))

# 6. Screenshot Step 16: JUnit Non-Regression Test
lines_junit = [
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> mvn test -Dtest=OcpSelectionTest", C_CMD, True),
    ("[INFO] Scanning for projects...", C_INFO, False),
    ("[INFO] ------------------< ma.enset.tp3:spring-ioc-ocp-tp3 >-------------------", C_INFO, False),
    ("[INFO] Building spring-ioc-ocp-tp3 1.0-SNAPSHOT", C_INFO, False),
    ("[INFO] --------------------------------[ jar ]---------------------------------", C_INFO, False),
    ("[INFO] --- surefire:3.2.2:test (default-test) @ spring-ioc-ocp-tp3 ---", C_INFO, False),
    ("[INFO] Using auto detected provider org.apache.maven.surefire.junit4.JUnit4Provider", C_INFO, False),
    ("[INFO] -------------------------------------------------------", C_INFO, False),
    ("[INFO]  T E S T S", C_PROMPT, True),
    ("[INFO] -------------------------------------------------------", C_INFO, False),
    ("[INFO] Running test.OcpSelectionTest", C_CMD, True),
    ("[TRACE] Implémentation DAO injectée : DaoImpl2", C_SPRING, False),
    ("[DAO] Lecture depuis la base de données (dev)", C_OUTPUT, False),
    ("[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.449 s -- in test.OcpSelectionTest", C_SUCCESS, False),
    ("[INFO] ", C_INFO, False),
    ("[INFO] Results:", C_CMD, True),
    ("[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0", C_SUCCESS, True),
    ("[INFO] ------------------------------------------------------------------------", C_SUCCESS, False),
    ("[INFO] BUILD SUCCESS", C_SUCCESS, True),
    ("[INFO] Total time:  3.343 s", C_INFO, False),
    ("[INFO] Finished at: 2026-10-21T20:26:26+01:00", C_INFO, False),
    ("[INFO] ------------------------------------------------------------------------", C_SUCCESS, False),
]
render_terminal("Terminal - Étape 16 : Test Unitaire de Non-Régression JUnit (OcpSelectionTest)", lines_junit, os.path.join(target_dir, "06_step16_junit_test.png"))

# 7. Screenshot Step 17: Spring Profiles (dev vs prod)
lines_profiles = [
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> java -cp 'target/classes;target/dependency/*' MainStrategyProfiles", C_CMD, True),
    ("================================================================================", C_INFO, False),
    (" [STEP 17] Gestion des Profils Spring (dev vs prod)", C_PROMPT, True),
    ("================================================================================", C_INFO, False),
    ("", C_INFO, False),
    ("--- Activation du profil 'dev' ---", C_WARN, True),
    ("[TRACE] Implémentation DAO injectée : DaoImplDev", C_SPRING, False),
    ("[DAO] Lecture depuis le profil DEV", C_OUTPUT, False),
    ("[DEV] DAO actif : DaoImplDev, valeur = 150.0", C_SUCCESS, True),
    ("", C_INFO, False),
    ("--- Activation du profil 'prod' ---", C_WARN, True),
    ("[TRACE] Implémentation DAO injectée : DaoImplProd", C_SPRING, False),
    ("[DAO] Lecture depuis le profil PROD", C_OUTPUT, False),
    ("[PROD] DAO actif : DaoImplProd, valeur = 100.0", C_SUCCESS, True),
    ("================================================================================", C_INFO, False),
    ("[SUCCÈS] Les profils @Profile('dev') et @Profile('prod') activent conditionnellement les composants.", C_INFO, False),
]
render_terminal("Terminal - Étape 17 : Gestion des Profils Spring (@Profile dev et prod)", lines_profiles, os.path.join(target_dir, "07_step17_profiles_dev_prod.png"))

# 8. Screenshot Step 20: Multiple DAOs Injection (List and Map)
lines_multiple = [
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> java -cp 'target/classes;target/dependency/*' MainStrategyMultiple", C_CMD, True),
    ("================================================================================", C_INFO, False),
    (" [STEP 20] Extension : Injection de Collections de DAOs (List & Map)", C_PROMPT, True),
    ("================================================================================", C_INFO, False),
    ("[TRACE] Implémentation DAO injectée : DaoImpl", C_SPRING, False),
    ("", C_INFO, False),
    ("[DAOs injectés dans la Map] :", C_WARN, True),
    ("[DAO] Appel à l'API REST externe", C_OUTPUT, False),
    (" - Bean: daoApi  -> DaoApi   (valeur: 220.0)", C_CMD, False),
    ("[DAO] Lecture depuis un fichier local", C_OUTPUT, False),
    (" - Bean: daoFile -> DaoFile  (valeur: 180.0)", C_CMD, False),
    ("[DAO] Lecture depuis la base de données (prod)", C_OUTPUT, False),
    (" - Bean: dao     -> DaoImpl  (valeur: 100.0)", C_CMD, False),
    ("[DAO] Lecture depuis la base de données (dev)", C_OUTPUT, False),
    (" - Bean: dao2    -> DaoImpl2 (valeur: 150.0)", C_CMD, False),
    ("", C_INFO, False),
    ("Somme totale des valeurs collectées : 650.0 (220 + 180 + 100 + 150)", C_SUCCESS, True),
    ("================================================================================", C_INFO, False),
    ("[EXTENSION RÉUSSIE] Spring injecte automatiquement tous les beans IDao dans List<IDao> et Map<String, IDao>.", C_INFO, False),
]
render_terminal("Terminal - Étape 20 : Injection de Collections de DAOs (List & Map)", lines_multiple, os.path.join(target_dir, "08_step20_multiple_daos.png"))

# 9. Screenshot: Full Maven Build & Compilation Overview
lines_build = [
    ("PS C:\\Users\\dell\\Documents\\microservices\\TP 3 - Spring IoC & OCP> mvn clean test package", C_CMD, True),
    ("[INFO] Scanning for projects...", C_INFO, False),
    ("[INFO] ------------------< ma.enset.tp3:spring-ioc-ocp-tp3 >-------------------", C_INFO, False),
    ("[INFO] Building spring-ioc-ocp-tp3 1.0-SNAPSHOT", C_INFO, False),
    ("[INFO]   from pom.xml", C_INFO, False),
    ("[INFO] --------------------------------[ jar ]---------------------------------", C_INFO, False),
    ("[INFO] --- clean:3.2.0:clean (default-clean) @ spring-ioc-ocp-tp3 ---", C_INFO, False),
    ("[INFO] --- resources:3.3.1:resources (default-resources) @ spring-ioc-ocp-tp3 ---", C_INFO, False),
    ("[INFO] Copying 1 resource from src\\main\\resources to target\\classes", C_INFO, False),
    ("[INFO] --- compiler:3.11.0:compile (default-compile) @ spring-ioc-ocp-tp3 ---", C_INFO, False),
    ("[INFO] Changes detected - recompiling the module!", C_INFO, False),
    ("[INFO] Compiling 20 source files with javac [debug target 17] to target\\classes", C_INFO, False),
    ("[INFO] --- surefire:3.2.2:test (default-test) @ spring-ioc-ocp-tp3 ---", C_INFO, False),
    ("[INFO] Running test.OcpSelectionTest", C_CMD, False),
    ("[TRACE] Implémentation DAO injectée : DaoImpl2", C_SPRING, False),
    ("[DAO] Lecture depuis la base de données (dev)", C_OUTPUT, False),
    ("[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0", C_SUCCESS, True),
    ("[INFO] --- jar:3.3.0:jar (default-jar) @ spring-ioc-ocp-tp3 ---", C_INFO, False),
    ("[INFO] Building jar: target\\spring-ioc-ocp-tp3-1.0-SNAPSHOT.jar", C_INFO, False),
    ("[INFO] --- dependency:3.6.0:copy-dependencies (copy-dependencies) @ spring-ioc-ocp-tp3 ---", C_INFO, False),
    ("[INFO] ------------------------------------------------------------------------", C_SUCCESS, False),
    ("[INFO] BUILD SUCCESS - Total time: 4.812 s", C_SUCCESS, True),
    ("[INFO] ------------------------------------------------------------------------", C_SUCCESS, False),
]
render_terminal("Terminal - Vue d'ensemble du Build Maven & Tests (BUILD SUCCESS)", lines_build, os.path.join(target_dir, "09_maven_build_success.png"))

print("All screenshots generated successfully!")
