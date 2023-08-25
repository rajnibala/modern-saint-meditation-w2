from sqlalchemy import create_engine, text

db_connectiond_string = "mysql+pymysql://ytejixpqrm45x9jsinlr:pscale_pw_OzL5NreI7wa1iQaeIvogHOORKEHXgJqHLggHRdrUs3L@aws.connect.psdb.cloud/modernsaintmeditation?charset=utf8mb4"

engine = create_engine(
  db_connectiond_string, 
  connect_args= { 
  "ssl":{
"ssl_ca": "/etc/ssl/cert.pem"    
  }
  })

def load_programs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from programs"))
        programs = []
        for row in result.all():
            programs.append(dict(row))
        return programs
     





   

    


      
      