from setuptools import setup

setup(name='finwic',
        version='0.1',
        description='Creates a word cloud from filenames',
        url='https://github.com/lawrencehlee/finwic',
        author='Lawrence H Lee',
        author_email='Lee.LawrenceH@gmail.com'
        license='MIT',
        packages=['finwic'],
        install_requires=[
            'wordcloud'
        ],
        zip_safe=False)
