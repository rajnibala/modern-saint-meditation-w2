from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://svnb48ooni63f7o22ofe:pscale_pw_xSUBDmAUVN76fpARnZ83gtiplx4mW5vbnsbH0oV2S7@aws.connect.psdb.cloud/modernsaintmeditation?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={
  "ssl" : {
 "ssl_ca": "/home/gord/client-ssl/ca.pem"
    
  }
})

 with engine.connect() as conn:
    result = conn.execute(text("select * from program"))
   print(result.all())
