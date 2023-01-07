## Siddha Scraper 

A python script that converts [Kapil Gupta](https://twitter.com/KapilGuptaMD)'s public discourses (articles) into textfiles via command-line interface. 

Note: all of the content being downloaded is free and public information available on Kapil Gupta's [website](https://www.kapilguptamd.com/).

**Usage:** 
1. Clone / download this repo: 
```
git clone https://github.com/rayankermanshahani/siddhascraper
```
2. Change into the downloaded directory: 
```
cd siddhascraper/
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
The following command would create a file called: `a-thing-like-no-other.txt`

```
./siddhascraper.py https://www.kapilguptamd.com/2022/12/29/a-thing-like-no-other/
``` 
