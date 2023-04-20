from decouple import config

class Config :
    SECRET_KEY=config('SECRET_KEY')

## Permite que se reinicie el server en cada cambio
class DevelopmentConfig(Config):
    DEBUG=True


config = {
    'development':DevelopmentConfig
}