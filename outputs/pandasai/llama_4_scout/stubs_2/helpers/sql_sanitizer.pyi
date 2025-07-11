import os
import re

import sqlglot
from sqlglot import parse_one
from sqlglot.optimizer.qualify_columns import quote_identifiers


def sanitize_view_column_name(relation_name: str) -> str:
    ...


def sanitize_sql_table_name(table_name: str) -> str:
    ...


def sanitize_file_name(filepath: str) -> str:
    ...


def is_sql_query_safe(query: str, dialect: str = "postgres") -> bool:
    ...


def is_sql_query(query: str) -> bool:
    ...