from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://yrpvqouzymlz00makhh9:pscale_pw_iSPBfxF58hLdpWD6Tmlem4rXtFeQMOH3WP0zGnXjGlf@aws.connect.psdb.cloud/meditation?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={
    "ssl": {
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})

def load_program_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM program"))
        program = [dict(row) for row in result.all()]
        return program

