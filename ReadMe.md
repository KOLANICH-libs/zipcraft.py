zipcraft.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===========
~~[wheel (GitLab)](https://gitlab.com/KOLANICH/zipcraft.py/-/jobs/artifacts/master/raw/dist/zipcraft-0.CI-py3-none-any.whl?job=build)~~
[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/zipcraft.py/workflows/CI/master/zipcraft-0.CI-py3-none-any.whl)
![GitLab Build Status](https://gitlab.com/KOLANICH-libs/zipcraft.py/badges/master/pipeline.svg)
~~![GitLab Coverage](https://gitlab.com/KOLANICH/zipcraft.py/badges/master/coverage.svg)~~
[![Coveralls Coverage](https://img.shields.io/coveralls/KOLANICH-libs/zipcraft.py.svg)](https://coveralls.io/r/KOLANICH-libs/zipcraft.py)
[![GitHub Actions](https://github.com/KOLANICH-libs/zipcraft.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/zipcraft.py/actions/)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/zipcraft.py.svg)](https://libraries.io/github/KOLANICH-libs/zipcraft.py)

This library allows you to edit `zipfile`s in-place, something that `zipfile` doesn't allow you.

Not fully, but in some assumption:

* only uncompressed files within archive can be edited. Archives of uncompressed files are very widespread as containers, examples are:
	* python wheels
	* Mozilla Firefox extensions

* you can overwrite existing files, you cannot delete them. It would require shifting.

* the content you writes must occupy exactly the same size. You must yourself find the most suitable way for you to make it occupy the needed size. I. e. some file formats have padding.

In these assumptions the task is very easy:

1. Find in headers the offset of the file within archive.
2. Seek to that offset.
3. Overwrite the data.
