import setuptools

setuptools.setup(
    name="lymworkbook",
    version="0.0.1",
    author="Kushal Das",
    author_email="mail@kushaldas.in",
    description="Work book for LYM",
    license="GPLv3+",
    url="https://github.com/kushaldas/lymworkbook",
    packages=["lymworkbook", "lymproblems"],
    include_package_data=True,
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
    entry_points={
        "console_scripts": [
            "lymsetup = lymworkbook:workbook_setup",
            "lymverify = lymworkbook:workbook_verify",
        ]
    },
)
