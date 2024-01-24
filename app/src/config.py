## IMPORT REQUIRED MODULES
import os

## DEFINE APPLICATION CONFIGURATION
class ApplicationConfig:
    SECRET_KEY = os.environ.get("SECRET_KEY", default="ThisIsMySuperSecretFakeSecretKey")
