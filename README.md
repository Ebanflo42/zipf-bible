# zipf-bible
Demonstrating Zipf's Law using the NIV Bible

## Usage

Use Anaconda to copy my environment:

```
conda env create -f environment.yml
```

If you don't have Anaconda, feel free to pip install all of the packages.

`python preprocess.py` will generate a text file, `raw_text.txt`, from the PDF containing all the text from the Bible, as well as another text file, `cleaned_text.txt`, stripped of newlines, punctuation, and numbers. This script might take 5-10 minutes to run.

`python extract_statistics.py` will generate a text file, `words.txt`, of every word occurring in the Bible (modulo plurals and possessives), as well as a `numpy` array, `frequencies.npy`, specifying the frequency of every word at the given index. These files are useful if you want to performa additional statistics on word occurrences in the Bible.

Finally, `python plot.py` will generate the plot featured in my blog post.