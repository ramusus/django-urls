from setuptools import setup, find_packages

setup(
    name='django-urls',
    version=__import__('django_urls').__version__,
    description="Experimental replacement for Django's get_absolute_url() method.",
    long_description=open('README.txt').read(),
    author='Simon Wilson',
    author_email='simon@simonwillison.net',
    url='https://github.com/ramusus/django-urls',
    download_url='https://github.com/ramusus/django-urls/downloads',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
