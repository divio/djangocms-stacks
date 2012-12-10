from setuptools import setup, find_packages


setup(
    name = "djangocms-stacks",
    version = __import__('stacks').__version__,
    url = 'http://github.com/divio/djangocms-stacks',
    license = 'BSD',
    platforms=['OS Independent'],
    description = "Stacks: Re-usable content blocks in django CMS.",
    long_description = open('README.rst').read() + u'\n' + open('HISTORY.rst').read(),
    author = 'Divio AG',
    author_email = 'developers@divio.ch',
    packages=find_packages(),
    install_requires = (
        # 'Django>=1.3,<1.5',  # no need to limit while in development
        'Django>=1.3',
        'django-cms>=2.3',
        'Django-Select2',
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
