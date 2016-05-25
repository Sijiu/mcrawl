# -*- coding=utf-8 -*-

"""
@author:lance
@date:
@version:
@description:
"""
from lib.nosql.mongo_util import FeedsWarehouse


def get_schema(project_id, site):

    project_enter = FeedsWarehouse("project")
    schemas = project_enter.get({"_id": project_id})["Schemas"]

    for schema in schemas:
        if schema["Site"] == site:
            return schema


def get_schema2(project_name, site):

    project_enter = FeedsWarehouse("project")
    schemas = project_enter.get({"ServiceName": project_name})["Schemas"]

    for schema in schemas:
        if schema["Site"] == site:
            return schema
    return None
