from unittest import TestCase

from django_docs_from_tests import docs_generator


class TestHtmlGeneration(TestCase):
    def test_test_name_is_in_response(self):
        test = docs_generator.TestResult('test-name')
        html = test.render()
        self.assertIn('test-name', html)

    def test_report_gen(self):
        pass
