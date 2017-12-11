# -*- coding: utf-8 -*-

from django.db import DEFAULT_DB_ALIAS, connections
from django.test import testcases
from django.test.utils import CaptureQueriesContext

__author__ = """Prismatic Digital"""
__email__ = 'contact@prismaticdigital.com'
__version__ = '0.1.1'


class _AssertMaxNumQueriesContext(CaptureQueriesContext):
    def __init__(self, test_case, num, connection):
        self.test_case = test_case
        self.num = num
        super(_AssertMaxNumQueriesContext, self).__init__(connection)

    def __exit__(self, exc_type, exc_value, traceback):
        super(_AssertMaxNumQueriesContext, self).__exit__(exc_type, exc_value, traceback)
        if exc_type is not None:
            return
        executed = len(self)
        self.test_case.assertLessEqual(
            executed, self.num,
            "%d queries executed, max %d expected\nCaptured queries were:\n%s" % (
                executed, self.num,
                '\n'.join(
                    query['sql'] for query in self.captured_queries
                )
            )
        )


class MaxNumQueriesMixin(object):

    def assertMaxNumQueries(self, num, func=None, *args, **kwargs):
        using = kwargs.pop("using", DEFAULT_DB_ALIAS)
        conn = connections[using]

        context = _AssertMaxNumQueriesContext(self, num, conn)
        if func is None:
            return context

        with context:
            func(*args, **kwargs)


class TransactionTestCase(MaxNumQueriesMixin, testcases.TransactionTestCase):
    pass
