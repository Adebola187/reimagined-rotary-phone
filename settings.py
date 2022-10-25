from os import environ

SESSION_CONFIGS = [
    dict(
        name='experience',
        app_sequence=['experience'],
        display_name = 'Decision_making Experiment Experience Paradigm',
        num_demo_participants=8,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.20, participation_fee=8.00, doc=""
)

PARTICIPANT_FIELDS = ['task_rounds', 'Total', 'choices' 'replacechar', 'in_round', 'NUM_ROUNDS', 'selected_round']
SESSION_FIELDS = ["answers", "previoupage", "ROUND_COUNT"]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = ''
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8237971376520'
