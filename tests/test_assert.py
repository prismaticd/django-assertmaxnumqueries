# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model

from django_assertmaxnumqueries import TransactionTestCase

User = get_user_model()


def do_queries(n=1):
    for n in range(0, n):
        list(User.objects.filter(id=n))


class TestAssertMaxNumQueries(TransactionTestCase):

    def testAssertMaxNumQueries(self):
        for n in range(0, 4):
            with self.assertMaxNumQueries(n):
                do_queries(n)

            self.assertMaxNumQueries(n, do_queries, n)
            self.assertMaxNumQueries(n + 1, do_queries, n)

            with self.assertRaises(AssertionError):
                self.assertMaxNumQueries(n, do_queries, n + 1)

            self.assertNumQueries(n, do_queries, n)
