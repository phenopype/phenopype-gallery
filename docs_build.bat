@echo off
@echo .doctrees > docs/.gitignore

if "%*"=="-t" (
	rmdir /Q /S _temp
)

if "%*"=="-d" (
	rmdir /Q /S docs
)

if "%*"=="-p1" (
	python deploy.py --find-notebooks True
)

if "%*"=="-p2" (
	python deploy.py --find-notebooks True --compile-zips True
)

if "%*"=="-p3" (
	python deploy.py --find-notebooks True --upload-gdrive True
)

if "%*"=="-p4" (
	python deploy.py --find-notebooks True --upload-gdrive-ow True
)

sphinx-build -a docs_source docs 

if "%*"=="-o" (
	cd docs
	rmdir ".git" /S /Q
	git init
	@echo .doctrees > .gitignore
	git add .
	git commit -m "- auto-generated with sphinx -"
	git remote add origin https://github.com/phenopype/static-phenopype-gallery
	git push --force origin main
	cd ..
)