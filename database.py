import rethinkdb as r

__node_table = 'node'
__way_table = 'way'
__relation_table = 'relation'


def __check_database(database_name, session):
    databases = r.db_list().run(session)
    for database in databases:
        if database == database_name:
            return

    r.db_create(database_name).run(session)


def __check_table(database_name, table_name, session):
    tables = r.db(database_name).table_list().run(session)
    for table in tables:
        if table == table_name:
            return

    r.db(database_name).table_create(table_name).run(session)


def connect(host, port):
    return r.connect(host, port)


def init_db(host, port, dbname):
    session = connect(host, port)
    __check_database(dbname, session)
    __check_table(dbname, __node_table, session)
    __check_table(dbname, __way_table, session)
    __check_table(dbname, __relation_table, session)
    close_session(session)


def close_session(session):
    session.close()


def save_nodes(nodes, dbname, session):
    r.db(dbname).table(__node_table).insert(nodes).run(session)


def save_ways(ways, dbname, session):
    r.db(dbname).table(__way_table).insert(ways).run(session)


def save_relations(relations, dbname, session):
    r.db(dbname).table(__relation_table).insert(relations).run(session)