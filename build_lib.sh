#Build library script, also include upload script

python setup.py sdist bdist_wheel,
twine upload --repository pypi dist/* --verbose