import config.config_database as cfg
from datetime import date

def get_OutletName(outletid):
    # cfg.db_cursor.execute("SET SEARCH_PATH TO public;")
    query = """select "Outlet_Name" from "Outlets" WHERE "OutletID" = '{}';""".format(outletid)
    cfg.db_cursor.execute(query)
    outlet_name = cfg.db_cursor.fetchone()
    # print(outlet_name[0])
    outlet_name = outlet_name[0]
    return outlet_name

def get_Audit(outletid, period):
    query = """SELECT * FROM "eAudit_setup" INNER JOIN "Products" ON "eAudit_setup"."ProductID" = "Products"."ProductID" WHERE "OutletID" = '{}' AND "Period" = '{}';""".format(outletid, period)
    # query = """SELECT * FROM public."eAudit_setup" INNER JOIN public."Products" ON "eAudit_setup"."ProductID" = "Products"."ProductID" WHERE "OutletID" = '55555' AND "Period" = '202001'"""
    cfg.db_cursor.execute(query)
    audit = cfg.db_cursor.fetchall()
    print(audit)
    return audit

def insert_Audit(outlet, period, sku, instock, onshelf, label):
    cfg.db_cursor.execute("""
    SELECT 
    * 
    FROM 
    "eAudit_facts"
    WHERE
    "OutletID" = '{}'
    AND
    "Period" = '{}'
    AND
    "ProductID" = '{}'
    """.format(outlet,period, sku))
    result = cfg.db_cursor.fetchone()
    if(result):
        cfg.db_cursor.execute("""
        DELETE 
        FROM 
        "eAudit_facts"
        WHERE
        "OutletID" = '{}'
        AND
        "Period" = '{}'
        AND
        "ProductID" = '{}'
        """.format(outlet, period, sku))
        cfg.conn.commit()
        qinstock = 'instock'
        today = date.today()
        qonshelf = 'onshelf'
        qlabel = 'label'
        cfg.db_cursor.execute("INSERT INTO eAudit_facts VALUES (?, ?, ?, ?, ?, ?)", (outlet, period, sku, qinstock, instock, today)) #
        cfg.conn.commit()
        cfg.db_cursor.execute("INSERT INTO eAudit_facts VALUES (?, ?, ?, ?, ?, ?)", (outlet, period, sku, qonshelf, onshelf, today)) #
        cfg.conn.commit()
        cfg.db_cursor.execute("INSERT INTO eAudit_facts VALUES (?, ?, ?, ?, ?, ?)", (outlet, period, sku, qlabel, label, today)) #
        cfg.conn.commit()
    else:
        qinstock = 'instock'
        today = date.today()
        qonshelf = 'onshelf'
        cfg.db_cursor.execute("INSERT INTO eAudit_facts VALUES (?, ?, ?, ?, ?, ?)", (outlet, period, sku, qinstock, instock, today)) #
        cfg.conn.commit()
        cfg.db_cursor.execute("INSERT INTO eAudit_facts VALUES (?, ?, ?, ?, ?, ?)", (outlet, period, sku, qonshelf, onshelf, today)) #
        cfg.conn.commit()
        cfg.db_cursor.execute("INSERT INTO eAudit_facts VALUES (?, ?, ?, ?, ?, ?)", (outlet, period, sku, qlabel, label, today)) #
        cfg.conn.commit()

    success = "Success"

    # cfg.db_cursor.execute("INSERT INTO table VALUES (%s, %s, %s)", (var1, var2, var3)) #
    return success

# def check_Audit(outletid, period, sku)

# get_OutletName(2225399)
# get_Audit("2225399","202002")

# insert_Audit("2225399","202002","574","yes", "yes")
