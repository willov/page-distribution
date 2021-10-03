# Distribute pages
This project is meant to distribute pages from an `original.pdf` to a set of people. 
The project reads an `index` file and a `people` file and creates a .pdf file specific for each person. The output files will be named after the person listed in the `people` file, and placed in the out-pdfs directory.
You can either specify the names of the files for the original pdf, index and people when calling the function from command line, have the files be automatically read if they have the right names, or get a prompt from the program else. 

Use case: all files are named `original`, `index`, `people` and will be read automatically 
```
python distribute_pages 
``` 

Use case: file have custom names `example.pdf`, `indf.txt`, `students.txt`
```
python distribute_pages example.pdf, indf.txt, students.txt
``` 

Use case: prompt from the program. Assumes files have non-standard names (compare first use case above)
```
python distribute_pages 
>> Enter original pdf: example.pdf
>> Enter index file: indf.txt
>> Enter people file: students.txt
``` 

## Index file
You must provide an excel spread sheet or comma separated file with an index to what content is available in which pages in the `original.pdf`. Start the first page at 1. Below is an example of the table

|Content|Start page|End page|
|-------|----------|--------|
|subject a | 1 | 20|
|subject b | 21 | 30|

## People file
You must provide an excel spread sheet or comma separated file with what subjects a specific person should be given. 

|Person|Subject a| Subject b|
|-------|------| ---|
|person a| yes| no |
|person b | yes| yes| 

Note: Selection should be binary (yes/no, True/False, 1/0, +/-). 
Note2: Actually, only positive selections have to be given. 