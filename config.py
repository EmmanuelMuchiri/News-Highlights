import os


class Config:

    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?country=us&apiKey=bc727edb606e4bb9a18ed13582730c86'
    # NEWS_API_ARTICLES_URL='https://newsapi.org/v2/everything?q=bitcoin&apiKey=bc727edb606e4bb9a18ed13582730c86'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig

}