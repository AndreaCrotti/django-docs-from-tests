from setuptools import setup, find_packages

package = 'django-nose-api-docs'
version = '0.1'

setup(
    name=package,
    packages=find_packages('.'),
    version=version,
    description="Generate API documentation from integration tests",
    url='',
    entry_points={
        'nose.plugins.0.10': [
            'docsgen = django_docs_from_tests.nose_plugin:HelloWorld',
        ]
    }
)

