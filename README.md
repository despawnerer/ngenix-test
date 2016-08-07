NGENIX test task
================

Requirements
------------

- make
- python 3


Step 1: Create zip files
------------------------

Create a `zips` dir and 50 zip files named `0.zip` `1.zip` and so on, with the required contents inside.

	make zips


Step 2: Create CSV files
------------------------

Create a `csvs` dir with two csv files filled with data extracted from zip files that were created in step 1.

	make csvs


Cleanup
-------

Remove all generated files.

	make clean
