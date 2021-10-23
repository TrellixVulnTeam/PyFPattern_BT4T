def get_key_columns(self, cursor, table_name):
    cursor.execute("\n            SELECT a1.attname, c2.relname, a2.attname\n            FROM pg_constraint con\n            LEFT JOIN pg_class c1 ON con.conrelid = c1.oid\n            LEFT JOIN pg_class c2 ON con.confrelid = c2.oid\n            LEFT JOIN pg_attribute a1 ON c1.oid = a1.attrelid AND a1.attnum = con.conkey[1]\n            LEFT JOIN pg_attribute a2 ON c2.oid = a2.attrelid AND a2.attnum = con.confkey[1]\n            WHERE\n                c1.relname = %s AND\n                con.contype = 'f' AND\n                c1.relnamespace = c2.relnamespace AND\n                pg_catalog.pg_table_is_visible(c1.oid)\n        ", [table_name])
    return cursor.fetchall()