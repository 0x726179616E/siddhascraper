## siddhascraper

`siddhascraper` is a python program that downloads [Kapil Gupta](https://twitter.com/KapilGuptaMD)'s public discourses (articles) as textfiles via a command-line interface. 

I sincerely thank Kapil Gupta for sharing his work with the world.

**Usage:** 
1. Clone / download this repo and navigate into it:
```
git clone https://github.com/0xtwosix/siddhascraper && cd siddhascraper
```
2. Install dependencies via pip: 
```
pip install -r requirements.txt
```
3. Make the script executable:
```
chmod +x siddhascraper.py
```
4. Run the python script with an article link as an argument:
```
./siddhascraper.py <ARTICLE_URL>
```
5. The script creates a textfile with the name of the discource

<br>

**Example:**

The following command creates a file called: `a-thing-like-no-other.txt` and stores it within a directory named `discourses/`:

```
./siddhascraper.py https://www.kapilguptamd.com/2022/12/29/a-thing-like-no-other/

Successfully scraped: https://www.kapilguptamd.com/2022/12/29/a-thing-like-no-other/

All done.
``` 

This discourse is now downloaded at: `./discourses/a-thing-like-no-other.txt`.
