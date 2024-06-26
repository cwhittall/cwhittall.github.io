
# coding: utf-8

# # Publications markdown generator for academicpages
# 
# Takes a TSV of publications with metadata and converts them for use with [academicpages.github.io](academicpages.github.io). This is an interactive Jupyter notebook, with the core python code in publications.py. Run either from the `markdown_generator` folder after replacing `publications.tsv` with one that fits your format.
# 
# TODO: Make this work with BibTex and other databases of citations, rather than Stuart's non-standard TSV format and citation style.
# 

# ## Data format
# 
# The TSV needs to have the following columns: pub_date, title, venue, excerpt, citation, site_url, and arxiv_url, with a header at the top. 
# 
# - `excerpt` and `arxiv_url` can be blank, but the others must have values. 
# - `pub_date` must be formatted as YYYY-MM-DD.
# - `url_slug` will be the descriptive part of the .md file and the permalink URL for the page about the paper. The .md file will be `YYYY-MM-DD-[url_slug].md` and the permalink will be `https://[yourdomain]/publications/YYYY-MM-DD-[url_slug]`


# ## Import pandas
# 
# We are using the very handy pandas library for dataframes.

# In[2]:

import pandas as pd


# ## Import TSV
# 
# Pandas makes this easy with the read_csv function. We are using a TSV, so we specify the separator as a tab, or `\t`.
# 
# I found it important to put this data in a tab-separated values format, because there are a lot of commas in this kind of data and comma-separated values can get messed up. However, you can modify the import statement, as pandas also has read_excel(), read_json(), and others.

# In[3]:

publications = pd.read_csv("publications.tsv", sep="\t", header=0)
publications


# ## Escape special characters
# 
# YAML is very picky about how it takes a valid string, so we are replacing single and double quotes (and ampersands) with their HTML encoded equivilents. This makes them look not so readable in raw format, but they are parsed and rendered nicely.

# In[4]:

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    """Produce entities within text."""
    return "".join(html_escape_table.get(c,c) for c in text)


# ## Creating the markdown files
# 
# This is where the heavy lifting is done. This loops through all the rows in the TSV dataframe, then starts to concatentate a big string (```md```) that contains the markdown for each type. It does the YAML metadata first, then does the description for the individual page. If you don't want something to appear (like the "Recommended citation")

# In[5]:

import os
for row, item in publications.iterrows():
    print(item)
    md_filename = str(item.pub_date) + "-" + item.url_slug + ".md"
    html_filename = str(item.pub_date) + "-" + item.url_slug
    year = item.pub_date[:4]
    
    if len(str(item.arxiv_id)) > 3:
        arxiv_url = f"https://arxiv.org/abs/{item.arxiv_id}";
        arxiv_str = f"arXiv:{item.arxiv_id}";

    ## YAML variables
    
    md = "---\ntitle: \""   + item.title + '"\n'
    
    md += """collection: publications"""
    
    md += """\npermalink: /publication/""" + html_filename
    
    if len(str(item.excerpt)) > 5:
        md += "\nexcerpt: '" + html_escape(item.excerpt) + "'"
    
    md += "\ndate: " + str(item.pub_date) 
    
    md += "\nvenue: '" + html_escape(item.venue) + "'"
    
    if len(str(item.journal_url)) > 5:
        md += "\npaperurl: '" + item.journal_url + "'"
    elif len(str(item.arxiv_id)) > 5:
        md += "\npaperurl: '" + arxiv_url + "'"
    
    md += "\ncitation: '" + html_escape(item.citation) + "'"
    
    if len(str(item.illustration)) > 3:
        md += "\nillustration: " + html_escape(item.illustration);

    if len(str(item.illustration2)) > 3:
        md += "\nillustration2: " + html_escape(item.illustration2);
    
    md += "\n---"
    
    ## Markdown description for individual page
    
    if len(str(item.illustration)) > 3:
        md += "\n<head>\n<style>\nimg {\n padding-right: 20px; \n}\n </style>\n</head>"
    
    if len(str(item.journal_url)) > 5:
        md += "\n\n<a href='" + item.journal_url + f"'>Link to {item.venue} entry</a>\n" 
  
    if len(str(item.arxiv_id)) > 3:
        md += "\n\n<a href='" + arxiv_url + f"'>Link to arxiv entry</a>\n" 
        #md += f"\n\n[{arxiv_str}]({arxiv_url})\n";
      
  
    if len(str(item.excerpt)) > 5:
        md += "\n" + html_escape(item.excerpt) + "\n"
        
    #md += "\nRecommended citation: " + item.citation
    
    if len(str(item.illustration)) > 3:
        md += "\n<div>"
        md += f"\n<image style=\"float:left\" width=\"360\" height=\"360\" src=\"{item.illustration}\" />"
        
        if len(str(item.illustration2)) > 3:
            md += f"\n<image style=\"float:left\" width=\"360\" height=\"360\" src=\"{item.illustration2}\" />"
        md += "\n</div>\n"
    
    md_filename = os.path.basename(md_filename)
       
    with open("../_publications/" + md_filename, 'w') as f:
        f.write(md)


