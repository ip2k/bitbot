import logging
import sqlite3
import time

class SQLiteHandler(logging.Handler): # Inherit from logging.Handler
"""
SQLiteHandler class override specifically to support using the python logging module to log to sqlite
"""
    def __init__(self, filename):
        global db
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Our custom argument
        db = sqlite3.connect(filename)
        db.execute("CREATE TABLE IF NOT EXISTS debug(date text, loggername text, srclineno integer, func text, level text, msg text)")
        db.commit()

    def emit(self, record):
        # record.message is the log message
        thisdate = time.time()
        print record.getMessage()
        db.execute('INSERT INTO debug(date, loggername, srclineno, func, level, msg) VALUES(?,?,?,?,?,?)', (thisdate, record.name, record.lineno, record.funcName, record.levelname, record.msg))
        db.commit()
