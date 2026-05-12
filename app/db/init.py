from app.db.commands import clean_retseptlar_table
from app.db.models import create_retseptlar_table
from app.services.boshlangich_malumotlar import add_retseptlar


def init_db():
    create_retseptlar_table()
    clean_retseptlar_table()
    add_retseptlar()
