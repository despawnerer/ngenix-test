NGENIX test task
================

Requirements
------------

- make
- python 3


Step 1: Create zip files
------------------------

`zips` dir will be created and 50 zip files will be put in there named `0.zip` `1.zip` and so on.

	make zips


Step 2: Create CSV files
------------------------

`csvs` dir will be created and two csv files inside it with data extracted from zip files created in step 1.

	make csvs


Cleanup
-------

Remove all generated files.

	make clean
