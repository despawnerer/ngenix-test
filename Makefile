.PHONY: zips csvs clean

zips:
	./make_zips.py

csvs:
	./make_csvs.py

clean:
	rm -rf zips
	rm -rf csvs
