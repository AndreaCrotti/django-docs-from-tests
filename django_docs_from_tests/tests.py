from unittest import TestCase

from django_docs_from_tests import docs_generator


class TestHtmlGeneration(TestCase):
    def test_test_name_is_in_response(self):
        test = docs_generator.TestResult('test-name')
        html = test.render()
        self.assertIn('test-name', html)

    def test_report_gen(self):
        test = docs_generator.TestResult('test-name')
        gen = docs_generator.Report('sample report')
        gen.add(test)
        res = gen.render()
        self.assertIn('test-name', res)


class ReportModelTest(TestCase):
    pass


class ResponseModelTest(TestCase):
    pass
