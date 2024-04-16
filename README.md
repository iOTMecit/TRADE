# PMD - CPD

For linux:

$ cd $HOME
$ wget https://github.com/pmd/pmd/releases/download/pmd_releases%2F7.0.0/pmd-dist-7.0.0-bin.zip
$ unzip pmd-dist-7.0.0-bin.zip
$ alias pmd="$HOME/pmd-bin-7.0.0/bin/pmd"
$ pmd check -d /usr/src -R rulesets/java/quickstart.xml -f text

After installation go to directory of code to be analyze by terminal
After:
$ pmd cpd --minimum-tokens 30 --dir components/ --language python --format text > cpd_results.xml


# Nicad

After installation go to directory of code to be analyze by terminal 
	
	cd NiCad-6.1

Create a directory to hold the source systems and results of the NiCad clone analysis. If you're running NiCad in place, the ./systems directory in the NiCad distribution directory is appropriate.
	
	mkdir ./systems
	
Copy the entire source directory of the system you want to analyze to the analysis directory

	cp -r ./examples/JHotDraw ./systems/

Run the NiCad command, specifying the analysis granularity and language of the system you want to analyze. 

	./nicad6 functions python systems/JHotDraw default-report

# Simian

After installation go to directory of code to be analyze by terminal 
	
	cd simian
	
Copy the code to be analyze inside of simian directory

Run simian command

	java -jar simian.jar -formatter=xml:output.xml "**/*.py"

